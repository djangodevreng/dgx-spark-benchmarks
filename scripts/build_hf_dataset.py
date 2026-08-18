#!/usr/bin/env python3
"""Genereert de HuggingFace-dataset-artefacten uit de live /arena/data.json
van djangodevreng.nl.

Eén bron van waarheid: de website publiceert de gecureerde, gescoorde dataset
als data.json, deze repo publiceert die naar HuggingFace. Zo blijft de
website-repo schoon en leeft alle dataset-publicatie hier, bij de data.

    python scripts/build_hf_dataset.py        # schrijft hf-dataset/
    hf upload Djangodevreng/dgx-spark-benchmarks ./hf-dataset . --repo-type=dataset

Over de kwaliteitsscores: de site levert ze als knowledge/science/coding, elk
met de benchmark waar het cijfer vandaan komt. Dat label hoort in de dataset,
want het verschilt per model -- knowledge is bij het ene model MMLU-Pro en bij
het andere gewoon MMLU, en coding loopt van LiveCodeBench v5 tot HumanEval+.
Eén kolom `mmlu` zou die verschillen wegpoetsen.
"""

import csv
import json
import os
import sys
import urllib.request

DATA_URL = "https://djangodevreng.nl/arena/data.json"
OUT_DIR = "hf-dataset"

# De kwaliteitsdimensies zoals de site ze publiceert.
QUALITY_DIMS = ("knowledge", "science", "coding")


def quality_of(model: dict, dim: str) -> tuple:
    """(waarde, benchmarknaam) voor een kwaliteitsdimensie.

    Valt terug op qualityLegacy zolang de site die meelevert, zodat een
    halve schema-wijziging aan de kant van de website deze sync niet breekt.
    """
    q = (model.get("quality") or {}).get(dim)
    if isinstance(q, dict):
        return q.get("value"), q.get("bench")
    legacy_key = {"knowledge": "mmlu", "science": "gpqa", "coding": "humaneval"}[dim]
    return (model.get("qualityLegacy") or {}).get(legacy_key), None


def title_of(bench: dict) -> str:
    """Testnaam zoals die in de repo en op de arena heet, bv. `02-rag-8k`.

    De site levert geen `title` meer mee; nummer + id samenvoegen geeft precies
    de naam die ook de resultaatbestanden in deze repo dragen, dus dat is
    bruikbaarder dan een verzonnen titel.
    """
    if bench.get("title"):
        return bench["title"]
    num, bid = bench.get("num", ""), bench.get("id", "")
    return f"{num}-{bid}" if num and bid else bid


def blank(v) -> str:
    return "" if v is None else v


def main() -> None:
    req = urllib.request.Request(DATA_URL, headers={"User-Agent": "dgx-spark-benchmarks-sync"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)

    # Vroeg en luid falen als de bron van vorm verandert, in plaats van een
    # kale KeyError diep in een schrijflus.
    for key in ("models", "benchmarks", "presets"):
        if not data.get(key):
            sys.exit(f"data.json mist '{key}' of het is leeg -- schema gewijzigd?")

    os.makedirs(OUT_DIR, exist_ok=True)
    preset_ids = [p["id"] for p in data["presets"]]

    # models.csv: één rij per model (meta + kwaliteit + scores per preset).
    with open(os.path.join(OUT_DIR, "models.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "model_id", "name", "vendor", "architecture", "params_b",
                "vram_gb", "context_k", "precision",
                *[c for d in QUALITY_DIMS for c in (d, f"{d}_bench")],
                "quality_avg", "size_bucket",
                *[f"score_{p}" for p in preset_ids],
                "detail_url", "markdown_url",
            ]
        )
        for m in data["models"]:
            quality_cells = []
            for dim in QUALITY_DIMS:
                value, bench = quality_of(m, dim)
                quality_cells += [blank(value), blank(bench)]
            avg = m.get("qualityAvg")
            if avg is None:
                avg = (m.get("qualityLegacy") or {}).get("avg")
            w.writerow(
                [
                    m.get("id"), m.get("name"), m.get("vendor"), m.get("architecture"),
                    m.get("params"), m.get("vramGb"), m.get("contextK"), m.get("precision"),
                    *quality_cells,
                    blank(avg), m.get("sizeBucket"),
                    *[m.get("scores", {}).get(p, "") for p in preset_ids],
                    m.get("detailUrl"), m.get("markdownUrl"),
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
            for bid, r in (m.get("results") or {}).items():
                b = bench.get(bid, {})
                w.writerow(
                    [
                        m.get("id"), bid, b.get("num", ""), title_of(b),
                        b.get("mode", ""), blank(r.get("tokensPerSecPerUser")),
                        blank(r.get("tokensPerSecTotal")), blank(r.get("ttftMs")),
                    ]
                )

    n_closed = sum(1 for b in data["benchmarks"] if b.get("mode") == "closed")
    n_open = sum(1 for b in data["benchmarks"] if b.get("mode") == "open")
    # Niet elke test van de suite haalt de per-model resultaten van de site;
    # de card moet zeggen wat er daadwerkelijk in results.csv staat.
    covered = {bid for m in data["models"] for bid in (m.get("results") or {})}

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

- `models`: one row per model ({len(data["models"])} rows). Metadata, quality scores and the leaderboard composite scores per use-case preset.
- `results`: long format, one row per measured (model, benchmark) pair. The suite has {len(data["benchmarks"])} benchmarks — {n_closed} closed-loop (llama-benchy) and {n_open} open-loop (vllm bench serve) — of which {len(covered)} carry per-model figures here.

### Quality columns

Quality is reported on three dimensions, each with the benchmark the number came
from: `knowledge` / `knowledge_bench`, `science` / `science_bench`, `coding` /
`coding_bench`. The underlying benchmark differs per model — knowledge is
MMLU-Pro for most models but plain MMLU for some, and coding ranges from
LiveCodeBench to HumanEval+ — so always read the value together with its
`_bench` column. Figures come from vendor model cards, not from own testing.
`quality_avg` is the mean across the three dimensions.

```python
from datasets import load_dataset

models = load_dataset("Djangodevreng/dgx-spark-benchmarks", "models")
results = load_dataset("Djangodevreng/dgx-spark-benchmarks", "results")
```

## Method

Closed-loop benchmarks run three times per measurement point and are reported as
the mean; open-loop benchmarks run once with a fixed seed (42). Run-to-run
variance stays within about 2%. No latency gate: slow models stay visible. Full
methodology and the raw stdout per run live in this repo.

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
