# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-17 03:29:32
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-e4b-it-bf16 |   pp256 (c1) | 1379.44 ± 506.14 | 1379.44 ± 506.14 |               |                  | 258.85 ± 55.79 | 187.40 ± 55.79 |  258.85 ± 55.79 |
| gemma-4-e4b-it-bf16 |  tg4096 (c1) |     19.62 ± 0.04 |     19.62 ± 0.04 |  20.00 ± 0.00 |     20.00 ± 0.00 |                |                |                 |
| gemma-4-e4b-it-bf16 |   pp256 (c5) |  4147.94 ± 50.03 |  1111.82 ± 49.78 |               |                  |  282.89 ± 0.71 |  211.43 ± 0.71 |   282.89 ± 0.71 |
| gemma-4-e4b-it-bf16 |  tg4096 (c5) |    66.20 ± 13.72 |     22.84 ± 0.43 | 118.00 ± 2.83 |     24.07 ± 0.24 |                |                |                 |
| gemma-4-e4b-it-bf16 |  pp256 (c10) |  5897.00 ± 48.30 |   718.05 ± 33.15 |               |                  |  403.21 ± 3.44 |  331.75 ± 3.44 |   403.21 ± 3.44 |
| gemma-4-e4b-it-bf16 | tg4096 (c10) |    125.67 ± 4.94 |     22.45 ± 0.21 | 233.33 ± 4.71 |     23.60 ± 0.49 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-17 03:23:48 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
