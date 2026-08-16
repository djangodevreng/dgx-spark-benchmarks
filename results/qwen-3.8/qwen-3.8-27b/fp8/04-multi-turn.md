# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-16 01:31:10
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |   t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|------------------:|--------------:|----------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.8-27b-fp8 |  pp2048 @ d4 (c1) | 633.81 ± 1.63 |   633.81 ± 1.63 |              |                  |    3189.63 ± 80.06 |    3032.59 ± 80.06 |    3189.63 ± 80.06 |
| qwen3.8-27b-fp8 |   tg512 @ d4 (c1) |   7.93 ± 0.00 |     7.93 ± 0.00 |  8.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |
| qwen3.8-27b-fp8 |  pp2048 @ d4 (c5) | 609.76 ± 0.47 | 214.61 ± 107.42 |              |                  | 11052.51 ± 4046.39 | 10895.47 ± 4046.39 | 11052.51 ± 4046.39 |
| qwen3.8-27b-fp8 |   tg512 @ d4 (c5) |  33.04 ± 0.13 |     7.23 ± 0.39 | 40.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |
| qwen3.8-27b-fp8 | pp2048 @ d4 (c10) | 612.17 ± 0.63 | 140.88 ± 103.78 |              |                  | 19285.69 ± 8894.28 | 19128.65 ± 8894.28 | 19285.69 ± 8894.28 |
| qwen3.8-27b-fp8 |  tg512 @ d4 (c10) |  52.63 ± 0.03 |     6.30 ± 0.65 | 80.00 ± 0.00 |      8.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-16 01:14:08 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
