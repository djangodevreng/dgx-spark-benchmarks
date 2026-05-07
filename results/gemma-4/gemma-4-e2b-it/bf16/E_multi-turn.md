# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-06 12:28:16
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|------------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-e2b-it-bf16 |  pp2048 @ d4 (c1) | 15114.39 ± 115.45 | 15114.39 ± 115.45 |               |                  |   168.48 ± 3.27 |   125.31 ± 3.27 |   168.48 ± 3.27 |
| gemma-4-e2b-it-bf16 |   tg512 @ d4 (c1) |      38.25 ± 0.39 |      38.25 ± 0.39 |  39.00 ± 0.00 |     39.00 ± 0.00 |                 |                 |                 |
| gemma-4-e2b-it-bf16 |  pp2048 @ d4 (c5) | 13234.23 ± 156.15 | 4985.76 ± 4120.69 |               |                  | 573.45 ± 206.18 | 530.28 ± 206.18 | 573.45 ± 206.18 |
| gemma-4-e2b-it-bf16 |   tg512 @ d4 (c5) |     197.47 ± 2.98 |      41.11 ± 0.75 | 214.67 ± 0.47 |     43.00 ± 0.00 |                 |                 |                 |
| gemma-4-e2b-it-bf16 | pp2048 @ d4 (c10) |  13596.16 ± 96.10 | 2385.44 ± 1051.74 |               |                  | 969.57 ± 335.53 | 926.40 ± 335.53 | 969.57 ± 335.53 |
| gemma-4-e2b-it-bf16 |  tg512 @ d4 (c10) |     383.07 ± 7.23 |      40.50 ± 1.03 | 430.00 ± 0.00 |     43.27 ± 0.44 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-06 12:26:14 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
