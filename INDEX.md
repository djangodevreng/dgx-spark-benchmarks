# Index

Alle runs in deze repo. Per model staan de gedraaide precisies, status, vLLM-versie en datum. Volledige cijfers vind je in de bijbehorende folder.

## Twee generaties

De runs hieronder komen uit twee verschillende meetopstellingen. Vergelijk alleen binnen een generatie.

| | Suite v1 (t/m juli 2026) | Suite v2 (vanaf augustus 2026) |
| --- | --- | --- |
| Tests | 10, met losse letters `A` t/m `J` | 11, met `01-chat` t/m `11-rate-sweep` |
| vLLM | v0.20.0, v0.20.1, v0.23.0 en een niet-gepinde nightly | v0.26.0, behalve `muse-glimmer` (zie kanttekeningen) |
| llama-benchy | 0.3.7 en 0.3.8 door elkaar | 0.4.0 overal |
| Driver / VBIOS | 580.159.03 / 9A.0B.25.00.00 | 580.173.02 / 9A.0B.2D.00.00 |
| Telemetrie | geen | stroom, temperatuur, SM-klok per 10 s |
| Correctheidscheck | geen | modeloutput gecontroleerd vóór elke suite |

llama-benchy 0.3.8 voegde een warmup-fase toe. Binnen suite v1 zijn runs op 0.3.7 en 0.3.8 daardoor niet volledig vergelijkbaar op het eerste meetpunt.

De `meta.json` van elke run vermeldt welke versies er daadwerkelijk zijn gebruikt, inclusief de door de server gerapporteerde vLLM-versie. Dat laatste omdat een image-tag geen identificatie is: `cu130-nightly` bleek achteraf `v0.19.2rc1.dev134+gfe9c3d6c5`.

## Suite v2

Elf genummerde tests, alles op vLLM v0.26.0 en llama-benchy 0.4.0, met
telemetrie per test en een correctheidscheck op de modeloutput vóór elke
suite. Deze runs zijn onderling vergelijkbaar; met suite v1 hieronder niet.

### gemma-4

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| gemma-4-26b-a4b-it | `bf16` | 11/11 | `fp8` | 2026-08-16 | [results/gemma-4/gemma-4-26b-a4b-it/bf16/](./results/gemma-4/gemma-4-26b-a4b-it/bf16/) |
| gemma-4-26b-a4b-it | `nvfp4` | 11/11 | `fp8` | 2026-08-16 | [results/gemma-4/gemma-4-26b-a4b-it/nvfp4/](./results/gemma-4/gemma-4-26b-a4b-it/nvfp4/) |
| gemma-4-26b-a4b-it | `bf16-v23` | 11/11 | `fp8` | 2026-08-06 | [results/gemma-4/gemma-4-26b-a4b-it/bf16-v23/](./results/gemma-4/gemma-4-26b-a4b-it/bf16-v23/) |
| gemma-4-26b-a4b-it | `nvfp4-v23` | 11/11 | `fp8` | 2026-08-06 | [results/gemma-4/gemma-4-26b-a4b-it/nvfp4-v23/](./results/gemma-4/gemma-4-26b-a4b-it/nvfp4-v23/) |
| gemma-4-31b-it | `bf16` | 11/11 | `fp8` | 2026-08-06 | [results/gemma-4/gemma-4-31b-it/bf16/](./results/gemma-4/gemma-4-31b-it/bf16/) |
| gemma-4-31b-it | `nvfp4` | 11/11 | `fp8` | 2026-08-17 | [results/gemma-4/gemma-4-31b-it/nvfp4/](./results/gemma-4/gemma-4-31b-it/nvfp4/) |
| gemma-4-e2b-it | `bf16` | 11/11 | `fp8` | 2026-08-17 | [results/gemma-4/gemma-4-e2b-it/bf16/](./results/gemma-4/gemma-4-e2b-it/bf16/) |
| gemma-4-e4b-it | `bf16` | 11/11 | `fp8` | 2026-08-17 | [results/gemma-4/gemma-4-e4b-it/bf16/](./results/gemma-4/gemma-4-e4b-it/bf16/) |

