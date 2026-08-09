# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-09 00:37:44
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| ministral-3-3b-instruct-bf16 |  pp2048 @ d4 (c1) | 3625.55 ± 186.60 | 3625.55 ± 186.60 |               |                  |   554.94 ± 22.67 |   525.02 ± 22.67 |   554.94 ± 22.67 |
| ministral-3-3b-instruct-bf16 |   tg512 @ d4 (c1) |     50.23 ± 0.14 |     50.23 ± 0.14 |  51.00 ± 0.00 |     51.00 ± 0.00 |                  |                  |                  |
| ministral-3-3b-instruct-bf16 |  pp2048 @ d4 (c5) | 8631.95 ± 451.80 | 1988.37 ± 436.97 |               |                  |  998.58 ± 166.45 |  968.66 ± 166.45 |  998.58 ± 166.45 |
| ministral-3-3b-instruct-bf16 |   tg512 @ d4 (c5) |    211.72 ± 0.37 |     43.49 ± 0.52 | 225.00 ± 0.00 |     45.00 ± 0.00 |                  |                  |                  |
| ministral-3-3b-instruct-bf16 | pp2048 @ d4 (c10) | 12155.42 ± 88.83 | 1713.74 ± 630.71 |               |                  | 1210.36 ± 304.90 | 1180.44 ± 304.90 | 1210.36 ± 304.90 |
| ministral-3-3b-instruct-bf16 |  tg512 @ d4 (c10) |    329.33 ± 3.13 |     34.98 ± 0.77 | 373.33 ± 4.71 |     37.33 ± 0.47 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-09 00:35:05 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
