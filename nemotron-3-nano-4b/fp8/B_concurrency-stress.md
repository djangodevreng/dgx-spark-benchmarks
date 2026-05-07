# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-05 16:51:16
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                  |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-4b-fp8 |  pp25000 (c5) | 9920.74 ± 14.94 | 4342.39 ± 2634.09 |               |                  |   6961.80 ± 3134.95 |   6920.93 ± 3134.95 |   6962.08 ± 3135.01 |
| nemotron-3-nano-4b-fp8 |    tg256 (c5) |    79.25 ± 0.38 |      24.60 ± 6.49 | 178.00 ± 2.16 |     37.53 ± 1.71 |                     |                     |                     |
| nemotron-3-nano-4b-fp8 | pp25000 (c10) |  9724.64 ± 9.23 | 2715.20 ± 2265.10 |               |                  |  12845.12 ± 6561.15 |  12804.25 ± 6561.15 |  12845.46 ± 6561.13 |
| nemotron-3-nano-4b-fp8 |   tg256 (c10) |    87.44 ± 0.86 |      16.46 ± 6.27 | 288.67 ± 0.47 |     33.37 ± 3.97 |                     |                     |                     |
| nemotron-3-nano-4b-fp8 | pp25000 (c20) | 9304.13 ± 68.21 | 1634.09 ± 1824.88 |               |                  | 25110.03 ± 13911.24 | 25069.17 ± 13911.24 | 25110.41 ± 13911.42 |
| nemotron-3-nano-4b-fp8 |   tg256 (c20) |    90.97 ± 1.28 |      10.34 ± 5.42 | 400.00 ± 0.00 |     27.67 ± 6.37 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-05 16:45:45 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
