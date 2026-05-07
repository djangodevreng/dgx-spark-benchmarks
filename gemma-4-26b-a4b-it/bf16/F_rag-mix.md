# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-05 21:32:48
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:---------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b-bf16 |  pp8192 (c5) | 5439.51 ± 32.60 | 2389.85 ± 1521.69 |               |                  |  4316.12 ± 1902.30 |  4197.67 ± 1902.30 |  4316.12 ± 1902.30 |
| gemma-4-26b-a4b-bf16 |   tg512 (c5) |    55.21 ± 1.49 |      12.11 ± 0.51 |  70.00 ± 0.00 |     14.80 ± 1.68 |                    |                    |                    |
| gemma-4-26b-a4b-bf16 | pp8192 (c10) | 5466.71 ± 15.65 | 1491.18 ± 1308.97 |               |                  |  7990.46 ± 4023.35 |  7872.01 ± 4023.35 |  7990.46 ± 4023.35 |
| gemma-4-26b-a4b-bf16 |  tg512 (c10) |    78.36 ± 1.61 |       9.31 ± 0.77 | 110.00 ± 0.00 |     12.80 ± 1.01 |                    |                    |                    |
| gemma-4-26b-a4b-bf16 | pp8192 (c20) |  5532.74 ± 5.39 |  926.67 ± 1094.80 |               |                  | 14609.13 ± 7715.56 | 14490.69 ± 7715.56 | 14609.13 ± 7715.56 |
| gemma-4-26b-a4b-bf16 |  tg512 (c20) |    97.35 ± 3.50 |       6.05 ± 0.62 | 160.00 ± 0.00 |      9.95 ± 1.61 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-05 21:22:23 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
