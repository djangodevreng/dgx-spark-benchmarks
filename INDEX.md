# Index

Alle runs in deze repo. Per model staan de gedraaide precisies, status, vLLM-versie en datum. Volledige cijfers vind je in de bijbehorende folder.

## Meetopstelling

Alle runs komen van dezelfde DGX Spark. Versie- en profielverschillen staan per
run in `meta.json` en bepalen welke vergelijkingen methodologisch geldig zijn.

| | |
| --- | --- |
| Tests | 11, van `01-chat` t/m `11-rate-sweep` |
| vLLM | v0.26.0, behalve `muse-glimmer`, `qwen-3.8-27b/nvfp4-v029`, `nemotron-3.5-super-120b-a12b/nvfp4-v031` en `qwen-3.8-flash-next/nvfp4-b12x` (zie kanttekeningen) |
| llama-benchy | 0.4.0 |
| Driver / VBIOS | 580.173.02 / 9A.0B.2D.00.00 (`nvfp4-v031` en `nvfp4-b12x`: driver 580.178.04) |
| Telemetrie | stroom, temperatuur, SM-klok per 10 s |
| Correctheidscheck | huidige runner controleert modeloutput; historische status staat in `meta.json` |

De `meta.json` van elke run vermeldt welke versies er daadwerkelijk zijn gebruikt,
inclusief de door de server gerapporteerde vLLM-versie. Dat laatste omdat een
image-tag geen identificatie is: `cu130-nightly` bleek achteraf
`v0.19.2rc1.dev134+gfe9c3d6c5`.

## Runs

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
| ministral-3-3b-instruct | `bf16` | 10 + afgebroken sweep · sanity failed | `auto` | 2026-08-09 | [results/ministral-3/ministral-3-3b-instruct/bf16/](./results/ministral-3/ministral-3-3b-instruct/bf16/) |
| ministral-3-8b-instruct | `bf16` | 10 + afgebroken sweep | `fp8` | 2026-08-07 | [results/ministral-3/ministral-3-8b-instruct/bf16/](./results/ministral-3/ministral-3-8b-instruct/bf16/) |

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
| nemotron-3-nano-omni-30b-a3b-reasoning | `fp8` | 10/11 · sweep zonder data | `fp8` | 2026-08-06 | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/) |
| nemotron-3-nano-omni-30b-a3b-reasoning | `nvfp4` | 10 + afgebroken sweep | `auto` | 2026-08-07 | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/) |
| nemotron-3-super-120b-a12b | `nvfp4` | 11/11 | `fp8` | 2026-08-15 | [results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/](./results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/) |

### nemotron-3.5

| Model | Precisie | Tests | KV-cache | Datum | Path |
| --- | --- | --- | --- | --- | --- |
| nemotron-3.5-super-120b-a12b | `nvfp4-v031` | 11/11 | `fp8` | 2026-10-18 | [results/nemotron-3.5/nemotron-3.5-super-120b-a12b/nvfp4-v031/](./results/nemotron-3.5/nemotron-3.5-super-120b-a12b/nvfp4-v031/) |

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
| qwen-3.8-27b | `nvfp4-v029` | 11/11 | `fp8` | 2026-09-21 | [results/qwen-3.8/qwen-3.8-27b/nvfp4-v029/](./results/qwen-3.8/qwen-3.8-27b/nvfp4-v029/) |
| qwen-3.8-flash-next | `nvfp4-b12x` | 11/11 | `fp8` | 2026-10-18 | [results/qwen-3.8/qwen-3.8-flash-next/nvfp4-b12x/](./results/qwen-3.8/qwen-3.8-flash-next/nvfp4-b12x/) |

## Kanttekeningen

**Zeven configs draaien met een marlin-omweg om SM121-kernelgaten.** De GB10 is
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
| `qwen-3.8-27b/nvfp4-v029` | `CUDA error: no kernel image is available for execution on the device` | `--linear-backend marlin` |

De cijfers zijn eerlijk gemeten, maar ze zijn gehaald op Marlin-kernels waar
CUTLASS of FlashInfer sneller zou kunnen zijn. Op hardware met wél die kernels
liggen deze getallen vermoedelijk hoger. Alles staat per run in `meta.json`.

**`qwen-3.8-27b/nvfp4-v029` draait op v0.29.0 en meet W4A16, niet W4A4.** Twee
dingen wijken af van de rest van de arena, allebei gedwongen.

Ten eerste de versie. Het checkpoint `nvidia/Qwen3.8-27B-NVFP4` is een ModelOpt
`MIXED_PRECISION`-model: 193 lagen NVFP4 met group_size 16 op de MLP's en de
lm_head, 208 lagen FP8 op self-attention en linear-attention. Dat vraagt vLLM's
`ModelOptMixedPrecisionConfig`, die in v0.26.0 nog niet bestaat. Vandaar v0.29.0.
Vergelijkingen met `bf16` en `fp8` in dezelfde modelfolder dragen dus een
versieverschil naast het precisieverschil.

