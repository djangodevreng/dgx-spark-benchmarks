# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-12 09:57:06
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:----------------------|--------------:|---------------:|----------------:|-------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| muse-glimmer-30b-bf16 | pp25000 (c20) | 1412.05 ± 0.81 | 247.93 ± 293.43 |              |                  | 167972.77 ± 91473.94 | 167706.26 ± 91473.94 | 184705.37 ± 89918.65 |
| muse-glimmer-30b-bf16 |   tg256 (c20) |   13.77 ± 0.04 |     1.54 ± 0.82 | 80.00 ± 0.00 |      4.32 ± 0.47 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-08-12 09:30:21 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
