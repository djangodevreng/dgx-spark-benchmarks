# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-17 03:23:48
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:--------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-e4b-it-bf16 |  pp8192 (c5) | 6137.49 ± 47.60 | 2670.77 ± 1708.32 |               |                  |  3824.43 ± 1684.81 |  3749.07 ± 1684.81 |  3824.43 ± 1684.81 |
| gemma-4-e4b-it-bf16 |   tg512 (c5) |    80.21 ± 7.74 |      19.26 ± 1.69 | 110.00 ± 0.00 |     22.20 ± 0.40 |                    |                    |                    |
| gemma-4-e4b-it-bf16 | pp8192 (c10) | 6271.18 ± 14.39 | 1778.24 ± 1669.67 |               |                  |  6935.19 ± 3542.08 |  6859.83 ± 3542.08 |  6935.19 ± 3542.08 |
| gemma-4-e4b-it-bf16 |  tg512 (c10) |   118.42 ± 7.12 |      16.04 ± 4.20 | 210.00 ± 0.00 |     21.17 ± 0.37 |                    |                    |                    |
| gemma-4-e4b-it-bf16 | pp8192 (c20) | 6270.25 ± 74.94 | 1103.03 ± 1381.35 |               |                  | 12857.83 ± 6869.31 | 12782.47 ± 6869.31 | 12857.83 ± 6869.31 |
| gemma-4-e4b-it-bf16 |  tg512 (c20) |   168.17 ± 8.23 |      11.98 ± 3.13 | 334.33 ± 8.01 |     18.77 ± 1.35 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-17 03:15:42 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
