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
<model>/<precisie>/
  meta.json                snapshot van profile/server-config bij start van de run
  _runner.log              tijdsstempels per test
  A_context-scaling.md     human-readable resultaat met markdown-tabel
  A_context-scaling.log    raw stdout/stderr van de runner
  H_office-baseline.json   raw JSON resultaat (alleen voor open-loop H/I/J)
  ...
```

## Wat erin zit

- **gemma-4-26b-a4b-it**: `bf16`, `nvfp4` (complete suite, vLLM v0.20.1)
- **gemma-4-31b-it**: `bf16` (complete suite)
- **gemma-4-e2b-it**: `bf16` (complete suite)
- **gemma-4-e4b-it**: `bf16` (complete suite)
- **nemotron-3-nano-4b**: `bf16`, `fp8`
- **nemotron-3-nano-omni-30b-a3b-reasoning**: `bf16`, `fp8`, `nvfp4`
- **nemotron-3-super-120b-a12b**: `nvfp4`
- **qwen3.5-0.8b**: `bf16`
- **qwen3.6-27b**: `fp8`
- **qwen3.6-35b-a3b**: `bf16`, `fp8`

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

[MIT](./LICENSE).
