# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-09 00:30:35
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                        |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| ministral-3-3b-instruct-bf16 |  pp8192 (c5) |  12573.19 ± 34.05 | 5062.99 ± 2761.18 |               |                  |  1885.57 ± 780.03 |  1851.78 ± 780.03 |  1885.57 ± 780.03 |
| ministral-3-3b-instruct-bf16 |   tg512 (c5) |     126.78 ± 0.31 |      26.96 ± 1.08 | 146.67 ± 2.36 |     29.47 ± 0.50 |                   |                   |                   |
| ministral-3-3b-instruct-bf16 | pp8192 (c10) |  12475.72 ± 22.21 | 3297.15 ± 2609.53 |               |                  | 3402.81 ± 1718.05 | 3369.02 ± 1718.05 | 3402.81 ± 1718.05 |
| ministral-3-3b-instruct-bf16 |  tg512 (c10) |     157.90 ± 0.94 |      17.46 ± 1.00 | 200.00 ± 0.00 |     20.60 ± 0.84 |                   |                   |                   |
| ministral-3-3b-instruct-bf16 | pp8192 (c20) | 11909.43 ± 463.88 | 2075.07 ± 2257.06 |               |                  | 6368.18 ± 3505.18 | 6334.38 ± 3505.18 | 6368.18 ± 3505.18 |
| ministral-3-3b-instruct-bf16 |  tg512 (c20) |     179.44 ± 1.87 |      10.11 ± 0.71 | 243.00 ± 4.24 |     14.03 ± 2.08 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-09 00:23:07 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
