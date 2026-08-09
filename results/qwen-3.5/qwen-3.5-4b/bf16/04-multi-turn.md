# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-07 17:20:47
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|------------------:|----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.5-4b-bf16 |  pp2048 @ d4 (c1) | 7356.59 ± 21.15 |   7356.59 ± 21.15 |               |                  |    321.83 ± 3.77 |    263.17 ± 3.77 |    321.83 ± 3.77 |
| qwen3.5-4b-bf16 |   tg512 @ d4 (c1) |    20.59 ± 0.09 |      20.59 ± 0.09 |  21.00 ± 0.00 |     21.00 ± 0.00 |                  |                  |                  |
| qwen3.5-4b-bf16 |  pp2048 @ d4 (c5) | 6301.86 ± 50.06 | 3087.82 ± 2152.92 |               |                  |  923.96 ± 417.78 |  865.30 ± 417.78 |  923.96 ± 417.78 |
| qwen3.5-4b-bf16 |   tg512 @ d4 (c5) |   112.55 ± 0.91 |      23.23 ± 0.41 | 125.00 ± 0.00 |     25.00 ± 0.00 |                  |                  |                  |
| qwen3.5-4b-bf16 | pp2048 @ d4 (c10) | 6290.96 ± 23.54 | 1889.86 ± 1853.61 |               |                  | 1731.50 ± 878.73 | 1672.83 ± 878.73 | 1731.50 ± 878.73 |
| qwen3.5-4b-bf16 |  tg512 @ d4 (c10) |   198.88 ± 1.74 |      21.22 ± 0.69 | 230.00 ± 0.00 |     23.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-07 17:15:43 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
