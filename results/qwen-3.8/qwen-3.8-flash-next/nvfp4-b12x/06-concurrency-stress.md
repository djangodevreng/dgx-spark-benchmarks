# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-10-18 15:53:29
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-flash-next --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model              |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:-------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| qwen3.8-flash-next | pp25000 (c20) | 2019.72 ± 4.14 | 361.84 ± 407.73 |               |                  | 114768.71 ± 63894.85 | 114597.22 ± 63894.85 | 114771.11 ± 63895.28 |
| qwen3.8-flash-next |   tg256 (c20) |   22.13 ± 0.05 |     3.44 ± 3.15 | 175.67 ± 3.77 |     18.95 ± 6.62 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-10-18 15:37:13 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
