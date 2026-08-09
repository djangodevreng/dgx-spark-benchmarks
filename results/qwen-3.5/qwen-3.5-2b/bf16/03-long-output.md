# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-07 14:39:55
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |         t/s (total) |           t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|--------------------:|--------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.5-2b-bf16 |   pp256 (c1) | 28382.17 ± 16366.97 | 28382.17 ± 16366.97 |               |                  |   51.46 ± 4.14 |   10.76 ± 4.14 |    51.46 ± 4.14 |
| qwen3.5-2b-bf16 |  tg4096 (c1) |        42.88 ± 0.01 |        42.88 ± 0.01 |  44.00 ± 0.00 |     44.00 ± 0.00 |                |                |                 |
| qwen3.5-2b-bf16 |   pp256 (c5) |   10780.05 ± 805.42 |   4946.49 ± 2166.85 |               |                  |  96.13 ± 15.97 |  55.43 ± 15.97 |   96.13 ± 15.97 |
| qwen3.5-2b-bf16 |  tg4096 (c5) |      122.27 ± 21.05 |        51.98 ± 2.62 | 273.33 ± 2.36 |     55.73 ± 0.93 |                |                |                 |
| qwen3.5-2b-bf16 |  pp256 (c10) |   10190.99 ± 241.39 |   1762.87 ± 1240.13 |               |                  | 198.71 ± 37.19 | 158.01 ± 37.19 |  198.71 ± 37.19 |
| qwen3.5-2b-bf16 | tg4096 (c10) |      245.19 ± 23.02 |        51.62 ± 1.00 | 520.00 ± 0.00 |     53.90 ± 1.42 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-07 14:36:58 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
