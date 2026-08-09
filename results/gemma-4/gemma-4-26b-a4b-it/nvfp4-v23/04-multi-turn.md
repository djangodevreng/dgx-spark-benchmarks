# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-06 12:03:44
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c1) | 6509.56 ± 102.15 |  6509.56 ± 102.15 |               |                  |    348.76 ± 7.64 |    281.40 ± 7.64 |    348.76 ± 7.64 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c1) |     29.66 ± 0.02 |      29.66 ± 0.02 |  30.00 ± 0.00 |     30.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c5) |  6221.30 ± 86.10 | 2571.63 ± 2088.26 |               |                  | 1125.11 ± 435.10 | 1057.75 ± 435.10 | 1125.11 ± 435.10 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c5) |    106.62 ± 5.54 |      24.17 ± 0.48 | 128.33 ± 2.36 |     28.33 ± 1.99 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp2048 @ d4 (c10) |  6402.91 ± 84.95 | 1542.80 ± 1739.74 |               |                  | 2016.56 ± 832.64 | 1949.20 ± 832.64 | 2016.56 ± 832.64 |
| gemma-4-26b-a4b-nvfp4 |  tg512 @ d4 (c10) |    172.32 ± 7.46 |      19.50 ± 0.84 | 210.00 ± 0.00 |     22.13 ± 1.09 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 11:59:14 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
