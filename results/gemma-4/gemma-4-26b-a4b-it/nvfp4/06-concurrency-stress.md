# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-16 16:34:18
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b-nvfp4 | pp25000 (c20) | 3212.41 ± 0.61 | 560.39 ± 661.41 |               |                  | 74373.63 ± 40385.02 | 74309.06 ± 40385.02 | 74374.51 ± 40385.28 |
| gemma-4-26b-a4b-nvfp4 |   tg256 (c20) |   32.57 ± 0.42 |     3.94 ± 2.60 | 233.33 ± 9.43 |     15.95 ± 3.69 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-16 16:23:26 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
