# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-04 14:59:43
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|-------------:|----------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-27b-fp8 |  pp8192 (c5) | 1853.26 ± 45.70 | 748.55 ± 427.18 |               |                  |  12832.10 ± 5353.14 |  12678.50 ± 5353.14 |  12832.10 ± 5353.14 |
| qwen3.6-27b-fp8 |   tg512 (c5) |    30.03 ± 0.19 |     6.73 ± 0.41 |  40.00 ± 0.00 |      8.00 ± 0.00 |                     |                     |                     |
| qwen3.6-27b-fp8 | pp8192 (c10) | 1792.57 ± 23.55 | 499.13 ± 413.29 |               |                  | 23310.26 ± 11906.04 | 23156.66 ± 11906.04 | 23310.26 ± 11906.04 |
| qwen3.6-27b-fp8 |  tg512 (c10) |    45.13 ± 0.25 |     5.60 ± 0.64 |  70.00 ± 0.00 |      7.70 ± 0.46 |                     |                     |                     |
| qwen3.6-27b-fp8 | pp8192 (c20) | 1752.72 ± 13.06 | 303.07 ± 333.06 |               |                  | 44427.16 ± 24472.35 | 44273.56 ± 24472.35 | 44427.16 ± 24472.35 |
| qwen3.6-27b-fp8 |  tg512 (c20) |    60.55 ± 0.18 |     4.24 ± 0.76 | 120.00 ± 0.00 |      7.08 ± 0.69 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-04 14:40:23 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
