# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-06 14:28:44
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-e4b-it-bf16 |   pp256 (c1) | 3047.05 ± 1055.87 | 3047.05 ± 1055.87 |               |                  |  164.39 ± 41.12 |   91.16 ± 41.12 |  164.39 ± 41.12 |
| gemma-4-e4b-it-bf16 |  tg4096 (c1) |      18.97 ± 0.03 |      18.97 ± 0.03 |  20.00 ± 0.00 |     20.00 ± 0.00 |                 |                 |                 |
| gemma-4-e4b-it-bf16 |   pp256 (c5) |  5574.80 ± 174.09 |  1718.99 ± 111.18 |               |                  |   210.15 ± 7.01 |   136.92 ± 7.01 |   210.15 ± 7.01 |
| gemma-4-e4b-it-bf16 |  tg4096 (c5) |      64.84 ± 5.96 |      21.67 ± 0.33 | 113.33 ± 2.36 |     22.93 ± 0.25 |                 |                 |                 |
| gemma-4-e4b-it-bf16 |  pp256 (c10) | 5413.04 ± 1791.65 |   668.85 ± 251.59 |               |                  | 508.05 ± 218.28 | 434.82 ± 218.28 | 508.05 ± 218.28 |
| gemma-4-e4b-it-bf16 | tg4096 (c10) |    125.36 ± 12.06 |      21.71 ± 0.14 | 230.00 ± 0.00 |     23.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-06 14:23:40 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
