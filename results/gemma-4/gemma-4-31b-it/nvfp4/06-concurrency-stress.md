# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-16 22:37:48
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model             |          test |   t/s (total) |      t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:------------------|--------------:|--------------:|---------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| gemma-4-31b-nvfp4 | pp25000 (c20) | 575.37 ± 0.06 | 96.14 ± 108.58 |              |                  | 419863.36 ± 225668.39 | 419659.21 ± 225668.39 | 419865.11 ± 225668.61 |
| gemma-4-31b-nvfp4 |   tg256 (c20) |   6.25 ± 0.00 |    0.90 ± 0.76 | 80.00 ± 0.00 |      5.10 ± 1.09 |                       |                       |                       |

llama-benchy (0.4.0)
date: 2026-08-16 21:40:26 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
