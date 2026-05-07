# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-06 12:16:14
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-e2b-it-bf16 |  pp25000 (c5) |  6927.96 ± 6.70 | 3017.10 ± 1882.75 |               |                  |  10174.24 ± 4602.89 |  10115.59 ± 4602.89 |  10174.74 ± 4603.19 |
| gemma-4-e2b-it-bf16 |    tg256 (c5) |    64.16 ± 0.21 |      22.24 ± 8.32 | 185.00 ± 0.00 |     37.00 ± 0.00 |                     |                     |                     |
| gemma-4-e2b-it-bf16 | pp25000 (c10) |  6946.46 ± 7.97 | 1916.30 ± 1647.36 |               |                  |  18359.96 ± 9223.60 |  18301.31 ± 9223.60 |  18360.47 ± 9223.36 |
| gemma-4-e2b-it-bf16 |   tg256 (c10) |    69.49 ± 0.15 |      14.72 ± 7.75 | 336.33 ± 4.50 |     34.00 ± 0.63 |                     |                     |                     |
| gemma-4-e2b-it-bf16 | pp25000 (c20) | 6857.63 ± 86.12 | 1147.38 ± 1276.71 |               |                  | 34902.81 ± 18700.76 | 34844.16 ± 18700.76 | 34903.63 ± 18700.94 |
| gemma-4-e2b-it-bf16 |   tg256 (c20) |    70.98 ± 0.73 |       8.61 ± 5.74 | 520.00 ± 0.00 |     29.15 ± 3.10 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-06 12:09:13 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
