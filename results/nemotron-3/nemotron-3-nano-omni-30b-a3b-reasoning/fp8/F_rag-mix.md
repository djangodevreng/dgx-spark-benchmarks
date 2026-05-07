# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-03 11:40:43
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                        |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-nano-omni-30b-fp8 |  pp8192 (c5) |   8826.63 ± 5.05 | 3612.86 ± 2125.27 |               |                  | 2740.85 ± 1147.94 | 2661.02 ± 1147.94 | 2740.85 ± 1147.94 |
| nemotron-3-nano-omni-30b-fp8 |   tg512 (c5) |     88.60 ± 2.98 |      21.02 ± 1.46 | 116.00 ± 0.00 |     28.87 ± 5.03 |                   |                   |                   |
| nemotron-3-nano-omni-30b-fp8 | pp8192 (c10) | 8741.57 ± 214.57 | 2255.52 ± 1892.72 |               |                  | 5107.51 ± 2518.15 | 5027.68 ± 2518.15 | 5107.51 ± 2518.15 |
| nemotron-3-nano-omni-30b-fp8 |  tg512 (c10) |    119.36 ± 2.15 |      14.37 ± 1.82 | 168.67 ± 0.94 |     19.07 ± 2.24 |                   |                   |                   |
| nemotron-3-nano-omni-30b-fp8 | pp8192 (c20) |  8938.71 ± 35.62 | 1423.81 ± 1587.49 |               |                  | 9158.41 ± 4752.45 | 9078.58 ± 4752.45 | 9158.41 ± 4752.45 |
| nemotron-3-nano-omni-30b-fp8 |  tg512 (c20) |    158.53 ± 4.12 |       9.82 ± 1.17 | 253.33 ± 9.43 |     14.25 ± 1.51 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-03 11:34:19 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
