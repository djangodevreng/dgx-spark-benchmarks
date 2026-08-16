# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-16 01:14:08
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|-------------:|----------------:|----------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.8-27b-fp8 |   pp256 (c1) | 721.56 ± 143.76 | 721.56 ± 143.76 |              |                  |   489.81 ± 48.41 |   329.29 ± 48.41 |   489.81 ± 48.41 |
| qwen3.8-27b-fp8 |  tg4096 (c1) |     7.94 ± 0.00 |     7.94 ± 0.00 |  8.67 ± 0.47 |      8.67 ± 0.47 |                  |                  |                  |
| qwen3.8-27b-fp8 |   pp256 (c5) |   554.28 ± 7.45 |  139.56 ± 42.09 |              |                  | 1906.14 ± 334.20 | 1745.62 ± 334.20 | 1906.14 ± 334.20 |
| qwen3.8-27b-fp8 |  tg4096 (c5) |    32.79 ± 0.81 |     7.75 ± 0.01 | 41.67 ± 2.36 |      8.33 ± 0.47 |                  |                  |                  |
| qwen3.8-27b-fp8 |  pp256 (c10) |   550.48 ± 6.67 |   65.73 ± 16.38 |              |                  | 3687.74 ± 541.52 | 3527.23 ± 541.52 | 3687.74 ± 541.52 |
| qwen3.8-27b-fp8 | tg4096 (c10) |    65.57 ± 1.95 |     7.29 ± 0.03 | 80.00 ± 0.00 |      8.07 ± 0.25 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-15 23:36:00 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
