# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-06 14:17:36
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|------------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-e4b-it-bf16 |  pp2048 @ d4 (c1) | 6653.79 ± 3447.03 | 6653.79 ± 3447.03 |               |                  |  552.68 ± 378.92 |  470.60 ± 378.92 |  552.68 ± 378.92 |
| gemma-4-e4b-it-bf16 |   tg512 @ d4 (c1) |      19.00 ± 0.03 |      19.00 ± 0.03 |  20.00 ± 0.00 |     20.00 ± 0.00 |                  |                  |                  |
| gemma-4-e4b-it-bf16 |  pp2048 @ d4 (c5) |  7314.09 ± 145.56 | 2312.33 ± 1003.23 |               |                  | 1012.88 ± 301.24 |  930.79 ± 301.24 | 1012.88 ± 301.24 |
| gemma-4-e4b-it-bf16 |   tg512 @ d4 (c5) |      95.85 ± 7.30 |      21.22 ± 0.31 | 110.00 ± 0.00 |     22.40 ± 0.49 |                  |                  |                  |
| gemma-4-e4b-it-bf16 | pp2048 @ d4 (c10) |   7409.64 ± 64.11 | 1589.84 ± 1545.79 |               |                  | 1777.93 ± 695.93 | 1695.85 ± 695.93 | 1777.93 ± 695.93 |
| gemma-4-e4b-it-bf16 |  tg512 @ d4 (c10) |    158.64 ± 10.61 |      20.10 ± 1.33 | 220.00 ± 0.00 |     22.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-06 14:13:38 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
