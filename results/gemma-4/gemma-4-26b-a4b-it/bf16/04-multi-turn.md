# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-16 12:39:45
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-bf16 |  pp2048 @ d4 (c1) |  4848.35 ± 70.80 |   4848.35 ± 70.80 |               |                  |   515.30 ± 10.72 |   395.68 ± 10.72 |   515.30 ± 10.72 |
| gemma-4-26b-a4b-bf16 |   tg512 @ d4 (c1) |     23.86 ± 0.01 |      23.86 ± 0.01 |  24.00 ± 0.00 |     24.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 |  pp2048 @ d4 (c5) | 5138.23 ± 294.82 | 1948.79 ± 1524.57 |               |                  | 1486.30 ± 543.26 | 1366.68 ± 543.26 | 1486.30 ± 543.26 |
| gemma-4-26b-a4b-bf16 |   tg512 @ d4 (c5) |     60.87 ± 1.53 |      13.17 ± 0.46 |  71.67 ± 2.36 |     15.93 ± 1.18 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 | pp2048 @ d4 (c10) |  5439.80 ± 24.37 | 1251.80 ± 1329.27 |               |                  | 2404.60 ± 926.60 | 2284.97 ± 926.60 | 2404.60 ± 926.60 |
| gemma-4-26b-a4b-bf16 |  tg512 @ d4 (c10) |     89.64 ± 1.74 |       9.85 ± 0.26 | 116.67 ± 4.71 |     12.50 ± 0.62 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-16 12:32:12 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
