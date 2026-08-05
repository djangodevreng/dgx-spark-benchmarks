# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-10 00:27:53
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |       t/s (total) |         t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------|-------------:|------------------:|------------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-27b-bf16 |   pp256 (c1) | 2249.19 ± 1026.69 | 2249.19 ± 1026.69 |              |                  |   408.75 ± 99.38 |   151.71 ± 99.38 |   408.75 ± 99.38 |
| qwen3.6-27b-bf16 |  tg4096 (c1) |       4.43 ± 0.01 |       4.43 ± 0.01 |  5.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| qwen3.6-27b-bf16 |   pp256 (c5) |   1043.38 ± 15.00 |   361.32 ± 125.46 |              |                  |  958.71 ± 182.03 |  701.67 ± 182.03 |  958.71 ± 182.03 |
| qwen3.6-27b-bf16 |  tg4096 (c5) |      14.20 ± 2.13 |       4.22 ± 0.03 | 25.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| qwen3.6-27b-bf16 |  pp256 (c10) |   1175.65 ± 81.82 |    175.05 ± 72.30 |              |                  | 1743.96 ± 354.81 | 1486.91 ± 354.81 | 1743.96 ± 354.81 |
| qwen3.6-27b-bf16 | tg4096 (c10) |      28.46 ± 0.99 |       4.08 ± 0.03 | 50.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-09 22:12:11 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
