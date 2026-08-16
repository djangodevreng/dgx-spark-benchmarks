# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-15 22:51:50
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |    t/s (total) |      t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|-------------:|---------------:|---------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.8-27b-fp8 |  pp1024 (c1) | 558.56 ± 42.49 | 558.56 ± 42.49 |              |                  |   1953.90 ± 163.98 |   1751.57 ± 163.98 |   1953.90 ± 163.98 |
| qwen3.8-27b-fp8 |  tg1024 (c1) |    7.95 ± 0.00 |    7.95 ± 0.00 |  9.00 ± 0.00 |      9.00 ± 0.00 |                    |                    |                    |
| qwen3.8-27b-fp8 |  pp1024 (c5) |  600.77 ± 1.40 | 168.36 ± 68.75 |              |                  |  6404.51 ± 1650.00 |  6202.18 ± 1650.00 |  6404.51 ± 1650.00 |
| qwen3.8-27b-fp8 |  tg1024 (c5) |   37.54 ± 0.05 |    7.69 ± 0.09 | 45.00 ± 0.00 |      9.00 ± 0.00 |                    |                    |                    |
| qwen3.8-27b-fp8 | pp1024 (c10) |  606.85 ± 0.66 | 112.62 ± 72.77 |              |                  | 10863.23 ± 4022.15 | 10660.90 ± 4022.15 | 10863.23 ± 4022.15 |
| qwen3.8-27b-fp8 | tg1024 (c10) |   66.85 ± 0.04 |    7.06 ± 0.18 | 80.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-15 22:23:17 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
