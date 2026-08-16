# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-14 21:02:20
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |   t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|------------------:|--------------:|----------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.6-27b-fp8 |  pp2048 @ d4 (c1) | 632.90 ± 1.71 |   632.90 ± 1.71 |              |                  |    3103.94 ± 55.61 |    2957.70 ± 55.61 |    3103.94 ± 55.61 |
| qwen3.6-27b-fp8 |   tg512 @ d4 (c1) |   7.90 ± 0.00 |     7.90 ± 0.00 |  8.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |
| qwen3.6-27b-fp8 |  pp2048 @ d4 (c5) | 609.56 ± 0.18 | 212.67 ± 104.54 |              |                  | 10847.65 ± 3973.48 | 10701.41 ± 3973.48 | 10847.65 ± 3973.48 |
| qwen3.6-27b-fp8 |   tg512 @ d4 (c5) |  33.15 ± 0.04 |     7.25 ± 0.38 | 40.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |
| qwen3.6-27b-fp8 | pp2048 @ d4 (c10) | 608.54 ± 0.55 | 138.92 ± 105.13 |              |                  | 19440.23 ± 8849.24 | 19294.00 ± 8849.24 | 19440.23 ± 8849.24 |
| qwen3.6-27b-fp8 |  tg512 @ d4 (c10) |  52.62 ± 0.14 |     6.30 ± 0.64 | 80.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-14 20:45:19 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
