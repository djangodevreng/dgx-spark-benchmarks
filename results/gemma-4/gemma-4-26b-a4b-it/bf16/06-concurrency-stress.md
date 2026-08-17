# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-16 13:21:46
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b-bf16 | pp25000 (c20) | 3089.31 ± 1.87 | 541.72 ± 646.21 |               |                  | 77387.96 ± 42013.67 | 77268.86 ± 42013.67 | 77389.54 ± 42014.07 |
| gemma-4-26b-a4b-bf16 |   tg256 (c20) |   28.66 ± 0.06 |     2.89 ± 1.38 | 140.00 ± 0.00 |      9.63 ± 2.59 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-16 13:09:20 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
