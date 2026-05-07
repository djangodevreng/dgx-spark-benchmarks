# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-07 17:57:35
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                        |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:-----------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| ministral-3-8b-instruct-bf16 |  pp8192 (c5) |  7354.20 ± 3.55 | 3358.04 ± 2243.39 |               |                  |  3129.76 ± 1436.55 |  3065.66 ± 1436.55 |  3129.76 ± 1436.55 |
| ministral-3-8b-instruct-bf16 |   tg512 (c5) |    81.92 ± 2.90 |      18.15 ± 0.89 | 100.00 ± 0.00 |     20.00 ± 0.00 |                    |                    |                    |
| ministral-3-8b-instruct-bf16 | pp8192 (c10) | 7291.02 ± 38.00 | 2116.44 ± 2014.09 |               |                  |  5918.50 ± 3067.89 |  5854.40 ± 3067.89 |  5918.50 ± 3067.89 |
| ministral-3-8b-instruct-bf16 |  tg512 (c10) |   122.20 ± 2.49 |      14.32 ± 1.27 | 170.00 ± 0.00 |     17.30 ± 0.46 |                    |                    |                    |
| ministral-3-8b-instruct-bf16 | pp8192 (c20) |  7231.67 ± 4.96 | 1286.99 ± 1642.43 |               |                  | 11085.17 ± 5954.47 | 11021.08 ± 5954.47 | 11085.17 ± 5954.47 |
| ministral-3-8b-instruct-bf16 |  tg512 (c20) |   161.68 ± 1.01 |       9.88 ± 1.11 | 242.33 ± 3.30 |     13.67 ± 1.43 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-07 17:50:43 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
