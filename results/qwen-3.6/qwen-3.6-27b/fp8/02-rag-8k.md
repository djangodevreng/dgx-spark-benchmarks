# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-14 19:09:31
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |   t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:----------------|-------------:|--------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| qwen3.6-27b-fp8 |  pp8192 (c5) | 606.69 ± 0.36 | 241.31 ± 135.03 |               |                  |  39096.02 ± 16295.52 |  38948.47 ± 16295.52 |  39096.02 ± 16295.52 |
| qwen3.6-27b-fp8 |   tg512 (c5) |  22.43 ± 0.05 |     5.93 ± 1.05 |  40.00 ± 0.00 |      8.00 ± 0.00 |                      |                      |                      |
| qwen3.6-27b-fp8 | pp8192 (c10) | 605.03 ± 0.09 | 158.83 ± 129.40 |               |                  |  70196.47 ± 34580.67 |  70048.92 ± 34580.67 |  70196.47 ± 34580.67 |
| qwen3.6-27b-fp8 |  tg512 (c10) |  28.05 ± 0.06 |     4.42 ± 1.27 |  70.00 ± 0.00 |      7.73 ± 0.44 |                      |                      |                      |
| qwen3.6-27b-fp8 | pp8192 (c20) | 601.56 ± 0.12 |  98.81 ± 107.57 |               |                  | 131963.74 ± 70785.35 | 131816.19 ± 70785.35 | 131963.74 ± 70785.35 |
| qwen3.6-27b-fp8 |  tg512 (c20) |  32.04 ± 0.09 |     2.98 ± 1.21 | 123.33 ± 4.71 |      7.18 ± 0.72 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-08-14 18:25:14 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
