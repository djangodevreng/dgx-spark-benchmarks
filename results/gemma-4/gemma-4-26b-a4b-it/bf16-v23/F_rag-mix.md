# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-06-23 00:36:00
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b |  pp8192 (c5) |  5121.41 ± 4.24 | 2301.15 ± 1493.57 |               |                  |  4540.10 ± 2050.31 |  4428.52 ± 2050.31 |  4540.10 ± 2050.31 |
| gemma-4-26b-a4b |   tg512 (c5) |    55.50 ± 2.13 |      12.67 ± 0.91 |  73.33 ± 2.36 |     15.80 ± 2.26 |                    |                    |                    |
| gemma-4-26b-a4b | pp8192 (c10) |  5120.73 ± 4.63 | 1440.73 ± 1339.54 |               |                  |  8487.64 ± 4328.88 |  8376.06 ± 4328.88 |  8487.64 ± 4328.88 |
| gemma-4-26b-a4b |  tg512 (c10) |    78.35 ± 4.17 |       9.53 ± 0.82 | 114.00 ± 4.32 |     12.97 ± 1.17 |                    |                    |                    |
| gemma-4-26b-a4b | pp8192 (c20) | 5139.06 ± 10.52 |  891.77 ± 1097.12 |               |                  | 15698.98 ± 8338.58 | 15587.40 ± 8338.58 | 15698.98 ± 8338.58 |
| gemma-4-26b-a4b |  tg512 (c20) |   100.81 ± 1.87 |       6.16 ± 0.63 | 160.00 ± 0.00 |      9.85 ± 1.74 |                    |                    |                    |

llama-benchy (0.3.8)
date: 2026-06-23 00:22:17 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
