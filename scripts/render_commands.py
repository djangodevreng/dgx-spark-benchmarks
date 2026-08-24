#!/usr/bin/env python3
"""Render reproducible commands for one published run.

Historical runs are reconstructed from the canonical suite plus meta.json and
are labelled as such. If a future runner stores captured argv arrays in
meta.json, those arrays are emitted verbatim instead.
"""

from __future__ import annotations

import argparse
import json
import shlex
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def flag(argv: list[str], name: str, *values: Any) -> None:
    argv.append(name)
    argv.extend(str(value) for value in values)


def closed_command(meta: dict, test: dict, defaults: dict) -> list[str]:
    argv = ["uvx", f"llama-benchy=={meta['llama_benchy_version']}"]
    flag(argv, "--base-url", defaults["baseUrl"])
    flag(argv, "--model", meta["served_name"])
    flag(argv, "--pp", *test["promptTokens"])
    flag(argv, "--tg", *test["outputTokens"])
    flag(argv, "--depth", *test["depth"])
    flag(argv, "--concurrency", *test["concurrency"])
    flag(argv, "--runs", test["runs"])
    flag(argv, "--latency-mode", "generation")
    flag(argv, "--format", "md")
    return argv


def open_command(meta: dict, test: dict, defaults: dict, rate: float | None = None) -> list[str]:
    argv = ["docker", "exec", "vllm-bench", "vllm", "bench", "serve"]
    flag(argv, "--backend", "openai-chat")
    flag(argv, "--base-url", defaults["openLoopBaseUrl"])
    flag(argv, "--endpoint", "/v1/chat/completions")
    flag(argv, "--model", meta["model"])
    flag(argv, "--tokenizer", meta["model"])
    flag(argv, "--served-model-name", meta["served_name"])
    flag(argv, "--dataset-name", test["dataset"])
    if test["dataset"] == "random":
        flag(argv, "--random-input-len", test["randomInputTokens"])
        flag(argv, "--random-output-len", test["randomOutputTokens"])
        flag(argv, "--random-range-ratio", defaults["randomRangeRatio"])
    else:
        flag(argv, "--dataset-path", test["datasetPath"])

    request_rate = test.get("requestRate") if rate is None else rate
    prompts = test.get("numPrompts")
    if rate is not None:
        prompts = max(test["minimumPrompts"], round(rate * test["arrivalWindowSeconds"]))
    flag(argv, "--num-prompts", prompts)
    flag(argv, "--request-rate", request_rate)
    flag(argv, "--burstiness", test["burstiness"])
    if test.get("maxConcurrency") is not None:
        flag(argv, "--max-concurrency", test["maxConcurrency"])
    flag(argv, "--percentile-metrics", "ttft,tpot,itl,e2el")
    flag(argv, "--metric-percentiles", ",".join(str(value) for value in defaults["metricPercentiles"]))
    flag(argv, "--seed", defaults["seed"])
    argv.append("--save-result")
    flag(argv, "--result-dir", "/tmp")
    filename = f"{test['id']}.json" if rate is None else f"{test['id']}-{rate:.1f}.json"
    flag(argv, "--result-filename", filename)
    return argv


def commands(meta: dict, suite: dict, selected: str | None) -> list[tuple[str, list[str]]]:
    captured = meta.get("commands") if meta.get("command_provenance") == "captured" else None
    output = []
    for test in suite["tests"]:
        test_id = test["id"]
        if selected and selected != test_id:
            continue
        if captured is not None:
            output.append((test_id, captured[test_id]))
        elif test_id == "11-rate-sweep":
            for rate in test["requestRates"]:
                output.append((f"{test_id} @ {rate:.1f} req/s", open_command(meta, test, suite["defaults"], rate)))
        elif test["mode"] == "closed":
            output.append((test_id, closed_command(meta, test, suite["defaults"])))
        else:
            output.append((test_id, open_command(meta, test, suite["defaults"])))
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path, help="run directory or its meta.json")
    parser.add_argument("--test", help="render only one test id")
    args = parser.parse_args()

    meta_path = args.run if args.run.name == "meta.json" else args.run / "meta.json"
    if not meta_path.is_file():
        parser.error(f"meta.json not found at {meta_path}")
    meta = json.loads(meta_path.read_text())
    suite = json.loads((ROOT / "benchmark-suite.json").read_text())
    known = {test["id"] for test in suite["tests"]}
    if args.test and args.test not in known:
        parser.error(f"unknown test id {args.test!r}")

    provenance = meta.get("command_provenance", "unknown")
    print(f"# command provenance: {provenance}", file=sys.stderr)
    for label, argv in commands(meta, suite, args.test):
        print(f"# {label}")
        print(shlex.join(argv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
