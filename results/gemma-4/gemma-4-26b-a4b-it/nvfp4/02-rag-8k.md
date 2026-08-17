# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-16 15:52:39
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b-nvfp4 |  pp8192 (c5) | 5236.92 ± 13.19 | 2382.74 ± 1556.90 |               |                  |  4378.79 ± 2025.46 |  4314.07 ± 2025.46 |  4378.79 ± 2025.46 |
| gemma-4-26b-a4b-nvfp4 |   tg512 (c5) |    90.19 ± 2.64 |      21.20 ± 2.04 | 125.00 ± 0.00 |     27.00 ± 1.10 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c10) | 5239.45 ± 57.27 | 1527.37 ± 1430.21 |               |                  |  8118.50 ± 4258.98 |  8053.78 ± 4258.98 |  8118.50 ± 4258.98 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c10) |   121.63 ± 4.74 |      16.02 ± 2.33 | 200.00 ± 0.00 |     22.67 ± 2.23 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c20) |  5208.19 ± 4.14 |  909.67 ± 1160.27 |               |                  | 15611.44 ± 8235.34 | 15546.72 ± 8235.34 | 15611.44 ± 8235.34 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c20) |   151.17 ± 1.92 |      10.41 ± 1.81 | 290.67 ± 8.22 |     16.97 ± 1.97 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-16 15:43:41 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
