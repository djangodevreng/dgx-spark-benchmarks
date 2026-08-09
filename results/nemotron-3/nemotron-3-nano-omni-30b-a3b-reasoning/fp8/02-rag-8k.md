# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-06 03:58:06
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                        |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-nano-omni-30b-fp8 |  pp8192 (c5) |  7580.30 ± 27.68 | 2944.72 ± 1488.78 |               |                  | 3179.87 ± 1282.66 | 3099.40 ± 1282.66 | 3179.87 ± 1282.66 |
| nemotron-3-nano-omni-30b-fp8 |   tg512 (c5) |     91.65 ± 4.07 |      22.31 ± 2.76 | 125.33 ± 1.89 |     29.87 ± 3.14 |                   |                   |                   |
| nemotron-3-nano-omni-30b-fp8 | pp8192 (c10) | 8683.04 ± 176.32 | 2010.68 ± 1400.98 |               |                  | 5156.24 ± 2379.24 | 5075.77 ± 2379.24 | 5156.24 ± 2379.24 |
| nemotron-3-nano-omni-30b-fp8 |  tg512 (c10) |    117.10 ± 0.77 |      13.44 ± 0.87 | 163.33 ± 4.71 |     16.87 ± 0.92 |                   |                   |                   |
| nemotron-3-nano-omni-30b-fp8 | pp8192 (c20) | 9147.22 ± 114.42 | 1327.58 ± 1250.18 |               |                  | 8919.76 ± 4476.58 | 8839.29 ± 4476.58 | 8919.76 ± 4476.58 |
| nemotron-3-nano-omni-30b-fp8 |  tg512 (c20) |    164.44 ± 3.55 |      10.02 ± 1.00 | 266.67 ± 9.43 |     14.63 ± 1.69 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-06 03:49:31 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