Ten tweede de kernel. Bij `--linear-backend auto` koos vLLM
`FlashInferCutlassNvFp4LinearKernel` en klapte de engine tijdens de profile-run op
`cudaErrorNoKernelImageForDevice`. Oorzaak: FlashInfer's CUTLASS-FP4-pad heeft geen
`@supported_compute_capability`-decorator en meldt zich dus overal als bruikbaar,
terwijl de arch-conditional cubins (`sm_100a`, `sm_120a`) geen sm_121-image bevatten.
Ter vergelijking: het cute-dsl-pad is wél afgeschermd met `[100, 103, 107]` en werd
correct overgeslagen. De crash staat in `_server-crash.log` bij de run.

De Marlin-terugval die daarop volgt is **weight-only (W4A16)**: de gewichten staan
in 4 bits, maar worden voor elke matmul uitgepakt naar bf16. De bandbreedtewinst
blijft, de rekenwinst niet. Dat is zichtbaar in de cijfers: decode haalt 2,4 tot
2,7x bf16, terwijl prefill op elke test en elke concurrency vastloopt rond 790 t/s
— tegen ~1100 t/s voor bf16. Het door NVIDIA bedoelde pad is W4A4, waarbij ook de
activaties gequantiseerd worden; dat vereist de `b12x`-bibliotheek, die SM121
expliciet ondersteunt maar niet in het vLLM-image zit. Deze run meet dus de
ondergrens van wat NVFP4 op een GB10 kan.

**`nemotron-3.5-super-120b-a12b/nvfp4-v031` wijkt op vijf punten af van de basislijn.**
Het checkpoint is `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4`, revisie
`2e5cc3953bb1ea66b2fb7c831fee3aa317427e69`.

- **vLLM v0.31.0.** Het vLLM-recept voor dit checkpoint vraagt v0.31.0 of nieuwer.
- **`gpu-memory-utilization` 0,85 in plaats van 0,90.** Op de GB10 delen CPU en GPU
  dezelfde 128 GB. Bij 0,90 bleef met dit model ongeveer 2,7 GB RAM over, en de
  open-loop client (`vllm bench serve` in de servercontainer) duwde dat tijdens
  `07-office-baseline` onder de grens van een tijdelijke geheugenwatchdog (buiten de runner),
  die de server stopte.
  Op 0,85 is de KV-pool nog 4,5M tokens, 34x de volle context van 131072, dus de
  KV-cache is in geen enkele test de beperking. Zie ook het 0,85-paar van
  `gemma-4-26b-a4b-it`.
- **Speculative decoding: MTP met 3 drafttokens.** Het model levert een eigen
  MTP-laag mee en alle Spark-recepten van NVIDIA gebruiken speculative decoding. Decode-cijfers liggen
  daardoor niet één-op-één naast modellen zonder speculative decoding, zoals
  `qwen-3.8-27b/nvfp4-v029`.
- **`--language-model-only`.** Alleen het taalmodel; de vision-encoder wordt niet geladen.
- **Voorgevulde FlashInfer-autotunecache.** De autotune draait na de KV-allocatie en
  piekt 24 tot 30 GB boven het budget, wat op 0,85 niet past. De cache is daarom eerst
  gevuld met een run op 0,63 en daarna hergebruikt. `gpu_memory_utilization` telt niet
  mee in de cachesleutel; aantal sequenties, contextlengte en spec-config wel, en die
  zijn gelijk. De kernelkeuze is dus dezelfde als bij een eigen autotune.

De Mamba-vlaggen volgen NVIDIA's Spark-recept. De vlaggen die prefix caching vereisen
(`--mamba-cache-mode align`, `--enable-mamba-shared-prefix-checkpoint`,
`--prefix-match-unit`) zijn weggelaten, omdat prefix caching suite-breed uit staat.
`_runner.log` bevat ook twee afgebroken sessies van 16 oktober (de poging op 0,90);
alle resultaatbestanden komen uit de run van 17 en 18 oktober.

**`qwen-3.8-flash-next/nvfp4-b12x` draait niet op upstream vLLM en wijkt op zes punten af van de basislijn.**
Het checkpoint is `nvidia/Qwen3.8-Flash-Next-FP4-Local`, revisie
`b9ce18a6887e18c089fdea8509a33e63429a3300`.

- **Community-image `eugr/spark-vllm-b12x`**, vastgezet op digest, met
  vLLM-ontwikkelversie `0.1.dev21830+g8244d1c44`. Upstream vLLM, ook v0.32.0, kan
  dit checkpoint nog niet laden: het lezen van de PLE-tabel vanaf de schijf en het
  gecomprimeerde schaalformaat ontbreken daar. Het image gebruikt b12x-kernels voor
  MoE, lineaire lagen en GDN-decode; de FlashInfer-autotune staat uit.
- **De n-gram/PLE-tabel (ongeveer 48 GiB) blijft op de schijf** en wordt via io_uring
  gelezen, buiten de page cache om. Docker's standaard-seccompprofiel blokkeert
  io_uring, dus de container draait met `seccomp=unconfined`.
