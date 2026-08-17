# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-17 04:03:43
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-e4b-it-bf16 | pp25000 (c20) | 4285.32 ± 4.69 | 745.87 ± 883.96 |               |                  | 55759.80 ± 30193.25 | 55683.03 ± 30193.25 | 55759.98 ± 30193.31 |
| gemma-4-e4b-it-bf16 |   tg256 (c20) |   41.47 ± 1.04 |     4.74 ± 2.75 | 260.00 ± 0.00 |     15.92 ± 2.40 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-17 03:55:20 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