### gpt-oss

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| gpt-oss-20b | `mxfp4` | 11/11 | `fp8` | 2026-08-14 | [results/gpt-oss/gpt-oss-20b/mxfp4/](./results/gpt-oss/gpt-oss-20b/mxfp4/) |

### granite-4.1

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| granite-4.1-8b | `bf16` | 11/11 | `fp8` | 2026-08-09 | [results/granite-4.1/granite-4.1-8b/bf16/](./results/granite-4.1/granite-4.1-8b/bf16/) |

### kat-coder

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| kat-coder-v2.5 | `bf16` | 11/11 | `fp8` | 2026-08-13 | [results/kat-coder/kat-coder-v2.5/bf16/](./results/kat-coder/kat-coder-v2.5/bf16/) |

### lfm2.5

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| lfm2.5-2.6b | `bf16` | 11/11 | `fp8` | 2026-08-08 | [results/lfm2.5/lfm2.5-2.6b/bf16/](./results/lfm2.5/lfm2.5-2.6b/bf16/) |

### ministral-3

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| ministral-3-3b-instruct | `bf16` | 11/11 | `auto` | 2026-08-09 | [results/ministral-3/ministral-3-3b-instruct/bf16/](./results/ministral-3/ministral-3-3b-instruct/bf16/) |
| ministral-3-8b-instruct | `bf16` | 11/11 | `fp8` | 2026-08-07 | [results/ministral-3/ministral-3-8b-instruct/bf16/](./results/ministral-3/ministral-3-8b-instruct/bf16/) |

### mistral-small-4

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| mistral-small-4-119b | `nvfp4` | 11/11 | `fp8` | 2026-08-13 | [results/mistral-small-4/mistral-small-4-119b/nvfp4/](./results/mistral-small-4/mistral-small-4-119b/nvfp4/) |

### muse-glimmer

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| muse-glimmer-30b | `bf16` | 11/11 | `auto` | 2026-08-12 | [results/muse-glimmer/muse-glimmer-30b/bf16/](./results/muse-glimmer/muse-glimmer-30b/bf16/) |
| muse-glimmer-30b | `bf16-spec` | 11/11 | `auto` | 2026-08-12 | [results/muse-glimmer/muse-glimmer-30b/bf16-spec/](./results/muse-glimmer/muse-glimmer-30b/bf16-spec/) |

### nemotron-3

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| nemotron-3-nano-30b-a3b | `bf16` | 11/11 | `fp8` | 2026-08-09 | [results/nemotron-3/nemotron-3-nano-30b-a3b/bf16/](./results/nemotron-3/nemotron-3-nano-30b-a3b/bf16/) |
| nemotron-3-nano-30b-a3b | `fp8` | 11/11 | `fp8` | 2026-08-08 | [results/nemotron-3/nemotron-3-nano-30b-a3b/fp8/](./results/nemotron-3/nemotron-3-nano-30b-a3b/fp8/) |
| nemotron-3-nano-30b-a3b | `nvfp4` | 11/11 | `fp8` | 2026-08-13 | [results/nemotron-3/nemotron-3-nano-30b-a3b/nvfp4/](./results/nemotron-3/nemotron-3-nano-30b-a3b/nvfp4/) |
| nemotron-3-nano-4b | `bf16` | 11/11 | `fp8` | 2026-08-06 | [results/nemotron-3/nemotron-3-nano-4b/bf16/](./results/nemotron-3/nemotron-3-nano-4b/bf16/) |
| nemotron-3-nano-4b | `fp8` | 11/11 | `fp8` | 2026-08-08 | [results/nemotron-3/nemotron-3-nano-4b/fp8/](./results/nemotron-3/nemotron-3-nano-4b/fp8/) |
| nemotron-3-nano-omni-30b-a3b-reasoning | `bf16` | 11/11 | `auto` | 2026-08-05 | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/bf16/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/bf16/) |
| nemotron-3-nano-omni-30b-a3b-reasoning | `fp8` | 11/11 | `fp8` | 2026-08-06 | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/) |
| nemotron-3-nano-omni-30b-a3b-reasoning | `nvfp4` | 11/11 | `auto` | 2026-08-07 | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/) |
| nemotron-3-super-120b-a12b | `nvfp4` | 11/11 | `fp8` | 2026-08-15 | [results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/](./results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/) |