- **`gpu-memory-utilization` 0,75 in plaats van 0,90.** Direct na het laden van de
  gewichten piekt het geheugen tijdelijk zo'n 40 GB, en de koude b12x-autotune komt
  daar bovenop. Op 0,85 en 0,80 zakte het vrije RAM daardoor onder de grens van een
  tijdelijke geheugenwatchdog (buiten de runner), die de server stopte.
- **`--max-num-seqs 32`** in plaats van de vLLM-standaard (1024 op deze GPU), omdat de
  werkruimte van de b12x-autotune met dit getal meegroeit. Meer gelijktijdige
  verzoeken wachten in de wachtrij van de server; dat drukt vooral de TTFT in de
  open-loop-tests 07 tot en met 11.
- **Speculative decoding: MTP met 3 drafttokens**, zoals in NVIDIA's Spark-recept.
  Decode-cijfers liggen daardoor niet één-op-één naast modellen zonder speculative
  decoding.
- **`--language-model-only`.** Alleen het taalmodel; de vision-encoder wordt niet geladen.

De overige vlaggen en omgevingsvariabelen volgen NVIDIA's Spark-recept en staan in
`meta.json`. Een herhaling van 07, 09 en 11 op 0,90 met `--max-num-seqs 128` en
`B12X_AUTOTUNE=0` (geen autotune en dus geen autotunepiek) laat zien dat die wachtrij
de TTFT bepaalde: in `07-office-baseline` daalde de gemiddelde TTFT van 102 naar 20 s
(p95 van 207 naar 52 s), in `09-reasoning` de p95 van 458 naar 2,5 s, en in
`11-rate-sweep` steeg de verzadigde doorvoer van 0,21 naar 0,25 req/s. De capaciteit
onder een p95-TTFT van 10 s bleef gelijk: de trede van 0,2 req/s haalde 9,95 en 10,1 s.
Die herhaling dekt 3 van de 11 tests en staat daarom niet als eigen run in deze repo.
`_runner.log` bevat ook een eerste, mislukte poging van 07 tot en met 11 (tokenizer
offline niet gevonden); alle resultaatbestanden komen uit de herhaling direct daarna.

**`qwen-3.8-27b` is gemeten op 131072 context, niet op zijn native 262144.**
Dat is de suite-brede `MAX_MODEL_LEN`, gekozen voor vergelijkbaarheid met de rest
van de arena. Het model kan dus meer dan hier te zien is.

**`muse-glimmer` draait niet op v0.26.0 maar op een nightly.** De architectuur
`muse_glimmer` zit niet in een uitgebrachte vLLM: v0.26.0 kent hem niet en in v0.27.1
ontbreken de modelbestanden nog steeds. Meta en vLLM leverden bij de launch een aparte
image `vllm/vllm-openai:muse-glimmer`, die zich meldt als `0.26.1rc1.dev608+g99a10304d`.
De twee runs zijn onderling schoon vergelijkbaar — zelfde image, zelfde serverconfig, alleen
de drafter verschilt — maar tegenover de rest van de arena draagt de vergelijking een
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

**Gebruik de huidige `ministral-3-3b-instruct`-run niet voor conclusies.** De
gepubliceerde BF16-run met `kv_cache_dtype=auto` produceerde tijdens de bewaarde
sanity-check uitsluitend hekjes tot de tokenlimiet. `validity.sanity` staat daarom
op `failed`. De cijfers blijven als audit trail aanwezig, maar horen niet in een
ranking totdat het model opnieuw geldig is gestart en gemeten.

**De mapnamen `bf16-v23` en `nvfp4-v23` slaan op vLLM v0.23.0**, waarop die vergelijking
oorspronkelijk is opgezet. De runs in die mappen draaien gewoon op v0.26.0, net als de rest.

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
Er is daarom geen MTP-meting voor dit model.

## Conventies

- **Family-folder** = de model-familie (`gemma-4`, `gpt-oss`, `granite-4.1`, `kat-coder`, `lfm2.5`, `ministral-3`, `mistral-small-4`, `muse-glimmer`, `nemotron-3`, `nemotron-3.5`, `nemotron-cascade-2`, `qwen-3.5`, `qwen-3.6`, `qwen-3.8`).
- **Model-folder** = de specifieke variant binnen een familie (`gemma-4-26b-a4b-it`, `nemotron-3-super-120b-a12b`, etc.).
- **Precisie-folder** = `bf16`, `fp8`, `nvfp4`, `mxfp4`. Varianten met een achtervoegsel meten hetzelfde model onder een afwijkende serverconfig: `bf16-spec` (speculative decoding), `bf16-v23` en `nvfp4-v23` (zie kanttekeningen), `nvfp4-v029` en `nvfp4-v031` (andere vLLM-versie), `nvfp4-b12x` (community-image met b12x-kernels); zie kanttekeningen.
- **Tests 01–11** worden uitgelegd in [README.md](./README.md).
