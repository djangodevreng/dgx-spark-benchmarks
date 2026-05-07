# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-07 15:46:15
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                        |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| ministral-3-3b-instruct-bf16 |  pp8192 (c5) | 12697.70 ± 47.18 | 5486.99 ± 3311.57 |               |                  |  1830.33 ± 809.19 |  1799.67 ± 809.19 |  1830.33 ± 809.19 |
| ministral-3-3b-instruct-bf16 |   tg512 (c5) |    159.23 ± 2.73 |      35.13 ± 1.85 | 191.67 ± 2.36 |     39.13 ± 1.20 |                   |                   |                   |
| ministral-3-3b-instruct-bf16 | pp8192 (c10) |  13022.62 ± 8.16 | 3523.66 ± 3092.15 |               |                  | 3336.28 ± 1684.14 | 3305.63 ± 1684.14 | 3336.28 ± 1684.14 |
| ministral-3-3b-instruct-bf16 |  tg512 (c10) |    219.23 ± 6.02 |      25.87 ± 2.37 | 300.00 ± 0.00 |     30.97 ± 1.43 |                   |                   |                   |
| ministral-3-3b-instruct-bf16 | pp8192 (c20) | 13013.98 ± 17.74 | 2178.07 ± 2557.72 |               |                  | 6180.13 ± 3283.92 | 6149.48 ± 3283.92 | 6180.13 ± 3283.92 |
| ministral-3-3b-instruct-bf16 |  tg512 (c20) |    271.31 ± 0.71 |      16.23 ± 1.63 | 400.00 ± 0.00 |     21.33 ± 1.61 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-07 15:42:20 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
