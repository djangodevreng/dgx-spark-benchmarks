# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-17 05:58:17
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |    est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|------------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|----------------:|-----------------:|
| gemma-4-e2b-it-bf16 |  pp2048 @ d4 (c1) | 12981.68 ± 602.72 | 12981.68 ± 602.72 |               |                  |    185.30 ± 7.37 |   145.23 ± 7.37 |    185.30 ± 7.37 |
| gemma-4-e2b-it-bf16 |   tg512 @ d4 (c1) |      39.36 ± 0.03 |      39.36 ± 0.03 |  40.00 ± 0.00 |     40.00 ± 0.00 |                  |                 |                  |
| gemma-4-e2b-it-bf16 |  pp2048 @ d4 (c5) |  12281.07 ± 68.93 | 5242.09 ± 4045.49 |               |                  |  548.24 ± 206.25 | 508.17 ± 206.25 |  548.24 ± 206.25 |
| gemma-4-e2b-it-bf16 |   tg512 @ d4 (c5) |    200.88 ± 12.06 |      43.63 ± 0.72 | 225.00 ± 0.00 |     45.00 ± 0.00 |                  |                 |                  |
| gemma-4-e2b-it-bf16 | pp2048 @ d4 (c10) |  12823.88 ± 49.86 | 3053.64 ± 3260.32 |               |                  | 1004.95 ± 411.24 | 964.89 ± 411.24 | 1004.95 ± 411.24 |
| gemma-4-e2b-it-bf16 |  tg512 @ d4 (c10) |    374.54 ± 17.13 |      41.67 ± 1.35 | 440.00 ± 0.00 |     44.20 ± 0.40 |                  |                 |                  |

llama-benchy (0.4.0)
date: 2026-08-17 05:55:44 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