### nemotron-cascade-2

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| nemotron-cascade-2-30b-a3b | `bf16` | 11/11 | `fp8` | 2026-08-13 | [results/nemotron-cascade-2/nemotron-cascade-2-30b-a3b/bf16/](./results/nemotron-cascade-2/nemotron-cascade-2-30b-a3b/bf16/) |

### qwen-3.5

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| qwen-3.5-0.8b | `bf16` | 11/11 | `fp8` | 2026-08-07 | [results/qwen-3.5/qwen-3.5-0.8b/bf16/](./results/qwen-3.5/qwen-3.5-0.8b/bf16/) |
| qwen-3.5-2b | `bf16` | 11/11 | `fp8` | 2026-08-07 | [results/qwen-3.5/qwen-3.5-2b/bf16/](./results/qwen-3.5/qwen-3.5-2b/bf16/) |
| qwen-3.5-4b | `bf16` | 11/11 | `fp8` | 2026-08-07 | [results/qwen-3.5/qwen-3.5-4b/bf16/](./results/qwen-3.5/qwen-3.5-4b/bf16/) |
| qwen-3.5-9b | `bf16` | 11/11 | `fp8` | 2026-08-07 | [results/qwen-3.5/qwen-3.5-9b/bf16/](./results/qwen-3.5/qwen-3.5-9b/bf16/) |

### qwen-3.6

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| qwen-3.6-27b | `bf16` | 11/11 | `fp8` | 2026-08-13 | [results/qwen-3.6/qwen-3.6-27b/bf16/](./results/qwen-3.6/qwen-3.6-27b/bf16/) |
| qwen-3.6-27b | `fp8` | 11/11 | `fp8` | 2026-08-14 | [results/qwen-3.6/qwen-3.6-27b/fp8/](./results/qwen-3.6/qwen-3.6-27b/fp8/) |
| qwen-3.6-35b-a3b | `bf16` | 11/11 | `fp8` | 2026-08-08 | [results/qwen-3.6/qwen-3.6-35b-a3b/bf16/](./results/qwen-3.6/qwen-3.6-35b-a3b/bf16/) |
| qwen-3.6-35b-a3b | `fp8` | 11/11 | `fp8` | 2026-08-14 | [results/qwen-3.6/qwen-3.6-35b-a3b/fp8/](./results/qwen-3.6/qwen-3.6-35b-a3b/fp8/) |
| qwen-3.6-35b-a3b | `nvfp4` | 11/11 | `fp8` | 2026-08-14 | [results/qwen-3.6/qwen-3.6-35b-a3b/nvfp4/](./results/qwen-3.6/qwen-3.6-35b-a3b/nvfp4/) |

### qwen-3.8

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| qwen-3.8-27b | `bf16` | 11/11 | `fp8` | 2026-08-15 | [results/qwen-3.8/qwen-3.8-27b/bf16/](./results/qwen-3.8/qwen-3.8-27b/bf16/) |
| qwen-3.8-27b | `fp8` | 11/11 | `fp8` | 2026-08-15 | [results/qwen-3.8/qwen-3.8-27b/fp8/](./results/qwen-3.8/qwen-3.8-27b/fp8/) |

### Kanttekeningen bij deze generatie

**Zes configs draaien met een marlin-omweg om SM121-kernelgaten.** De GB10 is
compute capability 12.1, en niet elke gekwantiseerde kernel bestaat daarvoor.
Zonder deze vlaggen weigerde de engine te starten:

| Config | Foutmelding zonder omweg | Toegevoegd |
| --- | --- | --- |
| `qwen-3.6-27b/fp8` | `cutlass_gemm_caller ... Error Internal` | `--linear-backend marlin` |
| `qwen-3.6-35b-a3b/fp8` | idem | `--linear-backend marlin` |
| `qwen-3.6-35b-a3b/nvfp4` | — | `--moe-backend marlin --linear-backend marlin`, `VLLM_USE_FLASHINFER_MOE_FP4=0` |
| `nemotron-3-super-120b-a12b/nvfp4` | `Failed to find a kernel ... ScaledMM` | `VLLM_TEST_FORCE_FP8_MARLIN=1` |
| `gemma-4-26b-a4b-it/nvfp4` | niet getest — vlaggen stonden al in het profiel | `--moe-backend marlin --linear-backend marlin`, `VLLM_USE_FLASHINFER_MOE_FP4=0` |
| `gemma-4-31b-it/nvfp4` | idem | `--quantization modelopt --moe-backend marlin --linear-backend marlin`, `VLLM_USE_FLASHINFER_MOE_FP4=0` |

