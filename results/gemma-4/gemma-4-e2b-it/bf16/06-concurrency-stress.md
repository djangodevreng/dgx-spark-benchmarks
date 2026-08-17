# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-17 06:17:15
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-e2b-it-bf16 | pp25000 (c20) | 5588.88 ± 3.44 | 976.80 ± 1160.69 |               |                  | 42853.94 ± 23256.49 | 42813.68 ± 23256.49 | 42854.68 ± 23256.43 |
| gemma-4-e2b-it-bf16 |   tg256 (c20) |   58.85 ± 0.13 |      7.71 ± 5.73 | 500.00 ± 0.00 |     29.03 ± 3.61 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-17 06:11:11 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
