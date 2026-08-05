# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-09 20:02:10
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model            |          test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:-----------------|--------------:|---------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| qwen3.6-27b-bf16 |  pp25000 (c5) | 1223.32 ± 2.67 | 547.61 ± 335.17 |              |                  |   55716.72 ± 25711.33 |   55463.31 ± 25711.33 |   55717.09 ± 25711.56 |
| qwen3.6-27b-bf16 |    tg256 (c5) |    9.08 ± 0.07 |     2.72 ± 0.64 | 20.00 ± 0.00 |      4.40 ± 0.49 |                       |                       |                       |
| qwen3.6-27b-bf16 | pp25000 (c10) | 1160.90 ± 0.64 | 345.72 ± 302.12 |              |                  |  105385.79 ± 55937.50 |  105132.39 ± 55937.50 |  105386.35 ± 55937.71 |
| qwen3.6-27b-bf16 |   tg256 (c10) |   10.23 ± 0.01 |     1.90 ± 0.71 | 40.00 ± 0.00 |      4.20 ± 0.40 |                       |                       |                       |
| qwen3.6-27b-bf16 | pp25000 (c20) | 1028.74 ± 0.61 | 211.20 ± 260.80 |              |                  | 216151.63 ± 127859.99 | 215898.23 ± 127859.99 | 216152.37 ± 127860.39 |
| qwen3.6-27b-bf16 |   tg256 (c20) |   10.14 ± 0.02 |     1.15 ± 0.66 | 60.00 ± 0.00 |      3.75 ± 0.62 |                       |                       |                       |

llama-benchy (0.3.7)
date: 2026-05-09 19:14:08 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
