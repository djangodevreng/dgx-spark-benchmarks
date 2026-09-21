# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-09-18 18:12:16
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model             |          test |   t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:------------------|--------------:|--------------:|----------------:|--------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| qwen3.8-27b-nvfp4 | pp25000 (c20) | 752.82 ± 0.41 | 132.93 ± 155.79 |               |                  | 316830.08 ± 173762.44 | 316688.59 ± 173762.44 | 316832.81 ± 173762.32 |
| qwen3.8-27b-nvfp4 |   tg256 (c20) |   8.43 ± 0.02 |     1.47 ± 1.62 | 124.67 ± 0.47 |      8.50 ± 1.87 |                       |                       |                       |

llama-benchy (0.4.0)
date: 2026-09-18 17:29:42 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
