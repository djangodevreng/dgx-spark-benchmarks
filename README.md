# dgx-spark-benchmarks

Ruwe benchmark-runs van LLMs op een **NVIDIA DGX Spark** (GB10, 128 GB unified memory).

Visualisaties en uitleg staan op [djangodevreng.nl/arena/](https://djangodevreng.nl/arena/). De posts erover staan op [djangodevreng.nl/blog/](https://djangodevreng.nl/blog/).

Deze repo is de bronlaag: per model en per precisie de complete suite van 9 tests, met markdown-tabellen en de ruwe stdout van de runners.

## Hardware en stack

- DGX Spark, NVIDIA GB10 (Blackwell SM12.1), 128 GB unified memory
- vLLM als OpenAI-compatible inference server (versies per run in `meta.json`)
- llama-benchy voor closed-loop tests
- `vllm bench serve` voor open-loop tests

## De 9 tests

Closed-loop (`llama-benchy`):

| ID  | Naam                | Vorm                                     | Concurrency  |
| --- | ------------------- | ---------------------------------------- | ------------ |
| A   | context-scaling     | 4k → 25k context                         | c=1, 5, 10   |
| B   | concurrency-stress  | 25k context                              | c=5, 10, 20  |
| C   | output-throughput   | 1k prompt + 1k output                    | c=1, 5, 10   |
| E   | multi-turn          | depth=4, 2k startcontext                 | c=1, 5, 10   |
| F   | rag-mix             | 8k prompt + 512 output                   | c=5, 10, 20  |
| G   | long-output         | 256 prompt + 4096 output                 | c=1, 5, 10   |

Open-loop (`vllm bench serve`):

| ID  | Naam              | Workload      | Druk                                                            |
| --- | ----------------- | ------------- | --------------------------------------------------------------- |
| H   | office-baseline   | random 4k     | Poisson 0.3 rps, burstiness 0.7, 200 prompts                    |
| I   | sharegpt-replay   | ShareGPT V3   | Poisson 0.3 rps, burstiness 0.7, 250 prompts                    |
| J   | monday-burst      | random 4k     | Poisson 1.5 rps, burstiness 1.0, 300 prompts, max 25 concurrent |

## Structuur

```
results/<family>/<model>/<precisie>/
  meta.json                snapshot van profile/server-config bij start van de run
  _runner.log              tijdsstempels per test
  A_context-scaling.md     human-readable resultaat met markdown-tabel
  A_context-scaling.log    raw stdout/stderr van de runner
  H_office-baseline.json   raw JSON resultaat (alleen voor open-loop H/I/J)
  ...
```

Volledig overzicht van alle runs in [INDEX.md](./INDEX.md).

## Wat erin zit

- `results/gemma-4/` (4 modellen, 8 precisie-runs)
- `results/ministral-3/` (2 modellen, 2 precisie-runs)
- `results/nemotron-3/` (3 modellen, 6 precisie-runs)
- `results/qwen-3.5/` (3 modellen, 3 precisie-runs)
- `results/qwen-3.6/` (2 modellen, 3 precisie-runs)

## Reproduceren

De runner-tool (`bench-spark`) is nog niet publiek. Tot dat zover is staan de exacte commands per test in de bijbehorende `meta.json` en bovenaan elke `.log`.

Heb je zelf een Spark en kom je tot andere cijfers? Open een issue, vooral interessant als de afwijking groot is.

## Hoe te citeren

```
@misc{devreng-dgx-spark-benchmarks-2026,
  author = {Django de Vreng},
  title  = {DGX Spark benchmark runs},
  year   = {2026},
  url    = {https://github.com/djangodevreng/dgx-spark-benchmarks}
}
```

## Licentie

De data in deze repo staat onder [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/): vrij te gebruiken, ook commercieel en aangepast, mits naamsvermelding (Django de Vreng, https://djangodevreng.nl). Zie [LICENSE](./LICENSE) en het citatie-blok hierboven.
