# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-07 03:34:00
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| ministral-3-8b-instruct-bf16 |  pp2048 @ d4 (c1) | 4691.28 ± 171.30 | 4691.28 ± 171.30 |               |                  |   457.13 ± 16.04 |   396.28 ± 16.04 |   457.13 ± 16.04 |
| ministral-3-8b-instruct-bf16 |   tg512 @ d4 (c1) |     25.07 ± 0.05 |     25.07 ± 0.05 |  26.00 ± 0.00 |     26.00 ± 0.00 |                  |                  |                  |
| ministral-3-8b-instruct-bf16 |  pp2048 @ d4 (c5) | 5233.05 ± 124.71 | 1284.64 ± 397.09 |               |                  | 1598.89 ± 331.41 | 1538.04 ± 331.41 | 1598.89 ± 331.41 |
| ministral-3-8b-instruct-bf16 |   tg512 @ d4 (c5) |    111.49 ± 4.20 |     23.54 ± 2.51 | 124.33 ± 0.94 |     24.87 ± 0.50 |                  |                  |                  |
| ministral-3-8b-instruct-bf16 | pp2048 @ d4 (c10) | 7081.71 ± 533.50 | 1244.23 ± 875.47 |               |                  | 1966.19 ± 701.42 | 1905.34 ± 701.42 | 1966.19 ± 701.42 |
| ministral-3-8b-instruct-bf16 |  tg512 @ d4 (c10) |    206.49 ± 0.76 |     21.89 ± 0.60 | 230.00 ± 0.00 |     23.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-07 03:29:24 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
