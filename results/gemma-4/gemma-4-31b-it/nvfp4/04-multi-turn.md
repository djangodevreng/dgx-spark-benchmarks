# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-16 19:46:30
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |              test |   t/s (total) |      t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------|------------------:|--------------:|---------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-31b-nvfp4 |  pp2048 @ d4 (c1) | 860.98 ± 8.21 |  860.98 ± 8.21 |              |                  |    2375.13 ± 69.28 |    2167.29 ± 69.28 |    2375.13 ± 69.28 |
| gemma-4-31b-nvfp4 |   tg512 @ d4 (c1) |   6.92 ± 0.00 |    6.92 ± 0.00 |  7.67 ± 0.47 |      7.67 ± 0.47 |                    |                    |                    |
| gemma-4-31b-nvfp4 |  pp2048 @ d4 (c5) | 878.06 ± 1.31 | 231.62 ± 90.52 |              |                  |  8991.98 ± 2142.29 |  8784.13 ± 2142.29 |  8991.98 ± 2142.29 |
| gemma-4-31b-nvfp4 |   tg512 @ d4 (c5) |  24.89 ± 1.32 |    6.37 ± 0.31 | 35.00 ± 0.00 |      7.00 ± 0.00 |                    |                    |                    |
| gemma-4-31b-nvfp4 | pp2048 @ d4 (c10) | 889.71 ± 1.81 | 128.28 ± 61.85 |              |                  | 16586.27 ± 4278.97 | 16378.43 ± 4278.97 | 16586.27 ± 4278.97 |
| gemma-4-31b-nvfp4 |  tg512 @ d4 (c10) |  43.41 ± 3.27 |    5.71 ± 0.69 | 70.00 ± 0.00 |      7.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-16 19:30:32 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
