# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-03 11:24:07
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                        |          test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------------|--------------:|-----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-omni-30b-fp8 |  pp25000 (c5) | 8015.98 ± 166.25 | 3371.80 ± 2022.54 |               |                  |   8887.82 ± 3846.44 |   8790.50 ± 3846.44 |   8887.82 ± 3846.44 |
| nemotron-3-nano-omni-30b-fp8 |    tg256 (c5) |     53.12 ± 0.98 |      15.33 ± 4.17 | 109.00 ± 2.94 |     24.20 ± 3.17 |                     |                     |                     |
| nemotron-3-nano-omni-30b-fp8 | pp25000 (c10) |  8091.85 ± 70.60 | 2195.55 ± 1851.25 |               |                  |  15822.84 ± 7862.28 |  15725.52 ± 7862.28 |  15823.57 ± 7862.46 |
| nemotron-3-nano-omni-30b-fp8 |   tg256 (c10) |     58.81 ± 1.29 |       9.18 ± 2.63 | 150.00 ± 0.00 |     18.00 ± 3.30 |                     |                     |                     |
| nemotron-3-nano-omni-30b-fp8 | pp25000 (c20) |  8058.58 ± 39.01 | 1320.14 ± 1446.83 |               |                  | 29908.79 ± 15941.89 | 29811.47 ± 15941.89 | 29909.07 ± 15942.03 |
| nemotron-3-nano-omni-30b-fp8 |   tg256 (c20) |     65.51 ± 1.10 |       5.97 ± 2.30 | 233.00 ± 9.20 |     14.98 ± 4.04 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-03 11:16:33 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
