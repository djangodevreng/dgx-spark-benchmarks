# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-06 08:49:40
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b |  pp2048 @ d4 (c1) | 5134.19 ± 123.87 |  5134.19 ± 123.87 |               |                  |   480.70 ± 10.20 |   361.40 ± 10.20 |   480.70 ± 10.20 |
| gemma-4-26b-a4b |   tg512 @ d4 (c1) |     23.76 ± 0.00 |      23.76 ± 0.00 |  24.00 ± 0.00 |     24.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b |  pp2048 @ d4 (c5) |  5456.60 ± 30.02 | 2013.09 ± 1668.94 |               |                  | 1464.26 ± 500.82 | 1344.95 ± 500.82 | 1464.26 ± 500.82 |
| gemma-4-26b-a4b |   tg512 @ d4 (c5) |     61.18 ± 0.93 |      13.25 ± 0.37 |  75.00 ± 4.08 |     16.60 ± 0.88 |                  |                  |                  |
| gemma-4-26b-a4b | pp2048 @ d4 (c10) |  5497.43 ± 40.55 | 1335.33 ± 1402.57 |               |                  | 2315.54 ± 941.92 | 2196.23 ± 941.92 | 2315.54 ± 941.92 |
| gemma-4-26b-a4b |  tg512 @ d4 (c10) |     88.68 ± 0.92 |      10.18 ± 0.42 | 113.33 ± 4.71 |     12.77 ± 0.88 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 08:42:07 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
