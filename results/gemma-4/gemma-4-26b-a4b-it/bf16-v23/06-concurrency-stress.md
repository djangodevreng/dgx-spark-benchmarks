# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-06 09:31:40
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b | pp25000 (c20) | 3110.01 ± 5.33 | 546.72 ± 651.93 |               |                  | 76759.65 ± 41792.23 | 76640.25 ± 41792.23 | 76760.63 ± 41792.39 |
| gemma-4-26b-a4b |   tg256 (c20) |   28.54 ± 0.35 |     2.88 ± 1.35 | 140.00 ± 0.00 |      9.72 ± 2.53 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-06 09:19:19 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
