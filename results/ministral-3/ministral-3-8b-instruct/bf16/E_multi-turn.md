# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-07 17:50:42
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| ministral-3-8b-instruct-bf16 |  pp2048 @ d4 (c1) | 9995.59 ± 313.86 |  9995.59 ± 313.86 |               |                  |    249.40 ± 6.57 |    179.84 ± 6.57 |    249.40 ± 6.57 |
| ministral-3-8b-instruct-bf16 |   tg512 @ d4 (c1) |     21.86 ± 0.01 |      21.86 ± 0.01 |  22.33 ± 0.47 |     22.33 ± 0.47 |                  |                  |                  |
| ministral-3-8b-instruct-bf16 |  pp2048 @ d4 (c5) |  8419.59 ± 38.57 | 3277.72 ± 2948.92 |               |                  |  948.27 ± 338.34 |  878.70 ± 338.34 |  948.27 ± 338.34 |
| ministral-3-8b-instruct-bf16 |   tg512 @ d4 (c5) |    111.28 ± 0.58 |      22.95 ± 0.40 | 120.00 ± 0.00 |     24.00 ± 0.00 |                  |                  |                  |
| ministral-3-8b-instruct-bf16 | pp2048 @ d4 (c10) | 8154.18 ± 633.34 | 1799.50 ± 1850.67 |               |                  | 1660.57 ± 670.18 | 1591.01 ± 670.18 | 1660.57 ± 670.18 |
| ministral-3-8b-instruct-bf16 |  tg512 @ d4 (c10) |    194.92 ± 0.94 |      20.82 ± 0.57 | 220.00 ± 0.00 |     22.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-07 17:47:01 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