De cijfers zijn eerlijk gemeten, maar ze zijn gehaald op Marlin-kernels waar
CUTLASS of FlashInfer sneller zou kunnen zijn. Op hardware met wél die kernels
liggen deze getallen vermoedelijk hoger. Alles staat per run in `meta.json`.

**`qwen-3.8-27b` is gemeten op 131072 context, niet op zijn native 262144.**
Dat is de suite-brede `MAX_MODEL_LEN`, gekozen voor vergelijkbaarheid met de rest
van de arena. Het model kan dus meer dan hier te zien is.

**`muse-glimmer` draait niet op v0.26.0 maar op een nightly.** De architectuur
`muse_glimmer` zit niet in een uitgebrachte vLLM: v0.26.0 kent hem niet en in v0.27.1
ontbreken de modelbestanden nog steeds. Meta en vLLM leverden bij de launch een aparte
image `vllm/vllm-openai:muse-glimmer`, die zich meldt als `0.26.1rc1.dev608+g99a10304d`.
De twee runs zijn onderling schoon vergelijkbaar — zelfde image, zelfde serverconfig, alleen
de drafter verschilt — maar tegenover de rest van suite v2 draagt de vergelijking een
versieverschil. De exacte versie staat per run in `meta.json`.

**`muse-glimmer` gebruikt `kv_cache_dtype=auto`, niet `fp8`.** Bewust: het model wordt in
bf16 gemeten met en zonder speculative decoding, en een gekwantiseerde KV-cache zou daar
een tweede variabele bovenop leggen. Het capaciteitscijfer ligt daardoor niet een-op-een
naast modellen die wel op `fp8` draaien.

**`muse-glimmer-30b/bf16-spec` meet de DFlash-drafter bij Meta's eigen sampling**
(temperature 1,0, top_p 0,95, top_k 64 via `--generation-config auto`). De acceptatiegraad
van de drafter hangt sterk aan die sampling en lag tijdens de run tussen 5% en 17%. Bij
greedy decoding zou dat getal fors hoger uitvallen; de gemeten winst is dus geen bovengrens.

**Het Omni-trio is onderling niet vergelijkbaar.** `nemotron-3-nano-omni-30b-a3b-reasoning`
draaide in bf16 en nvfp4 met `kv_cache_dtype=auto` en in fp8 met `fp8`. Bij de eerste twee
meet je dus alleen de gewichtsprecisie, bij de derde ook een andere KV-cache. De losse
cijfers kloppen; de vergelijking tussen die drie niet. Het text-only trio
`nemotron-3-nano-30b-a3b` is wél schoon opgezet.

**`ministral-3-3b-instruct` draait bewust met `kv_cache_dtype=auto`.** Op fp8 produceert
dat model uitsluitend hekjes tot de tokenlimiet, live getoetst op 8 augustus 2026. Dat is
een eigenschap van het model, geen fout in de opzet, maar het betekent wel dat zijn
capaciteitscijfer niet een-op-een naast de rest ligt: de KV-cache bepaalt hoeveel
aanvragen er tegelijk in passen.

**De mapnamen `bf16-v23` en `nvfp4-v23` slaan op vLLM v0.23.0**, waarop die vergelijking
oorspronkelijk is opgezet. De v2-runs in die mappen draaien gewoon op v0.26.0.

**`gemma-4-26b-a4b-it` staat er twee keer in, en dat is geen duplicaat.** Zelfde model,
zelfde image, één verschil: `bf16`/`nvfp4` draaien op `gpu-memory-utilization` 0,90 —
de suite-brede standaard — en `bf16-v23`/`nvfp4-v23` op 0,85. Vergelijk dit model dus
met de rest van de arena via `bf16`/`nvfp4`, en onderling binnen één van de twee paren.

