# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-09-18 16:03:09
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |              test |   t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------|------------------:|--------------:|----------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.8-27b-nvfp4 |  pp2048 @ d4 (c1) | 848.83 ± 3.66 |   848.83 ± 3.66 |               |                  |    2411.63 ± 31.01 |    2257.53 ± 31.01 |    2411.63 ± 31.01 |
| qwen3.8-27b-nvfp4 |   tg512 @ d4 (c1) |  12.26 ± 0.02 |    12.26 ± 0.02 |  13.33 ± 0.47 |     13.33 ± 0.47 |                    |                    |                    |
| qwen3.8-27b-nvfp4 |  pp2048 @ d4 (c5) | 804.15 ± 1.56 | 282.14 ± 141.71 |               |                  |  8410.15 ± 3043.71 |  8256.05 ± 3043.71 |  8410.15 ± 3043.71 |
| qwen3.8-27b-nvfp4 |   tg512 @ d4 (c5) |  47.75 ± 0.14 |    10.54 ± 0.62 |  60.00 ± 0.00 |     12.00 ± 0.00 |                    |                    |                    |
| qwen3.8-27b-nvfp4 | pp2048 @ d4 (c10) | 804.85 ± 0.92 | 186.05 ± 137.86 |               |                  | 14670.39 ± 6757.65 | 14516.29 ± 6757.65 | 14670.39 ± 6757.65 |
| qwen3.8-27b-nvfp4 |  tg512 @ d4 (c10) |  73.40 ± 0.07 |     8.90 ± 0.99 | 110.00 ± 0.00 |     11.10 ± 0.30 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-09-18 15:51:24 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
