# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-17 05:55:44
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |        t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-------------------:|------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-e2b-it-bf16 |   pp256 (c1) |   4047.14 ± 533.28 |  4047.14 ± 533.28 |               |                  |  109.05 ± 6.32 |   57.96 ± 6.32 |   109.05 ± 6.32 |
| gemma-4-e2b-it-bf16 |  tg4096 (c1) |       39.65 ± 0.01 |      39.65 ± 0.01 |  40.00 ± 0.00 |     40.00 ± 0.00 |                |                |                 |
| gemma-4-e2b-it-bf16 |   pp256 (c5) |   9757.81 ± 378.13 |  3434.65 ± 269.84 |               |                  |  119.76 ± 3.61 |   68.67 ± 3.61 |   119.76 ± 3.61 |
| gemma-4-e2b-it-bf16 |  tg4096 (c5) |      168.56 ± 6.04 |      45.19 ± 0.26 | 230.00 ± 0.00 |     46.40 ± 0.49 |                |                |                 |
| gemma-4-e2b-it-bf16 |  pp256 (c10) | 10433.13 ± 1211.97 | 2168.69 ± 1818.53 |               |                  | 199.99 ± 54.33 | 148.90 ± 54.33 |  199.99 ± 54.33 |
| gemma-4-e2b-it-bf16 | tg4096 (c10) |     268.10 ± 15.79 |      44.52 ± 0.37 | 456.33 ± 4.50 |     46.03 ± 0.60 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-17 05:52:52 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