**`gemma-4-26b-a4b-it/mtp` ontbreekt: die kán niet op v0.26.0.** De MTP-drafter
`google/gemma-4-26B-A4B-it-assistant` valt om tijdens engine-init met
`a and b must have same reduction dim, but got [s47, 3840] X [5632, 1024]`. Dat is een
fout in vLLM zelf, niet in de opzet: `Gemma4MTPModel.forward()` doet
`cat([inputs_embeds, hidden_states])` met de eigen embedding van de drafter (1024) waar
`pre_projection` twee backbone-vectoren verwacht (2 × 2816 = 5632). Het checkpoint
bevestigt die maten — `model.embed_tokens` is `[262144, 1024]`, `pre_projection` is
`[1024, 5632]` — dus de embedding van het *doelmodel* (2816) had erin moeten gaan. Het
gaat alleen goed als `backbone_hidden_size == hidden_size`, en juist bij deze drafter
verschillen ze. `num_speculative_tokens` maakt geen verschil; op 1 én op 4 dezelfde fout.
De v1-meting in `mtp-v23` blijft daarom voorlopig de enige MTP-data voor dit model.

**Waar v1 en v2 in dezelfde map staan** houden de bestandsnamen ze uit elkaar: letters
`A`–`J` voor v1, cijfers `01`–`11` voor v2. De serverconfig van elke generatie staat in
`meta-v1.json` en `meta.json`. Het `_runner.log` bevat beide, op tijdstempel.
## Suite v1

## gemma-4

| Model               | Precisie  | Suite    | vLLM    | Datum         | Path |
| ------------------- | --------- | -------- | ------- | ------------- | ---- |
| gemma-4-26b-a4b-it  | `bf16`    | compleet | v0.20.1 | 2026-05-05/06 | [results/gemma-4/gemma-4-26b-a4b-it/bf16/](./results/gemma-4/gemma-4-26b-a4b-it/bf16/) · benchy 0.3.7 |
| gemma-4-26b-a4b-it  | `nvfp4`   | compleet | v0.20.1 | 2026-05-05/06 | [results/gemma-4/gemma-4-26b-a4b-it/nvfp4/](./results/gemma-4/gemma-4-26b-a4b-it/nvfp4/) · benchy 0.3.7 |
| gemma-4-26b-a4b-it  | `bf16-v23`  | A–J behalve D | v0.23.0 | 2026-06-22/23 | [results/gemma-4/gemma-4-26b-a4b-it/bf16-v23/](./results/gemma-4/gemma-4-26b-a4b-it/bf16-v23/) · benchy 0.3.8 |
| gemma-4-26b-a4b-it  | `nvfp4-v23` | A–J behalve D | v0.23.0 | 2026-06-22/23 | [results/gemma-4/gemma-4-26b-a4b-it/nvfp4-v23/](./results/gemma-4/gemma-4-26b-a4b-it/nvfp4-v23/) · benchy 0.3.8 |
| gemma-4-26b-a4b-it  | `mtp-v23`   | A–J behalve D | v0.23.0 | 2026-06-22/23 | [results/gemma-4/gemma-4-26b-a4b-it/mtp-v23/](./results/gemma-4/gemma-4-26b-a4b-it/mtp-v23/) · benchy 0.3.8 |
| gemma-4-31b-it      | `bf16`    | compleet | v0.20.1 | 2026-05-06    | [results/gemma-4/gemma-4-31b-it/bf16/](./results/gemma-4/gemma-4-31b-it/bf16/) · benchy 0.3.7 |
| gemma-4-31b-it      | `nvfp4`   | compleet | v0.20.1 | 2026-05-08    | [results/gemma-4/gemma-4-31b-it/nvfp4/](./results/gemma-4/gemma-4-31b-it/nvfp4/) · benchy 0.3.7 |
| gemma-4-e2b-it      | `bf16`    | compleet | v0.20.1 | 2026-05-06    | [results/gemma-4/gemma-4-e2b-it/bf16/](./results/gemma-4/gemma-4-e2b-it/bf16/) · benchy 0.3.7 |
| gemma-4-e4b-it      | `bf16`    | compleet | v0.20.1 | 2026-05-06    | [results/gemma-4/gemma-4-e4b-it/bf16/](./results/gemma-4/gemma-4-e4b-it/bf16/) · benchy 0.3.7 |

