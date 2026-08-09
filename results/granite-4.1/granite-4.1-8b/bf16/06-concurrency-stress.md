# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-09 08:04:50
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model granite-4-1-8b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| granite-4-1-8b-bf16 | pp25000 (c20) | 3102.83 ± 1.50 | 546.21 ± 645.45 |               |                  | 74995.00 ± 41049.76 | 74881.55 ± 41049.76 | 74996.25 ± 41049.86 |
| granite-4-1-8b-bf16 |   tg256 (c20) |   25.97 ± 0.25 |     2.31 ± 0.86 | 100.00 ± 0.00 |      7.17 ± 1.91 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-09 07:51:20 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
