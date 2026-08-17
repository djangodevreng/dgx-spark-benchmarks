# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-17 05:52:52
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|------------------:|---------------:|-----------------:|------------------:|------------------:|------------------:|
| gemma-4-e2b-it-bf16 |  pp8192 (c5) |  9868.86 ± 39.19 | 4358.72 ± 2724.33 |                |                  | 2335.35 ± 1051.27 | 2293.90 ± 1051.27 | 2335.35 ± 1051.27 |
| gemma-4-e2b-it-bf16 |   tg512 (c5) |    158.71 ± 9.96 |      38.02 ± 2.99 |  216.67 ± 2.36 |     43.40 ± 0.49 |                   |                   |                   |
| gemma-4-e2b-it-bf16 | pp8192 (c10) | 10037.79 ± 31.47 | 2809.48 ± 2564.98 |                |                  | 4319.93 ± 2203.64 | 4278.48 ± 2203.64 | 4319.93 ± 2203.64 |
| gemma-4-e2b-it-bf16 |  tg512 (c10) |    261.38 ± 0.65 |      32.69 ± 4.43 |  410.00 ± 0.00 |     41.00 ± 0.00 |                   |                   |                   |
| gemma-4-e2b-it-bf16 | pp8192 (c20) |  10107.45 ± 6.17 | 1759.49 ± 2150.99 |                |                  | 7958.30 ± 4245.64 | 7916.85 ± 4245.64 | 7958.30 ± 4245.64 |
| gemma-4-e2b-it-bf16 |  tg512 (c20) |    331.45 ± 5.81 |      23.41 ± 4.79 | 673.33 ± 18.86 |     34.52 ± 0.94 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-17 05:48:20 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
