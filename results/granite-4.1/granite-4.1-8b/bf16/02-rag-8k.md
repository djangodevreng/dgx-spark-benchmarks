# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-09 06:56:13
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model granite-4-1-8b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| granite-4-1-8b-bf16 |  pp8192 (c5) | 3826.60 ± 80.17 | 1753.57 ± 1192.43 |               |                  |   5937.12 ± 2751.47 |   5816.87 ± 2751.47 |   5937.12 ± 2751.47 |
| granite-4-1-8b-bf16 |   tg512 (c5) |    47.11 ± 0.72 |      10.43 ± 0.59 |  60.67 ± 0.94 |     12.13 ± 0.34 |                     |                     |                     |
| granite-4-1-8b-bf16 | pp8192 (c10) |  3905.43 ± 2.59 | 1137.14 ± 1077.57 |               |                  |  10825.07 ± 5665.19 |  10704.83 ± 5665.19 |  10825.07 ± 5665.19 |
| granite-4-1-8b-bf16 |  tg512 (c10) |    69.03 ± 3.70 |       8.62 ± 1.45 | 110.00 ± 0.00 |     11.13 ± 0.34 |                     |                     |                     |
| granite-4-1-8b-bf16 | pp8192 (c20) |  3902.79 ± 1.64 |   697.89 ± 884.34 |               |                  | 20333.73 ± 10972.43 | 20213.48 ± 10972.43 | 20333.73 ± 10972.43 |
| granite-4-1-8b-bf16 |  tg512 (c20) |    89.50 ± 1.40 |       5.80 ± 0.77 | 160.00 ± 0.00 |      9.33 ± 1.23 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-09 06:40:31 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
