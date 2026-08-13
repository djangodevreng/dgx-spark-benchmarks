# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-13 11:17:08
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model mistral-small-4-119b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                      |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| mistral-small-4-119b-nvfp4 | pp25000 (c20) | 3266.33 ± 3.11 | 548.55 ± 624.19 |               |                  | 73818.41 ± 39601.83 | 73703.94 ± 39601.83 | 73818.56 ± 39601.87 |
| mistral-small-4-119b-nvfp4 |   tg256 (c20) |   22.21 ± 0.36 |     2.56 ± 1.72 | 114.67 ± 1.70 |      9.53 ± 4.30 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-13 11:05:33 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
