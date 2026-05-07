# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-06 13:57:45
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-e4b-it-bf16 |  pp25000 (c5) | 4426.27 ± 8.74 | 1926.91 ± 1191.11 |               |                  |  15732.32 ± 7067.61 |  15659.41 ± 7067.61 |  15732.71 ± 7067.71 |
| gemma-4-e4b-it-bf16 |    tg256 (c5) |   37.83 ± 0.08 |      12.12 ± 3.86 |  95.00 ± 0.00 |     19.13 ± 0.34 |                     |                     |                     |
| gemma-4-e4b-it-bf16 | pp25000 (c10) | 4413.72 ± 7.34 | 1224.18 ± 1056.91 |               |                  | 28786.96 ± 14554.54 | 28714.05 ± 14554.54 | 28787.53 ± 14554.39 |
| gemma-4-e4b-it-bf16 |   tg256 (c10) |   40.30 ± 1.44 |       8.11 ± 3.82 | 170.00 ± 0.00 |     18.13 ± 0.99 |                     |                     |                     |
| gemma-4-e4b-it-bf16 | pp25000 (c20) | 4400.89 ± 5.85 |   755.49 ± 871.45 |               |                  | 54466.98 ± 29473.07 | 54394.07 ± 29473.07 | 54467.46 ± 29473.33 |
| gemma-4-e4b-it-bf16 |   tg256 (c20) |   43.12 ± 0.25 |       4.98 ± 3.02 | 266.00 ± 0.00 |     16.00 ± 1.91 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-06 13:46:21 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
