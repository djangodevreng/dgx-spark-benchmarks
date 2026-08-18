# dgx-spark-benchmarks

Ruwe benchmark-runs van LLMs op een **NVIDIA DGX Spark** (GB10, 128 GB unified memory).

Visualisaties en uitleg staan op [djangodevreng.nl/arena/](https://djangodevreng.nl/arena/). De posts erover staan op [djangodevreng.nl/blog/](https://djangodevreng.nl/blog/).

Deze repo is de bronlaag: per model en per precisie de complete suite van elf tests, met markdown-tabellen, telemetrie en de ruwe stdout van de runners.

## Hardware en stack

- DGX Spark, NVIDIA GB10 (Blackwell SM12.1), 128 GB unified memory
- vLLM als OpenAI-compatible inference server (versies per run in `meta.json`)
- llama-benchy voor closed-loop tests
- `vllm bench serve` voor open-loop tests

Alle runs draaien op dezelfde opstelling en zijn onderling vergelijkbaar. Waar
een run daarvan afwijkt — een andere vLLM-versie, een andere KV-cache, een
kernel-omweg — staat dat bij de kanttekeningen in [INDEX.md](./INDEX.md).

## De elf tests

De nummers dragen de uitvoervolgorde: eerst closed-loop, dan open-loop, binnen
elke helft licht naar zwaar. De namen komen overeen met de bench-id's op
[djangodevreng.nl/arena](https://djangodevreng.nl/arena/).

Closed-loop (`llama-benchy`, drie runs per meetpunt), vaste concurrency:

| ID                      | Vorm                          | Concurrency |
| ----------------------- | ----------------------------- | ----------- |
| `01-chat`               | 1k prompt + 1k output         | c=1, 5, 10  |
| `02-rag-8k`             | 8k prompt + 512 output        | c=5, 10, 20 |
| `03-long-output`        | 256 prompt + 4096 output      | c=1, 5, 10  |
| `04-multi-turn`         | 5 beurten, 2k startcontext    | c=1, 5, 10  |
| `05-big-context`        | 4k, 8k, 16k en 25k context    | c=1, 5, 10  |
| `06-concurrency-stress` | 25k context                   | c=20        |

Open-loop (`vllm bench serve`), Poisson-aankomsten:

| ID                   | Workload      | Druk                                                    |
| -------------------- | ------------- | ------------------------------------------------------- |
| `07-office-baseline` | random 4k     | 0,3 rps, burstiness 0,7, 200 prompts                    |
| `08-sharegpt`        | ShareGPT V3   | 0,3 rps, burstiness 0,7, 250 prompts                    |
| `09-reasoning`       | 1k in, 4k uit | 0,2 rps, burstiness 1,0, 50 prompts                     |
| `10-monday-peak`     | random 4k     | 1,5 rps, burstiness 1,0, 300 prompts, max 25 gelijktijdig |
| `11-rate-sweep`      | random 4k     | 0,1 → 1,0 rps in zes treden, burstiness 0,7             |

`11-rate-sweep` is anders dan de rest: hij meet niet één punt maar de curve.
Elke trede duurt 250 seconden aan aankomsten, en uit de curve volgt de
**capaciteit** — de hoogste request rate die nog onder een p95-TTFT-grens
blijft. Er worden drie grenzen gerapporteerd: 2, 5 en 10 seconden. Haalt een
model een grens bij geen enkele trede, dan staat dat er ook zo in. De cijfers
per trede staan in `11-rate-sweep-<rate>.json`, de samenvatting in
`11-rate-sweep.json` en `11-rate-sweep.md`.

`06-concurrency-stress` draait alleen c=20; c=5 en c=10 op 25k context zitten al
in `05-big-context`.

## Correctheidscheck

Een doorvoerbenchmark ziet een kapot model niet: een model dat alleen `!`
produceert levert keurige tokens per seconde. Daarom genereert elke suite eerst
een kort antwoord en controleert of dat geen onzin is. Het resultaat staat in
`_sanity.txt`; bij twijfel wordt de ruwe respons bewaard in `_sanity-raw.json`.

## Structuur

```
results/<family>/<model>/<precisie>/
  meta.json                snapshot van profiel, serverconfig, driver, VBIOS en
                           de door de server gerapporteerde vLLM-versie
  _runner.log              tijdstempels per test
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

38 complete runs over 24 modellen in dertien families:

| Familie              | Modellen | Runs |
| -------------------- | -------: | ---: |
| `gemma-4`            |        4 |    8 |
| `gpt-oss`            |        1 |    1 |
| `granite-4.1`        |        1 |    1 |
| `kat-coder`          |        1 |    1 |
| `lfm2.5`             |        1 |    1 |
| `ministral-3`        |        2 |    2 |
| `mistral-small-4`    |        1 |    1 |
| `muse-glimmer`       |        1 |    2 |
| `nemotron-3`         |        4 |    9 |
| `nemotron-cascade-2` |        1 |    1 |
| `qwen-3.5`           |        4 |    4 |
| `qwen-3.6`           |        2 |    5 |
| `qwen-3.8`           |        1 |    2 |

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
