# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-04 23:16:29
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |         t/s (total) |           t/s (req) |       peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|--------------------:|--------------------:|---------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.5-0.8b-bf16 |   pp256 (c1) | 39375.13 ± 27612.34 | 39375.13 ± 27612.34 |                |                  |  45.73 ± 21.40 |  19.78 ± 21.40 |   45.73 ± 21.40 |
| qwen3.5-0.8b-bf16 |  tg4096 (c1) |       110.48 ± 0.90 |       110.48 ± 0.90 |  112.58 ± 0.82 |    112.58 ± 0.82 |                |                |                 |
| qwen3.5-0.8b-bf16 |   pp256 (c5) |   18400.80 ± 361.55 |   8047.77 ± 2847.55 |                |                  |   57.43 ± 8.01 |   31.48 ± 8.01 |    57.43 ± 8.01 |
| qwen3.5-0.8b-bf16 |  tg4096 (c5) |      325.34 ± 95.38 |       115.04 ± 2.03 | 555.33 ± 24.36 |    119.21 ± 3.22 |                |                |                 |
| qwen3.5-0.8b-bf16 |  pp256 (c10) |  17641.56 ± 1934.01 |   3013.88 ± 1518.78 |                |                  | 116.26 ± 28.46 |  90.31 ± 28.46 |  116.26 ± 28.46 |
| qwen3.5-0.8b-bf16 | tg4096 (c10) |      588.08 ± 50.65 |       105.58 ± 3.62 | 1030.00 ± 0.00 |    112.03 ± 7.16 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-04 23:15:07 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
