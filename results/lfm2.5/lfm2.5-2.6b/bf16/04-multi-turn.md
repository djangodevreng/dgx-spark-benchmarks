# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-08 16:35:14
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model lfm2-5-2-6b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------|------------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| lfm2-5-2-6b-bf16 |  pp2048 @ d4 (c1) | 14227.86 ± 171.95 | 14227.86 ± 171.95 |               |                  |    175.70 ± 5.24 |    132.10 ± 5.24 |    175.70 ± 5.24 |
| lfm2-5-2-6b-bf16 |   tg512 @ d4 (c1) |      32.03 ± 0.36 |      32.03 ± 0.36 |  33.00 ± 0.00 |     33.00 ± 0.00 |                  |                  |                  |
| lfm2-5-2-6b-bf16 |  pp2048 @ d4 (c5) |  12795.40 ± 34.49 | 5005.80 ± 4542.87 |               |                  |  617.52 ± 221.70 |  573.92 ± 221.70 |  617.52 ± 221.70 |
| lfm2-5-2-6b-bf16 |   tg512 @ d4 (c5) |     187.08 ± 3.83 |      38.70 ± 1.02 | 200.00 ± 0.00 |     40.00 ± 0.00 |                  |                  |                  |
| lfm2-5-2-6b-bf16 | pp2048 @ d4 (c10) |  13106.00 ± 17.82 | 3050.07 ± 3514.83 |               |                  | 1044.18 ± 405.31 | 1000.57 ± 405.31 | 1044.18 ± 405.31 |
| lfm2-5-2-6b-bf16 |  tg512 @ d4 (c10) |     345.22 ± 6.89 |      36.76 ± 1.28 | 390.00 ± 0.00 |     39.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-08 16:32:11 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
