# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-07 16:38:24
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.5-4b-bf16 |  pp8192 (c5) | 5863.10 ± 213.45 | 2501.03 ± 1478.37 |               |                  |  3942.15 ± 1709.41 |  3883.55 ± 1709.41 |  3942.15 ± 1709.41 |
| qwen3.5-4b-bf16 |   tg512 (c5) |     94.04 ± 0.83 |      21.00 ± 1.28 | 120.33 ± 0.47 |     24.07 ± 0.25 |                    |                    |                    |
| qwen3.5-4b-bf16 | pp8192 (c10) |  5895.33 ± 34.81 | 1623.82 ± 1412.30 |               |                  |  7144.76 ± 3558.41 |  7086.16 ± 3558.41 |  7144.76 ± 3558.41 |
| qwen3.5-4b-bf16 |  tg512 (c10) |    142.18 ± 0.49 |      17.50 ± 1.85 | 210.00 ± 0.00 |     22.13 ± 1.09 |                    |                    |                    |
| qwen3.5-4b-bf16 | pp8192 (c20) |  5954.88 ± 65.58 | 1060.83 ± 1257.52 |               |                  | 13093.34 ± 7162.43 | 13034.74 ± 7162.43 | 13093.34 ± 7162.43 |
| qwen3.5-4b-bf16 |  tg512 (c20) |    181.63 ± 0.82 |      12.17 ± 1.79 | 325.33 ± 7.54 |     19.72 ± 2.65 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-07 16:30:03 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
