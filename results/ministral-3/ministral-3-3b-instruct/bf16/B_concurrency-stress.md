# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-07 15:29:42
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                        |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| ministral-3-3b-instruct-bf16 |  pp25000 (c5) | 8075.89 ± 20.42 | 3602.45 ± 2282.81 |               |                  |   8531.13 ± 3903.83 |   8493.24 ± 3903.83 |   8531.31 ± 3903.58 |
| ministral-3-3b-instruct-bf16 |    tg256 (c5) |    57.75 ± 0.36 |      16.62 ± 4.13 | 120.00 ± 0.00 |     25.00 ± 1.03 |                     |                     |                     |
| ministral-3-3b-instruct-bf16 | pp25000 (c10) | 8022.84 ± 18.46 | 2317.60 ± 2071.77 |               |                  |  15539.60 ± 8041.48 |  15501.71 ± 8041.48 |  15539.89 ± 8041.51 |
| ministral-3-3b-instruct-bf16 |   tg256 (c10) |    60.94 ± 0.23 |       9.61 ± 2.83 | 155.00 ± 0.00 |     18.43 ± 2.99 |                     |                     |                     |
| ministral-3-3b-instruct-bf16 | pp25000 (c20) |  7855.33 ± 8.78 | 1427.29 ± 1725.98 |               |                  | 29926.04 ± 16557.77 | 29888.15 ± 16557.77 | 29926.43 ± 16558.19 |
| ministral-3-3b-instruct-bf16 |   tg256 (c20) |    61.54 ± 0.17 |       5.15 ± 1.67 | 180.33 ± 0.47 |     14.12 ± 4.75 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-07 15:21:54 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
