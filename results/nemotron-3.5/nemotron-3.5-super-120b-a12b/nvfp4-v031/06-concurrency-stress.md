# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-10-17 23:21:54
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3.5-super --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model              |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:-------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| nemotron-3.5-super | pp25000 (c20) | 2258.24 ± 2.35 | 401.11 ± 474.22 |               |                  | 105011.23 ± 57558.72 | 104815.47 ± 57558.72 | 105011.90 ± 57558.75 |
| nemotron-3.5-super |   tg256 (c20) |   25.24 ± 0.06 |     5.28 ± 3.88 | 122.33 ± 4.19 |     12.22 ± 9.84 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-10-17 23:07:39 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
