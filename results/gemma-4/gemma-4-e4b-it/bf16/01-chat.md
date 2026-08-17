# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-17 03:15:41
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |    est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|----------------:|-----------------:|
| gemma-4-e4b-it-bf16 |  pp1024 (c1) | 2871.46 ± 1080.63 | 2871.46 ± 1080.63 |               |                  |  539.87 ± 201.49 | 401.56 ± 201.49 |  539.87 ± 201.49 |
| gemma-4-e4b-it-bf16 |  tg1024 (c1) |      19.56 ± 0.03 |      19.56 ± 0.03 |  20.00 ± 0.00 |     20.00 ± 0.00 |                  |                 |                  |
| gemma-4-e4b-it-bf16 |  pp1024 (c5) |  5275.30 ± 169.49 | 2893.53 ± 2594.31 |               |                  |  650.08 ± 222.71 | 511.77 ± 222.71 |  650.08 ± 222.71 |
| gemma-4-e4b-it-bf16 |  tg1024 (c5) |      65.79 ± 6.74 |      21.46 ± 2.64 | 111.33 ± 5.19 |     23.13 ± 2.47 |                  |                 |                  |
| gemma-4-e4b-it-bf16 | pp1024 (c10) |  6766.94 ± 213.50 | 2291.03 ± 3635.04 |               |                  | 1051.32 ± 399.02 | 913.01 ± 399.02 | 1051.32 ± 399.02 |
| gemma-4-e4b-it-bf16 | tg1024 (c10) |    134.08 ± 24.97 |      21.47 ± 1.99 | 223.00 ± 9.20 |     22.70 ± 1.60 |                  |                 |                  |

llama-benchy (0.4.0)
date: 2026-08-17 03:07:52 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
