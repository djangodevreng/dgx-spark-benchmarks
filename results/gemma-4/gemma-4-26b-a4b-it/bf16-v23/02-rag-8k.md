# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-06 08:35:35
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b |  pp8192 (c5) | 4846.70 ± 10.95 | 2258.79 ± 1509.42 |               |                  |  4715.03 ± 2181.35 |  4595.87 ± 2181.35 |  4715.03 ± 2181.35 |
| gemma-4-26b-a4b |   tg512 (c5) |    52.22 ± 1.28 |      12.22 ± 0.93 |  68.33 ± 2.36 |     15.87 ± 1.20 |                    |                    |                    |
| gemma-4-26b-a4b | pp8192 (c10) |  4869.04 ± 6.01 | 1430.87 ± 1366.72 |               |                  |  8794.63 ± 4564.93 |  8675.46 ± 4564.93 |  8794.63 ± 4564.93 |
| gemma-4-26b-a4b |  tg512 (c10) |    75.79 ± 0.37 |       8.74 ± 0.68 | 110.00 ± 0.00 |     11.60 ± 0.84 |                    |                    |                    |
| gemma-4-26b-a4b | pp8192 (c20) |  4896.36 ± 2.73 |  873.99 ± 1114.24 |               |                  | 16372.88 ± 8767.15 | 16253.71 ± 8767.15 | 16372.88 ± 8767.15 |
| gemma-4-26b-a4b |  tg512 (c20) |    93.69 ± 0.82 |       5.86 ± 0.66 | 150.00 ± 7.07 |      9.87 ± 1.72 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-06 08:21:03 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
