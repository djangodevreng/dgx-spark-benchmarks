#!/usr/bin/env python3
"""Stamp existing run metadata with the result-contract version.

Historical commands were not stored as argv arrays. They can still be
reconstructed and checked against the raw logs and JSON outputs, so the stamp
states that provenance explicitly instead of claiming they were captured.
"""

import argparse
import json
import re
from pathlib import Path


FAILED_SANITY = {
    "ministral-3/ministral-3-3b-instruct/bf16",
}


def validity_for(run_dir: Path, root: Path, suite: dict) -> dict:
    relative = run_dir.relative_to(root / "results").as_posix()
    if (run_dir / "_sanity.txt").is_file():
        sanity = "passed"
    elif (run_dir / "_sanity-raw.json").is_file():
        sanity = "failed" if relative in FAILED_SANITY else "captured_unreviewed"
    else:
        sanity = "not_recorded"

    tests = {}
    for test in suite["tests"]:
        test_id = test["id"]
        if test_id == "11-rate-sweep":
            summary_path = run_dir / "11-rate-sweep.json"
            summary = json.loads(summary_path.read_text()) if summary_path.is_file() else {}
            steps = summary.get("steps") or []
            if len(steps) == len(test["requestRates"]):
                tests[test_id] = "complete"
            elif summary.get("aborted_at_rps") is not None:
                tests[test_id] = "aborted"
            elif not steps:
                tests[test_id] = "no_data"
            else:
                tests[test_id] = "incomplete"
        else:
            suffixes = (".md", ".log") if test["mode"] == "closed" else (".json", ".log")
            tests[test_id] = "complete" if all((run_dir / f"{test_id}{suffix}").is_file() for suffix in suffixes) else "incomplete"
    return {"sanity": sanity, "tests": tests}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    suite = json.loads((root / "benchmark-suite.json").read_text())
    changed = 0

    for path in sorted((root / "results").glob("*/*/*/meta.json")):
        data = json.loads(path.read_text())
        expected = {
            "contract_version": suite["contractVersion"],
            "suite_version": suite["suiteVersion"],
            "command_provenance": "reconstructed_from_raw_artifacts",
            "validity": validity_for(path.parent, root, suite),
        }
        needs_stamp = not all(data.get(key) == value for key, value in expected.items())
        if args.write:
            data.update(expected)
            rendered = json.dumps(data, indent=2) + "\n"
            util = data.get("server_config", {}).get("gpu_memory_utilization")
            if isinstance(util, float):
                rendered = re.sub(
                    r'("gpu_memory_utilization": )\d+(?:\.\d+)?',
                    rf"\g<1>{util:.2f}",
                    rendered,
                    count=1,
                )
            if path.read_text() != rendered:
                path.write_text(rendered)
                changed += 1
        elif needs_stamp:
            changed += 1

    action = "stamped" if args.write else "would stamp"
    print(f"{action}: {changed} meta.json files")


if __name__ == "__main__":
    main()
