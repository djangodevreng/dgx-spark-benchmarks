#!/usr/bin/env python3
"""Validate every published run against benchmark-suite.json.

The checks intentionally use only the Python standard library so the same
command works locally and in GitHub Actions without installing dependencies.
"""

from __future__ import annotations

import itertools
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SUITE_PATH = ROOT / "benchmark-suite.json"
META_REQUIRED = {
    "contract_version",
    "suite_version",
    "command_provenance",
    "validity",
    "profile",
    "model",
    "served_name",
    "vllm_image",
    "vllm_version_reported",
    "llama_benchy_version",
    "hardware",
    "driver_version",
    "vbios_version",
    "server_config",
    "generated_at",
}
SERVER_REQUIRED = {
    "max_model_len",
    "gpu_memory_utilization",
    "kv_cache_dtype",
    "enable_prefix_caching",
    "async_scheduling",
    "extra_vllm_args",
    "profile_env_vars",
}
PROVENANCE_VALUES = {"captured", "reconstructed_from_raw_artifacts"}
SANITY_VALUES = {"passed", "failed", "captured_unreviewed", "not_recorded"}
TEST_STATUS_VALUES = {"complete", "aborted", "no_data", "incomplete"}


class Validation:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.runs = 0
        self.tests = 0
        self.sanity_counts: dict[str, int] = {}
        self.test_status_counts: dict[str, int] = {}

    def check(self, condition: bool, location: Path | str, message: str) -> None:
        if not condition:
            self.errors.append(f"{location}: {message}")


def load_json(path: Path, validation: Validation) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        validation.errors.append(f"{path}: invalid JSON ({exc})")
        return None
    if not isinstance(value, dict):
        validation.errors.append(f"{path}: expected a JSON object")
        return None
    return value


def close(a: Any, b: Any) -> bool:
    return isinstance(a, (int, float)) and math.isclose(float(a), float(b), abs_tol=1e-9)


def expected_closed_cells(test: dict[str, Any]) -> set[str]:
    cells = set()
    for pp, tg, depth, concurrency in itertools.product(
        test["promptTokens"],
        test["outputTokens"],
        test["depth"],
        test["concurrency"],
    ):
        depth_label = f" @ d{depth}" if depth else ""
        cells.add(f"pp{pp}{depth_label} (c{concurrency})")
        cells.add(f"tg{tg}{depth_label} (c{concurrency})")
    return cells


def actual_closed_cells(markdown: str) -> set[str]:
    cells = set()
    for line in markdown.splitlines():
        if not line.startswith("|") or "(c" not in line:
            continue
        columns = [part.strip() for part in line.split("|")[1:-1]]
        if len(columns) >= 2 and re.fullmatch(r"(?:pp|tg)\d+(?: @ d\d+)? \(c\d+\)", columns[1]):
            cells.add(columns[1])
    return cells


def namespace_value(log: str, key: str) -> str | None:
    match = re.search(rf"(?:Namespace\(|, ){re.escape(key)}=([^,)]+)", log)
    return match.group(1).strip("'\"") if match else None


def validate_suite(suite: dict[str, Any], validation: Validation) -> list[dict[str, Any]]:
    validation.check(suite.get("contractVersion") == 1, SUITE_PATH, "contractVersion must be 1")
    validation.check(isinstance(suite.get("suiteVersion"), str), SUITE_PATH, "suiteVersion is required")
    tests = suite.get("tests")
    validation.check(isinstance(tests, list), SUITE_PATH, "tests must be an array")
    if not isinstance(tests, list):
        return []
    ids = [test.get("id") for test in tests if isinstance(test, dict)]
    validation.check(len(tests) == 11, SUITE_PATH, "expected exactly 11 tests")
    validation.check(len(set(ids)) == len(ids), SUITE_PATH, "test ids must be unique")
    validation.check(sum(test.get("mode") == "closed" for test in tests) == 6, SUITE_PATH, "expected 6 closed-loop tests")
    validation.check(sum(test.get("mode") == "open" for test in tests) == 5, SUITE_PATH, "expected 5 open-loop tests")
    return tests


