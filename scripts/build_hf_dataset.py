#!/usr/bin/env python3
"""Genereert de HuggingFace-dataset-artefacten uit de live /arena/data.json
van djangodevreng.nl.

Eén bron van waarheid: de website publiceert de gecureerde, gescoorde dataset
als data.json, deze repo publiceert die naar HuggingFace. Zo blijft de
website-repo schoon en leeft alle dataset-publicatie hier, bij de data.

    python scripts/build_hf_dataset.py        # schrijft hf-dataset/
    hf upload Djangodevreng/dgx-spark-benchmarks ./hf-dataset . --repo-type=dataset
"""

import csv
import json
import os
import urllib.request

DATA_URL = "https://djangodevreng.nl/arena/data.json"
OUT_DIR = "hf-dataset"


def main() -> None:
    req = urllib.request.Request(DATA_URL, headers={"User-Agent": "dgx-spark-benchmarks-sync"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)

    os.makedirs(OUT_DIR, exist_ok=True)
    preset_ids = [p["id"] for p in data["presets"]]

    # models.csv: één rij per model (meta + quality + scores per preset).
    with open(os.path.join(OUT_DIR, "models.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "model_id", "name", "vendor", "architecture", "params_b",
                "vram_gb", "context_k", "precision", "mmlu", "gpqa",
                "humaneval", "quality_avg", "size_bucket",
                *[f"score_{p}" for p in preset_ids],
                "detail_url", "markdown_url",
            ]
        )
        for m in data["models"]:
            q = m["quality"]
            w.writerow(
                [
                    m["id"], m["name"], m["vendor"], m["architecture"],
                    m["params"], m["vramGb"], m["contextK"], m["precision"],
                    q["mmlu"], q["gpqa"], q["humaneval"], q["avg"],
                    m["sizeBucket"],
                    *[m["scores"].get(p, "") for p in preset_ids],
                    m["detailUrl"], m["markdownUrl"],
                ]
            )

    # results.csv: long-format, één rij per gemeten (model, benchmark).
    bench = {b["id"]: b for b in data["benchmarks"]}
    with open(os.path.join(OUT_DIR, "results.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "model_id", "benchmark_id", "benchmark_num", "benchmark_title",
                "mode", "tokens_per_sec_per_user", "tokens_per_sec_total",
                "ttft_ms",
            ]
        )
        for m in data["models"]:
            for bid, r in m["results"].items():
                b = bench.get(bid, {})
                w.writerow(
                    [
                        m["id"], bid, b.get("num", ""), b.get("title", ""),
                        b.get("mode", ""), r["tokensPerSecPerUser"],
                        r["tokensPerSecTotal"], r["ttftMs"],
                    ]
                )

    # README.md: de dataset-card met YAML-metadata.
    card = f"""---
license: cc-by-4.0
language:
  - en
pretty_name: DGX Spark LLM Arena benchmarks
tags:
  - llm
  - inference
  - benchmark
  - on-prem
  - dgx-spark
  - vllm
size_categories:
  - n<1K
configs:
  - config_name: models
    data_files: models.csv
  - config_name: results
    data_files: results.csv
---

# DGX Spark LLM Arena benchmarks

{data["description"]}

- **Hardware:** {data["hardware"]}
- **Creator:** {data["creator"]} (https://djangodevreng.nl)
- **Visualised:** {data["url"]}
- **Raw runs:** {data["source"]}
- **Last updated:** {data["dateModified"]}

## Configs

- `models`: one row per model ({len(data["models"])} rows). Metadata, quality scores (MMLU-Pro, GPQA-Diamond, HumanEval/LiveCodeBench from vendor model cards) and the leaderboard composite scores per use-case preset.
- `results`: long format, one row per measured (model, benchmark) pair. {len(data["benchmarks"])} benchmarks: five closed-loop (llama-benchy) and four open-loop (vllm bench serve).

```python
from datasets import load_dataset

models = load_dataset("Djangodevreng/dgx-spark-benchmarks", "models")
results = load_dataset("Djangodevreng/dgx-spark-benchmarks", "results")
```

## Method

Three runs per benchmark, fixed seed (42), reported as the mean. Run-to-run variance stays within about 2%. No latency gate: slow models stay visible. Full methodology and the raw stdout per run live in this repo.

## License

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Free to use, including commercially, with attribution: {data["attribution"]}.

## Citation

```bibtex
@misc{{devreng-dgx-spark-benchmarks-2026,
  author = {{Django de Vreng}},
  title  = {{DGX Spark LLM Arena benchmarks}},
  year   = {{2026}},
  url    = {{https://huggingface.co/datasets/Djangodevreng/dgx-spark-benchmarks}}
}}
```
"""
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(card)

    print(
        f"hf-dataset/ geschreven: README.md, models.csv ({len(data['models'])} modellen), "
        f"results.csv (uit {DATA_URL})."
    )


if __name__ == "__main__":
    main()
