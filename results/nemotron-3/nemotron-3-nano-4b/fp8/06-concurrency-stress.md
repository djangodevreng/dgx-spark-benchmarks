# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-08 10:04:54
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                  |          test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------|--------------:|-----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-4b-fp8 | pp25000 (c20) | 9695.82 ± 275.59 | 1796.77 ± 2133.53 |               |                  | 24235.29 ± 13618.71 | 23803.37 ± 13399.38 | 23847.57 ± 13399.73 |
| nemotron-3-nano-4b-fp8 |   tg256 (c20) |     90.74 ± 2.02 |      10.09 ± 4.98 | 378.33 ± 2.36 |     27.66 ± 6.71 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-08 10:01:01 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