def validate_meta(path: Path, meta: dict[str, Any], suite: dict[str, Any], validation: Validation) -> None:
    missing = sorted(META_REQUIRED - meta.keys())
    validation.check(not missing, path, f"missing keys: {', '.join(missing)}")
    validation.check(meta.get("contract_version") == suite.get("contractVersion"), path, "contract version mismatch")
    validation.check(meta.get("suite_version") == suite.get("suiteVersion"), path, "suite version mismatch")
    validation.check(meta.get("command_provenance") in PROVENANCE_VALUES, path, "invalid command_provenance")
    if meta.get("command_provenance") == "captured":
        commands = meta.get("commands")
        validation.check(isinstance(commands, dict) and len(commands) == 11, path, "captured provenance requires 11 command arrays")
        if isinstance(commands, dict):
            for test_id, argv in commands.items():
                validation.check(isinstance(argv, list) and all(isinstance(v, str) for v in argv), path, f"commands.{test_id} must be a string array")
    server = meta.get("server_config")
    validation.check(isinstance(server, dict), path, "server_config must be an object")
    if isinstance(server, dict):
        missing_server = sorted(SERVER_REQUIRED - server.keys())
        validation.check(not missing_server, path, f"server_config missing: {', '.join(missing_server)}")
        util = server.get("gpu_memory_utilization")
        validation.check(isinstance(util, (int, float)) and 0 < util <= 1, path, "gpu_memory_utilization must be in (0, 1]")
    try:
        datetime.fromisoformat(str(meta.get("generated_at")))
    except ValueError:
        validation.check(False, path, "generated_at must be ISO 8601")

    validity = meta.get("validity")
    validation.check(isinstance(validity, dict), path, "validity must be an object")
    if isinstance(validity, dict):
        sanity = validity.get("sanity")
        validation.check(sanity in SANITY_VALUES, path, "invalid validity.sanity")
        if sanity in SANITY_VALUES:
            validation.sanity_counts[sanity] = validation.sanity_counts.get(sanity, 0) + 1
        statuses = validity.get("tests")
        validation.check(isinstance(statuses, dict), path, "validity.tests must be an object")
        if isinstance(statuses, dict):
            expected_ids = {test["id"] for test in suite["tests"]}
            validation.check(set(statuses) == expected_ids, path, "validity.tests must cover exactly the suite ids")
            for test_id, status in statuses.items():
                validation.check(status in TEST_STATUS_VALUES, path, f"invalid status for {test_id}: {status}")
                if status in TEST_STATUS_VALUES:
                    validation.test_status_counts[status] = validation.test_status_counts.get(status, 0) + 1


def validate_sanity(run_dir: Path, meta: dict[str, Any], validation: Validation) -> None:
    status = (meta.get("validity") or {}).get("sanity")
    text_exists = (run_dir / "_sanity.txt").is_file()
    raw_exists = (run_dir / "_sanity-raw.json").is_file()
    if status == "passed":
        validation.check(text_exists, run_dir, "sanity=passed requires _sanity.txt")
    elif status in {"failed", "captured_unreviewed"}:
        validation.check(raw_exists, run_dir, f"sanity={status} requires _sanity-raw.json")
    elif status == "not_recorded":
        validation.check(not text_exists and not raw_exists, run_dir, "sanity=not_recorded conflicts with a sanity artifact")


def validate_closed(run_dir: Path, meta: dict[str, Any], test: dict[str, Any], validation: Validation) -> None:
    test_id = test["id"]
    md_path = run_dir / f"{test_id}.md"
    log_path = run_dir / f"{test_id}.log"
    validation.check(md_path.is_file(), md_path, "missing result table")
    validation.check(log_path.is_file(), log_path, "missing raw log")
    if not md_path.is_file() or not log_path.is_file():
        return
    markdown = md_path.read_text(errors="replace")
    log = log_path.read_text(errors="replace")
    expected = expected_closed_cells(test)
    actual = actual_closed_cells(markdown)
    validation.check(actual == expected, md_path, f"benchmark cells differ: missing={sorted(expected - actual)}, extra={sorted(actual - expected)}")
    validation.check(f"llama-benchy ({meta.get('llama_benchy_version')})" in log, log_path, "llama-benchy version differs from meta.json")
    validation.check(f"Benchmarking model: {meta.get('served_name')} " in log, log_path, "served model differs from meta.json")
    validation.tests += 1


def validate_open_result(path: Path, meta: dict[str, Any], test: dict[str, Any], validation: Validation) -> None:
    data = load_json(path, validation)
    if data is None:
        return
    expected_prompts = test["numPrompts"]
    validation.check(data.get("num_prompts") == expected_prompts, path, f"num_prompts must be {expected_prompts}")
    validation.check(close(data.get("request_rate"), test["requestRate"]), path, f"request_rate must be {test['requestRate']}")
    validation.check(close(data.get("burstiness"), test["burstiness"]), path, f"burstiness must be {test['burstiness']}")
    validation.check(data.get("max_concurrency") == test["maxConcurrency"], path, f"max_concurrency must be {test['maxConcurrency']}")
    validation.check(data.get("model_id") == meta.get("model"), path, "model_id differs from meta.json")
    validation.check(data.get("tokenizer_id") == meta.get("model"), path, "tokenizer_id differs from meta.json")
    completed = data.get("completed")
    failed = data.get("failed")
    validation.check(isinstance(completed, int) and isinstance(failed, int), path, "completed and failed must be integers")
    if isinstance(completed, int) and isinstance(failed, int):
        validation.check(completed + failed == expected_prompts, path, "completed + failed must equal num_prompts")