Eerdere BF16-runs op de `gemma4-cu130` image bewaard onder de `no-prefix-cache` precisie-folder.

De `-v23` precisies zijn een 3-weg her-run op vLLM **v0.23.0** (stable): `bf16-v23` vs `nvfp4-v23` (nvidia NVFP4, modelopt+marlin) vs `mtp-v23` (bf16 + speculative decoding, assistant-drafter γ=4). Identieke config (gpu-util 0.85, kv fp8, prefix-cache uit) op de variabele-onder-test na.

## nemotron-3

| Model                                       | Precisie | Suite    | vLLM    | Datum      | Path |
| ------------------------------------------- | -------- | -------- | ------- | ---------- | ---- |
| nemotron-3-nano-4b                          | `bf16`   | compleet | v0.20.0 | 2026-05-05 | [results/nemotron-3/nemotron-3-nano-4b/bf16/](./results/nemotron-3/nemotron-3-nano-4b/bf16/) · benchy 0.3.7 |
| nemotron-3-nano-4b                          | `fp8`    | compleet | v0.20.0 | 2026-05-05 | [results/nemotron-3/nemotron-3-nano-4b/fp8/](./results/nemotron-3/nemotron-3-nano-4b/fp8/) · benchy 0.3.7 |
| nemotron-3-nano-omni-30b-a3b-reasoning      | `bf16`   | A–J behalve D | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/bf16/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/bf16/) · benchy 0.3.7 |
| nemotron-3-nano-omni-30b-a3b-reasoning      | `fp8`    | A–J behalve D | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/) · benchy 0.3.7 |
| nemotron-3-nano-omni-30b-a3b-reasoning      | `nvfp4`  | A–J behalve D | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/) · benchy 0.3.7 |
| nemotron-3-super-120b-a12b                  | `nvfp4`  | compleet | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/](./results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/) · benchy 0.3.7 |

## ministral-3

| Model                       | Precisie | Suite    | vLLM    | Datum      | Path |
| --------------------------- | -------- | -------- | ------- | ---------- | ---- |
| ministral-3-3b-instruct     | `bf16`   | compleet | v0.20.1 | 2026-05-07 | [results/ministral-3/ministral-3-3b-instruct/bf16/](./results/ministral-3/ministral-3-3b-instruct/bf16/) · benchy 0.3.7 |
| ministral-3-8b-instruct     | `bf16`   | compleet | v0.20.1 | 2026-05-07 | [results/ministral-3/ministral-3-8b-instruct/bf16/](./results/ministral-3/ministral-3-8b-instruct/bf16/) · benchy 0.3.7 |

## mistral-small

| Model                       | Precisie | Suite    | vLLM    | Datum      | Path |
| --------------------------- | -------- | -------- | ------- | ---------- | ---- |
| mistral-small-3.2-24b-it    | `nvfp4`  | A–J behalve D | v0.23.0 | 2026-06-23 | [results/mistral-small/mistral-small-3.2-24b-it/nvfp4/](./results/mistral-small/mistral-small-3.2-24b-it/nvfp4/) · benchy 0.3.8 |

Dense 24B (géén MoE, dus 24B actief — fors trager dan de MoE-modellen). NVFP4-build van RedHatAI. Vereiste op SM121 (GB10) drie env-vars om Marlin te forceren i.p.v. de kapotte CUTLASS-FP4-kernel: `VLLM_USE_FLASHINFER_MOE_FP4=0`, `VLLM_NVFP4_GEMM_BACKEND=marlin`, `VLLM_TEST_FORCE_FP8_MARLIN=1`. Config: gpu-util 0.70, kv fp8, prefix-cache uit, async-scheduling aan.

## qwen-3.5

