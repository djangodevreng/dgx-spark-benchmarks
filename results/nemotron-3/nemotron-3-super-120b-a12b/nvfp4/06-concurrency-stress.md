# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-15 07:15:51
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model            |          test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:-----------------|--------------:|---------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| nemotron-3-super | pp25000 (c20) | 1192.35 ± 2.15 | 209.32 ± 240.34 |              |                  | 198113.78 ± 109004.70 | 197909.79 ± 109004.70 | 198114.97 ± 109004.73 |
| nemotron-3-super |   tg256 (c20) |   13.04 ± 0.15 |     2.59 ± 2.41 | 88.00 ± 4.97 |      9.02 ± 7.24 |                       |                       |                       |

llama-benchy (0.4.0)
date: 2026-08-15 06:48:53 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