def validate_open(run_dir: Path, meta: dict[str, Any], test: dict[str, Any], defaults: dict[str, Any], validation: Validation) -> None:
    test_id = test["id"]
    json_path = run_dir / f"{test_id}.json"
    log_path = run_dir / f"{test_id}.log"
    validation.check(json_path.is_file(), json_path, "missing raw JSON")
    validation.check(log_path.is_file(), log_path, "missing raw log")
    if not json_path.is_file() or not log_path.is_file():
        return
    validate_open_result(json_path, meta, test, validation)
    log = log_path.read_text(errors="replace")
    expected_namespace = {
        "seed": defaults["seed"],
        "dataset_name": repr(test["dataset"]),
        "num_prompts": test["numPrompts"],
        "request_rate": test["requestRate"],
        "burstiness": test["burstiness"],
        "max_concurrency": test["maxConcurrency"],
        "model": repr(meta["model"]),
        "tokenizer": repr(meta["model"]),
        "served_model_name": repr(meta["served_name"]),
        "save_result": True,
        "result_filename": repr(f"{test_id}.json"),
    }
    if test["dataset"] == "random":
        expected_namespace.update({
            "random_input_len": test["randomInputTokens"],
            "random_output_len": test["randomOutputTokens"],
            "random_range_ratio": repr(str(defaults["randomRangeRatio"])),
        })
    else:
        expected_namespace["dataset_path"] = repr(test["datasetPath"])
    for key, value in expected_namespace.items():
        actual = namespace_value(log, key)
        expected = str(value).strip("'\"")
        validation.check(actual == expected, log_path, f"{key}={actual!r}, expected {expected!r}")
    validation.tests += 1


def sweep_prompts(test: dict[str, Any], rate: float) -> int:
    return max(test["minimumPrompts"], round(rate * test["arrivalWindowSeconds"]))


def validate_sweep(run_dir: Path, meta: dict[str, Any], test: dict[str, Any], validation: Validation) -> None:
    summary_path = run_dir / "11-rate-sweep.json"
    log_path = run_dir / "11-rate-sweep.log"
    summary = load_json(summary_path, validation) if summary_path.is_file() else None
    validation.check(summary_path.is_file(), summary_path, "missing sweep summary")
    validation.check(log_path.is_file(), log_path, "missing raw sweep log")
    status = ((meta.get("validity") or {}).get("tests") or {}).get(test["id"])
    summary_steps = summary.get("steps") if summary is not None else []
    summary_rates = [item.get("configured_rps") for item in summary_steps if isinstance(item, dict)] if isinstance(summary_steps, list) else []
    expected_raw_rates = summary_rates
    if status == "complete":
        validation.check(summary_rates == test["requestRates"], summary_path, "complete sweep must contain every configured rate")
    elif status == "aborted":
        aborted_at = summary.get("aborted_at_rps") if summary is not None else None
        validation.check(aborted_at in test["requestRates"], summary_path, "aborted sweep needs a configured aborted_at_rps")
        validation.check(all(rate < aborted_at for rate in summary_rates), summary_path, "aborted sweep may only contain completed earlier steps")
    elif status == "no_data":
        validation.check(not summary_rates, summary_path, "no_data sweep cannot contain completed steps")
    else:
        validation.check(False, summary_path, f"rate sweep has unresolved status {status!r}")

    seen_rates = []
    for rate in expected_raw_rates:
        rate_label = f"{rate:.1f}"
        path = run_dir / f"11-rate-sweep-{rate_label}.json"
        validation.check(path.is_file(), path, "missing sweep step")
        if not path.is_file():
            continue
        step = dict(test)
        step["requestRate"] = rate
        step["numPrompts"] = sweep_prompts(test, rate)
        validate_open_result(path, meta, step, validation)
        seen_rates.append(rate)
    if summary is not None:
        steps = summary.get("steps")
        validation.check(isinstance(steps, list), summary_path, "steps must be an array")
        if isinstance(steps, list):
            validation.check(summary_rates == seen_rates[:len(summary_rates)], summary_path, "summary rates do not match raw steps")
        validation.check(summary.get("model") == meta.get("model"), summary_path, "model differs from meta.json")
        validation.check(summary.get("served_name") == meta.get("served_name"), summary_path, "served_name differs from meta.json")
    validation.tests += 1


def main() -> int:
    validation = Validation()
    suite = load_json(SUITE_PATH, validation)
    if suite is None:
        return report(validation)
    tests = validate_suite(suite, validation)
    defaults = suite.get("defaults", {})

    meta_paths = sorted(RESULTS.glob("*/*/*/meta.json"))
    validation.check(bool(meta_paths), RESULTS, "no runs found")
    for meta_path in meta_paths:
        run_dir = meta_path.parent
        meta = load_json(meta_path, validation)
        if meta is None:
            continue
        validation.runs += 1
        validate_meta(meta_path, meta, suite, validation)
        validate_sanity(run_dir, meta, validation)
        for test in tests:
            if test.get("mode") == "closed":
                validate_closed(run_dir, meta, test, validation)
            elif test.get("id") == "11-rate-sweep":
                validate_sweep(run_dir, meta, test, validation)
            else:
                validate_open(run_dir, meta, test, defaults, validation)

    return report(validation)


def report(validation: Validation) -> int:
    if validation.errors:
        print(f"FAILED: {len(validation.errors)} error(s)", file=sys.stderr)
        for error in validation.errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"OK: {validation.runs} runs and {validation.tests} test slots match the contract")
    print("sanity: " + ", ".join(f"{key}={value}" for key, value in sorted(validation.sanity_counts.items())))
    print("test status: " + ", ".join(f"{key}={value}" for key, value in sorted(validation.test_status_counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
