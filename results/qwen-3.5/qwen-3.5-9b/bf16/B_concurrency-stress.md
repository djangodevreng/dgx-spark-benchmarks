# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-09 14:36:11
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.5-9b-bf16 |  pp25000 (c5) | 3669.75 ± 3.01 | 1627.49 ± 1005.68 |               |                  |  18789.95 ± 8585.42 |  18695.53 ± 8585.42 |  18790.65 ± 8585.01 |
| qwen3.5-9b-bf16 |    tg256 (c5) |   28.27 ± 0.15 |       8.70 ± 2.17 |  65.00 ± 0.00 |     13.40 ± 0.49 |                     |                     |                     |
| qwen3.5-9b-bf16 | pp25000 (c10) | 3607.62 ± 3.51 |  1034.00 ± 890.68 |               |                  | 34578.50 ± 17889.67 | 34484.09 ± 17889.67 | 34579.97 ± 17889.52 |
| qwen3.5-9b-bf16 |   tg256 (c10) |   32.45 ± 0.11 |       6.19 ± 2.36 | 111.00 ± 0.82 |     12.53 ± 0.85 |                     |                     |                     |
| qwen3.5-9b-bf16 | pp25000 (c20) | 3500.40 ± 1.73 |   641.16 ± 762.08 |               |                  | 66901.69 ± 37356.88 | 66807.27 ± 37356.88 | 66903.31 ± 37357.42 |
| qwen3.5-9b-bf16 |   tg256 (c20) |   34.49 ± 0.03 |       4.05 ± 2.20 | 180.00 ± 0.00 |     11.20 ± 1.63 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-09 14:21:26 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