| Model           | Precisie | Suite                            | vLLM    | Datum      | Path |
| --------------- | -------- | -------------------------------- | ------- | ---------- | ---- |
| qwen-3.5-0.8b   | `bf16`   | compleet                         | v0.20.0 | 2026-05    | [results/qwen-3.5/qwen-3.5-0.8b/bf16/](./results/qwen-3.5/qwen-3.5-0.8b/bf16/) · benchy 0.3.7 |
| qwen-3.5-2b     | `bf16`   | compleet                         | v0.20.1 | 2026-05-07 | [results/qwen-3.5/qwen-3.5-2b/bf16/](./results/qwen-3.5/qwen-3.5-2b/bf16/) · benchy 0.3.7 |
| qwen-3.5-4b     | `bf16`   | compleet                         | v0.20.1 | 2026-05-07 | [results/qwen-3.5/qwen-3.5-4b/bf16/](./results/qwen-3.5/qwen-3.5-4b/bf16/) · benchy 0.3.7 |
| qwen-3.5-9b     | `bf16`   | compleet                         | v0.20.1 | 2026-05-09 | [results/qwen-3.5/qwen-3.5-9b/bf16/](./results/qwen-3.5/qwen-3.5-9b/bf16/) · benchy 0.3.7 |

## qwen-3.6

| Model              | Precisie | Suite                    | vLLM           | Datum      | Path |
| ------------------ | -------- | ------------------------ | -------------- | ---------- | ---- |
| qwen-3.6-27b       | `fp8`    | A–J behalve D            | v0.20.0        | 2026-05    | [results/qwen-3.6/qwen-3.6-27b/fp8/](./results/qwen-3.6/qwen-3.6-27b/fp8/) · benchy 0.3.7 |
| qwen-3.6-27b       | `bf16`   | compleet                 | cu130-nightly  | 2026-05-09 | [results/qwen-3.6/qwen-3.6-27b/bf16/](./results/qwen-3.6/qwen-3.6-27b/bf16/) · benchy 0.3.7 |
| qwen-3.6-35b-a3b   | `bf16`   | compleet                 | cu130-nightly  | 2026-05    | [results/qwen-3.6/qwen-3.6-35b-a3b/bf16/](./results/qwen-3.6/qwen-3.6-35b-a3b/bf16/) · benchy 0.3.7 |
| qwen-3.6-35b-a3b   | `fp8`    | A–J behalve D            | cu130-nightly  | 2026-05    | [results/qwen-3.6/qwen-3.6-35b-a3b/fp8/](./results/qwen-3.6/qwen-3.6-35b-a3b/fp8/) · benchy 0.3.7 |
| qwen-3.6-35b-a3b   | `nvfp4`  | compleet                 | cu130-nightly  | 2026-06-26 | [results/qwen-3.6/qwen-3.6-35b-a3b/nvfp4/](./results/qwen-3.6/qwen-3.6-35b-a3b/nvfp4/) · benchy 0.3.8 |

De qwen-3.6-runs draaiden op de tag `cu130-nightly`, die niet gepind is. De bootlog van de 35B-A3B BF16-run identificeert die build als `v0.19.2rc1.dev134+gfe9c3d6c5`. Die runs zijn dus niet reproduceerbaar zonder een herrun op een gepinde versie. Let ook op de `kv_cache_dtype`: `auto` bij BF16 en NVFP4, `fp8_e4m3` bij FP8, dus die drie zijn geen zuivere precisievergelijking.

## gpt-oss

| Model        | Precisie | Suite    | vLLM    | Datum      | Path |
| ------------ | -------- | -------- | ------- | ---------- | ---- |
| gpt-oss-20b  | `mxfp4`  | compleet | v0.23.0 | 2026-06-26 | [results/gpt-oss/gpt-oss-20b/mxfp4/](./results/gpt-oss/gpt-oss-20b/mxfp4/) · benchy 0.3.8 |

MoE met native MXFP4-gewichten, Apache 2.0. Config: gpu-util 0.90, kv fp8, prefix-cache uit, async-scheduling aan. De 120B-variant uit dezelfde familie is nog niet gedraaid.

## Conventies

- **Family-folder** = de model-familie (`gemma-4`, `gpt-oss`, `ministral-3`, `mistral-small`, `nemotron-3`, `qwen-3.5`, `qwen-3.6`).
- **Model-folder** = de specifieke variant binnen een familie (`gemma-4-26b-a4b-it`, `nemotron-3-super-120b-a12b`, etc.).
- **Precisie-folder** = `bf16`, `fp8`, `nvfp4`. Ook gebruikt: `no-prefix-cache` (BF16 op oude image).
- **Tests A–J** worden uitgelegd in [README.md](./README.md).
