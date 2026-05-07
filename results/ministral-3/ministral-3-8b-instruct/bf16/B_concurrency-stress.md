# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-07 17:28:23
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                        |          test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------------|--------------:|-----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| ministral-3-8b-instruct-bf16 |  pp25000 (c5) | 4884.11 ± 171.11 | 2109.93 ± 1299.93 |               |                  |  14253.17 ± 6304.69 |  14139.16 ± 6304.69 |  14254.02 ± 6305.69 |
| ministral-3-8b-instruct-bf16 |    tg256 (c5) |     35.05 ± 0.37 |       9.95 ± 2.32 |  70.00 ± 0.00 |     14.80 ± 0.75 |                     |                     |                     |
| ministral-3-8b-instruct-bf16 | pp25000 (c10) |  4934.17 ± 19.60 | 1423.08 ± 1275.46 |               |                  | 25452.50 ± 13079.29 | 25338.49 ± 13079.29 | 25452.69 ± 13079.22 |
| ministral-3-8b-instruct-bf16 |   tg256 (c10) |     37.95 ± 0.15 |       6.07 ± 1.83 | 100.67 ± 0.47 |     12.40 ± 1.99 |                     |                     |                     |
| ministral-3-8b-instruct-bf16 | pp25000 (c20) |   4862.91 ± 3.40 |  879.30 ± 1071.70 |               |                  | 48568.77 ± 26699.54 | 48454.76 ± 26699.54 | 48569.05 ± 26699.70 |
| ministral-3-8b-instruct-bf16 |   tg256 (c20) |     39.37 ± 0.28 |       3.43 ± 1.23 | 133.00 ± 0.00 |      9.82 ± 2.99 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-07 17:15:59 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
