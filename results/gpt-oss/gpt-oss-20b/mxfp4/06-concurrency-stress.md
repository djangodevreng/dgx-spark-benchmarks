# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-14 12:46:51
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model             |          test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------|--------------:|-----------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gpt-oss-20b-mxfp4 | pp25000 (c20) | 4219.88 ± 348.97 | 811.38 ± 945.29 |               |                  | 50053.74 ± 27117.99 | 49981.45 ± 27117.99 | 55410.77 ± 27669.16 |
| gpt-oss-20b-mxfp4 |   tg256 (c20) |     47.51 ± 0.41 |     5.76 ± 3.47 | 290.00 ± 7.07 |     17.78 ± 4.57 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-14 12:39:23 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
