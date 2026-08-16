# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-13 17:07:09
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model kat-coder-v2-5-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| kat-coder-v2-5-bf16 |  pp2048 @ d4 (c1) | 4119.18 ± 481.94 | 4119.18 ± 481.94 |               |                  |   584.97 ± 45.12 |   470.01 ± 45.12 |   584.97 ± 45.12 |
| kat-coder-v2-5-bf16 |   tg512 @ d4 (c1) |     30.51 ± 0.13 |     30.51 ± 0.13 |  31.00 ± 0.00 |     31.00 ± 0.00 |                  |                  |                  |
| kat-coder-v2-5-bf16 |  pp2048 @ d4 (c5) |  4725.35 ± 28.03 | 1218.38 ± 370.46 |               |                  | 1745.79 ± 362.24 | 1630.83 ± 362.24 | 1745.79 ± 362.24 |
| kat-coder-v2-5-bf16 |   tg512 @ d4 (c5) |     64.09 ± 0.32 |     13.96 ± 0.81 |  82.67 ± 1.89 |     20.40 ± 3.81 |                  |                  |                  |
| kat-coder-v2-5-bf16 | pp2048 @ d4 (c10) |   4739.36 ± 8.94 |  741.58 ± 419.50 |               |                  | 3070.71 ± 827.62 | 2955.75 ± 827.62 | 3070.71 ± 827.62 |
| kat-coder-v2-5-bf16 |  tg512 @ d4 (c10) |     77.92 ± 1.30 |      9.36 ± 0.73 | 113.33 ± 4.71 |     14.27 ± 3.72 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-13 17:00:12 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
