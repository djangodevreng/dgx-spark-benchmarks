# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-06 20:03:41
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model       |          test |   t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:------------|--------------:|--------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| gemma-4-31b | pp25000 (c20) | 651.25 ± 0.64 | 114.05 ± 136.05 |              |                  | 367913.01 ± 199785.97 | 367537.07 ± 199785.97 | 367913.71 ± 199786.30 |
| gemma-4-31b |   tg256 (c20) |   6.40 ± 0.11 |     0.77 ± 0.49 | 59.00 ± 1.41 |      3.37 ± 0.58 |                       |                       |                       |

llama-benchy (0.4.0)
date: 2026-08-06 19:09:34 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
