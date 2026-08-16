# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-13 14:32:44
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                     |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-30b-nvfp4 | pp25000 (c20) | 6229.68 ± 10.14 | 1071.07 ± 1254.73 |               |                  | 38513.84 ± 20820.88 | 38460.06 ± 20820.88 | 38514.61 ± 20821.10 |
| nemotron-3-nano-30b-nvfp4 |   tg256 (c20) |    60.81 ± 0.33 |       6.69 ± 3.74 | 340.00 ± 0.00 |     20.88 ± 4.11 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-13 14:26:50 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
