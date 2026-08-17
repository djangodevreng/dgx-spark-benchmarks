# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-17 03:34:31
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-e4b-it-bf16 |  pp2048 @ d4 (c1) | 7001.06 ± 169.31 |  7001.06 ± 169.31 |               |                  |    331.48 ± 2.14 |    258.82 ± 2.14 |    331.48 ± 2.14 |
| gemma-4-e4b-it-bf16 |   tg512 @ d4 (c1) |     19.47 ± 0.01 |      19.47 ± 0.01 |  20.00 ± 0.00 |     20.00 ± 0.00 |                  |                  |                  |
| gemma-4-e4b-it-bf16 |  pp2048 @ d4 (c5) |  6956.62 ± 17.04 | 2613.28 ± 2289.58 |               |                  | 1141.82 ± 403.59 | 1069.16 ± 403.59 | 1141.82 ± 403.59 |
| gemma-4-e4b-it-bf16 |   tg512 @ d4 (c5) |     97.88 ± 9.74 |      22.21 ± 0.36 | 116.67 ± 2.36 |     23.47 ± 0.50 |                  |                  |                  |
| gemma-4-e4b-it-bf16 | pp2048 @ d4 (c10) |  7190.94 ± 15.87 | 1718.18 ± 1928.97 |               |                  | 1806.22 ± 727.64 | 1733.56 ± 727.64 | 1806.22 ± 727.64 |
| gemma-4-e4b-it-bf16 |  tg512 @ d4 (c10) |   145.37 ± 15.16 |      20.77 ± 1.25 | 220.00 ± 0.00 |     22.73 ± 0.44 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-17 03:29:32 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
