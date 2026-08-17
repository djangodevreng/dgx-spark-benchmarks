# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-17 05:48:20
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-e2b-it-bf16 |  pp1024 (c1) | 2542.52 ± 1007.95 | 2542.52 ± 1007.95 |               |                  | 490.48 ± 221.73 | 444.36 ± 221.73 | 490.48 ± 221.73 |
| gemma-4-e2b-it-bf16 |  tg1024 (c1) |      39.62 ± 0.07 |      39.62 ± 0.07 |  40.00 ± 0.00 |     40.00 ± 0.00 |                 |                 |                 |
| gemma-4-e2b-it-bf16 |  pp1024 (c5) |  9048.90 ± 756.39 | 3856.20 ± 2536.99 |               |                  | 366.21 ± 132.90 | 320.09 ± 132.90 | 366.21 ± 132.90 |
| gemma-4-e2b-it-bf16 |  tg1024 (c5) |     160.43 ± 9.18 |      44.41 ± 0.54 | 230.00 ± 0.00 |     46.13 ± 0.34 |                 |                 |                 |
| gemma-4-e2b-it-bf16 | pp1024 (c10) | 12509.86 ± 402.28 | 3453.92 ± 3843.85 |               |                  | 514.60 ± 226.47 | 468.48 ± 226.47 | 514.60 ± 226.47 |
| gemma-4-e2b-it-bf16 | tg1024 (c10) |    254.44 ± 13.19 |      43.34 ± 0.84 | 450.00 ± 0.00 |     45.47 ± 0.72 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-17 05:44:27 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
