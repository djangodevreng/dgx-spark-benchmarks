# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-07 15:42:19
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |              test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|------------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| ministral-3-3b-instruct-bf16 |  pp2048 @ d4 (c1) | 15204.00 ± 1056.87 | 15204.00 ± 1056.87 |               |                  |   165.22 ± 9.11 |   123.13 ± 9.11 |   165.22 ± 9.11 |
| ministral-3-3b-instruct-bf16 |   tg512 @ d4 (c1) |       50.65 ± 0.07 |       50.65 ± 0.07 |  51.00 ± 0.00 |     51.00 ± 0.00 |                 |                 |                 |
| ministral-3-3b-instruct-bf16 |  pp2048 @ d4 (c5) |  14501.75 ± 168.81 |  5624.26 ± 5012.24 |               |                  | 539.97 ± 191.67 | 497.87 ± 191.67 | 539.97 ± 191.67 |
| ministral-3-3b-instruct-bf16 |   tg512 @ d4 (c5) |      231.17 ± 3.32 |       48.80 ± 0.82 | 251.67 ± 2.36 |     50.87 ± 0.34 |                 |                 |                 |
| ministral-3-3b-instruct-bf16 | pp2048 @ d4 (c10) |   16284.47 ± 18.21 |  3618.05 ± 3820.53 |               |                  | 822.74 ± 314.11 | 780.64 ± 314.11 | 822.74 ± 314.11 |
| ministral-3-3b-instruct-bf16 |  tg512 @ d4 (c10) |      401.00 ± 7.63 |       43.19 ± 1.10 | 460.00 ± 0.00 |     46.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-07 15:40:35 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
