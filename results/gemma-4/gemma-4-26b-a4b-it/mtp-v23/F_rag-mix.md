# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-06-23 04:42:07
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-mtp --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |    t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:--------------------|-------------:|---------------:|------------------:|---------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b-mtp |  pp8192 (c5) | 4546.04 ± 3.51 | 2076.06 ± 1366.03 |                |                  |  5090.24 ± 2307.27 |  4939.25 ± 2307.27 |  5090.24 ± 2307.27 |
| gemma-4-26b-a4b-mtp |   tg512 (c5) |   70.32 ± 3.22 |      17.58 ± 2.85 |  118.33 ± 8.99 |     30.33 ± 3.38 |                    |                    |                    |
| gemma-4-26b-a4b-mtp | pp8192 (c10) | 4537.34 ± 1.91 | 1299.09 ± 1211.61 |                |                  |  9519.03 ± 4884.03 |  9368.03 ± 4884.03 |  9519.03 ± 4884.03 |
| gemma-4-26b-a4b-mtp |  tg512 (c10) |   97.26 ± 0.64 |      13.23 ± 1.94 |  186.33 ± 5.19 |     27.33 ± 3.72 |                    |                    |                    |
| gemma-4-26b-a4b-mtp | pp8192 (c20) | 4540.06 ± 0.44 |  801.70 ± 1005.75 |                |                  | 17686.05 ± 9416.85 | 17535.06 ± 9416.85 | 17686.05 ± 9416.85 |
| gemma-4-26b-a4b-mtp |  tg512 (c20) |  132.26 ± 4.78 |       9.70 ± 1.84 | 291.67 ± 10.87 |     22.77 ± 2.30 |                    |                    |                    |

llama-benchy (0.3.8)
date: 2026-06-23 04:31:15 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
