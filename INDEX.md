# Index

Alle runs in deze repo. Per model staan de gedraaide precisies, status, vLLM-versie en datum. Volledige cijfers vind je in de bijbehorende folder.

## gemma-4

| Model               | Precisie  | Suite    | vLLM    | Datum         | Path |
| ------------------- | --------- | -------- | ------- | ------------- | ---- |
| gemma-4-26b-a4b-it  | `bf16`    | compleet | v0.20.1 | 2026-05-05/06 | [results/gemma-4/gemma-4-26b-a4b-it/bf16/](./results/gemma-4/gemma-4-26b-a4b-it/bf16/) |
| gemma-4-26b-a4b-it  | `nvfp4`   | compleet | v0.20.1 | 2026-05-05/06 | [results/gemma-4/gemma-4-26b-a4b-it/nvfp4/](./results/gemma-4/gemma-4-26b-a4b-it/nvfp4/) |
| gemma-4-31b-it      | `bf16`    | compleet | v0.20.1 | 2026-05-06    | [results/gemma-4/gemma-4-31b-it/bf16/](./results/gemma-4/gemma-4-31b-it/bf16/) |
| gemma-4-e2b-it      | `bf16`    | compleet | v0.20.1 | 2026-05-06    | [results/gemma-4/gemma-4-e2b-it/bf16/](./results/gemma-4/gemma-4-e2b-it/bf16/) |
| gemma-4-e4b-it      | `bf16`    | compleet | v0.20.1 | 2026-05-06    | [results/gemma-4/gemma-4-e4b-it/bf16/](./results/gemma-4/gemma-4-e4b-it/bf16/) |

Eerdere BF16-runs op de `gemma4-cu130` image bewaard onder de `no-prefix-cache` precisie-folder.

## nemotron-3

| Model                                       | Precisie | Suite    | vLLM    | Datum      | Path |
| ------------------------------------------- | -------- | -------- | ------- | ---------- | ---- |
| nemotron-3-nano-4b                          | `bf16`   | compleet | v0.20.0 | 2026-05-05 | [results/nemotron-3/nemotron-3-nano-4b/bf16/](./results/nemotron-3/nemotron-3-nano-4b/bf16/) |
| nemotron-3-nano-4b                          | `fp8`    | compleet | v0.20.0 | 2026-05-05 | [results/nemotron-3/nemotron-3-nano-4b/fp8/](./results/nemotron-3/nemotron-3-nano-4b/fp8/) |
| nemotron-3-nano-omni-30b-a3b-reasoning      | `bf16`   | compleet | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/bf16/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/bf16/) |
| nemotron-3-nano-omni-30b-a3b-reasoning      | `fp8`    | compleet | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/fp8/) |
| nemotron-3-nano-omni-30b-a3b-reasoning      | `nvfp4`  | compleet | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/](./results/nemotron-3/nemotron-3-nano-omni-30b-a3b-reasoning/nvfp4/) |
| nemotron-3-super-120b-a12b                  | `nvfp4`  | compleet | v0.20.0 | 2026-05    | [results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/](./results/nemotron-3/nemotron-3-super-120b-a12b/nvfp4/) |

## qwen-3.5

| Model           | Precisie | Suite    | vLLM    | Datum      | Path |
| --------------- | -------- | -------- | ------- | ---------- | ---- |
| qwen-3.5-0.8b   | `bf16`   | compleet | v0.20.0 | 2026-05    | [results/qwen-3.5/qwen-3.5-0.8b/bf16/](./results/qwen-3.5/qwen-3.5-0.8b/bf16/) |
| qwen-3.5-2b     | `bf16`   | compleet | v0.20.1 | 2026-05-07 | [results/qwen-3.5/qwen-3.5-2b/bf16/](./results/qwen-3.5/qwen-3.5-2b/bf16/) |

## qwen-3.6

| Model              | Precisie | Suite                    | vLLM    | Datum   | Path |
| ------------------ | -------- | ------------------------ | ------- | ------- | ---- |
| qwen-3.6-27b       | `fp8`    | compleet                 | v0.20.0 | 2026-05 | [results/qwen-3.6/qwen-3.6-27b/fp8/](./results/qwen-3.6/qwen-3.6-27b/fp8/) |
| qwen-3.6-27b       | `bf16`   | nog niet gedraaid        |         |         |      |
| qwen-3.6-35b-a3b   | `bf16`   | compleet                 | v0.20.0 | 2026-05 | [results/qwen-3.6/qwen-3.6-35b-a3b/bf16/](./results/qwen-3.6/qwen-3.6-35b-a3b/bf16/) |
| qwen-3.6-35b-a3b   | `fp8`    | compleet                 | v0.20.0 | 2026-05 | [results/qwen-3.6/qwen-3.6-35b-a3b/fp8/](./results/qwen-3.6/qwen-3.6-35b-a3b/fp8/) |

## Conventies

- **Family-folder** = de model-familie (`gemma-4`, `nemotron-3`, `qwen-3.5`, `qwen-3.6`).
- **Model-folder** = de specifieke variant binnen een familie (`gemma-4-26b-a4b-it`, `nemotron-3-super-120b-a12b`, etc.).
- **Precisie-folder** = `bf16`, `fp8`, `nvfp4`. Ook gebruikt: `no-prefix-cache` (BF16 op oude image).
- **Tests A–J** worden uitgelegd in [README.md](./README.md).
