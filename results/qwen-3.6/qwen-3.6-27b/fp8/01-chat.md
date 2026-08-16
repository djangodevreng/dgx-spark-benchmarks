# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-14 18:25:14
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |    t/s (total) |      t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|-------------:|---------------:|---------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.6-27b-fp8 |  pp1024 (c1) | 551.90 ± 41.22 | 551.90 ± 41.22 |              |                  |   1895.41 ± 135.08 |   1721.63 ± 135.08 |   1895.41 ± 135.08 |
| qwen3.6-27b-fp8 |  tg1024 (c1) |    7.80 ± 0.00 |    7.80 ± 0.00 |  9.00 ± 0.00 |      9.00 ± 0.00 |                    |                    |                    |
| qwen3.6-27b-fp8 |  pp1024 (c5) | 601.16 ± 19.81 | 167.00 ± 65.82 |              |                  |  6485.93 ± 1673.23 |  6312.15 ± 1673.23 |  6485.93 ± 1673.23 |
| qwen3.6-27b-fp8 |  tg1024 (c5) |   36.80 ± 0.15 |    7.54 ± 0.09 | 40.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |
| qwen3.6-27b-fp8 | pp1024 (c10) | 586.49 ± 21.41 | 105.86 ± 66.54 |              |                  | 11411.26 ± 4123.58 | 11237.48 ± 4123.58 | 11411.26 ± 4123.58 |
| qwen3.6-27b-fp8 | tg1024 (c10) |   65.43 ± 0.94 |    6.94 ± 0.19 | 80.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-14 17:55:57 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
