# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-07 03:17:30
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                        |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:-----------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| ministral-3-8b-instruct-bf16 |  pp8192 (c5) | 6351.10 ± 78.50 | 2678.49 ± 1489.14 |               |                  |  3665.21 ± 1624.16 |  3605.31 ± 1624.16 |  3665.21 ± 1624.16 |
| ministral-3-8b-instruct-bf16 |   tg512 (c5) |    85.87 ± 1.12 |      18.90 ± 1.13 | 106.00 ± 1.41 |     21.47 ± 0.50 |                    |                    |                    |
| ministral-3-8b-instruct-bf16 | pp8192 (c10) | 6877.56 ± 21.23 | 1768.21 ± 1389.22 |               |                  |  6334.70 ± 3128.26 |  6274.80 ± 3128.26 |  6334.70 ± 3128.26 |
| ministral-3-8b-instruct-bf16 |  tg512 (c10) |   124.14 ± 1.82 |      14.74 ± 1.42 | 175.33 ± 3.77 |     18.30 ± 0.69 |                    |                    |                    |
| ministral-3-8b-instruct-bf16 | pp8192 (c20) |  7079.49 ± 5.87 | 1102.48 ± 1146.34 |               |                  | 11394.35 ± 5908.26 | 11334.46 ± 5908.26 | 11394.35 ± 5908.26 |
| ministral-3-8b-instruct-bf16 |  tg512 (c20) |   161.09 ± 3.27 |       9.86 ± 1.60 | 249.00 ± 8.29 |     13.93 ± 2.29 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-07 03:08:26 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
