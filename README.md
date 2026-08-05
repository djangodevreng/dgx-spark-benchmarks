# dgx-spark-benchmarks

Ruwe benchmark-runs van LLMs op een **NVIDIA DGX Spark** (GB10, 128 GB unified memory).

Visualisaties en uitleg staan op [djangodevreng.nl/arena/](https://djangodevreng.nl/arena/). De posts erover staan op [djangodevreng.nl/blog/](https://djangodevreng.nl/blog/).

Deze repo is de bronlaag: per model en per precisie de complete suite van 9 tests, met markdown-tabellen en de ruwe stdout van de runners.

## Hardware en stack

- DGX Spark, NVIDIA GB10 (Blackwell SM12.1), 128 GB unified memory
- vLLM als OpenAI-compatible inference server (versies per run in `meta.json`)
- llama-benchy voor closed-loop tests
- `vllm bench serve` voor open-loop tests

## De 11 tests

Sinds augustus 2026 heten de tests `NN-naam` in plaats van losse letters. De
nummers dragen de uitvoervolgorde (closed-loop eerst, binnen elke helft licht
naar zwaar), de namen komen overeen met de bench-id's op
[djangodevreng.nl/arena](https://djangodevreng.nl/arena/). Runs van vóór die
wijziging gebruiken de oude letters; de mapping staat onderaan deze sectie.

Closed-loop (`llama-benchy`), vaste concurrency:

| ID                     | Vorm                        | Concurrency |
| ---------------------- | --------------------------- | ----------- |
| `01-chat`              | 1k prompt + 1k output       | c=1, 5, 10  |
| `02-rag-8k`            | 8k prompt + 512 output      | c=5, 10, 20 |
| `03-long-output`       | 256 prompt + 4096 output    | c=1, 5, 10  |
| `04-multi-turn`        | depth=4, 2k startcontext    | c=1, 5, 10  |
| `05-big-context`       | 4k → 25k context            | c=1, 5, 10  |
| `06-concurrency-stress`| 25k context                 | c=20        |

Open-loop (`vllm bench serve`), Poisson-aankomsten:

| ID                   | Workload      | Druk                                                            |
| -------------------- | ------------- | --------------------------------------------------------------- |
| `07-office-baseline` | random 4k     | 0.3 rps, burstiness 0.7, 200 prompts                            |
| `08-sharegpt`        | ShareGPT V3   | 0.3 rps, burstiness 0.7, 250 prompts                            |
| `09-reasoning`       | 1k in, 4k uit | 0.2 rps, burstiness 1.0, 50 prompts                             |
| `10-monday-peak`     | random 4k     | 1.5 rps, burstiness 1.0, 300 prompts, max 25 concurrent         |
| `11-rate-sweep`      | random 4k     | 0.3 → 1.3 rps in vijf treden, burstiness 0.7                    |

`11-rate-sweep` is anders dan de rest: hij meet niet één punt maar de curve, en
leidt daaruit de **capaciteit** af, de hoogste request rate die onder een
p95-TTFT-grens blijft (standaard 2000 ms). Resultaat staat in
`11-rate-sweep.json` en `11-rate-sweep.md`.

`06-concurrency-stress` draait alleen c=20; c=5 en c=10 op 25k context zitten al
in `05-big-context`.

### Mapping van de oude letters

| Oud | Nieuw                   |
| --- | ----------------------- |
| A   | `05-big-context`        |
| B   | `06-concurrency-stress` |
| C   | `01-chat`               |
| D   | `09-reasoning`          |
| E   | `04-multi-turn`         |
| F   | `02-rag-8k`             |
| G   | `03-long-output`        |
| H   | `07-office-baseline`    |
| I   | `08-sharegpt`           |
| J   | `10-monday-peak`        |
| -   | `11-rate-sweep` (nieuw) |

Test D (nu `09-reasoning`) is later toegevoegd dan de rest en ontbreekt op een
aantal oudere runs. Welke, staat in [INDEX.md](./INDEX.md).

## Structuur

```
results/<family>/<model>/<precisie>/
  meta.json                snapshot van profiel, serverconfig, driver, VBIOS en
                           de door de server gerapporteerde vLLM-versie
  _runner.log              tijdstempels per test, appendt per sessie
  _sanity.txt              modeloutput waarmee is aangetoond dat de run geldig is
  01-chat.md               human-readable resultaat met markdown-tabel
  01-chat.log              raw stdout/stderr van de runner
  01-telemetry.csv         stroom, temperatuur, SM-klok en geheugen, per 10 s
  07-office-baseline.json  raw JSON (alleen open-loop)
  11-rate-sweep-0.3.json   ruwe cijfers per trede van de sweep
  11-rate-sweep.json       samenvatting met het afgeleide capaciteitscijfer
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
