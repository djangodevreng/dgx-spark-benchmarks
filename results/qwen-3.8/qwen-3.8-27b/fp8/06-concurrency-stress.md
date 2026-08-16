# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-16 04:21:41
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |   t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:----------------|--------------:|--------------:|----------------:|--------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| qwen3.8-27b-fp8 | pp25000 (c20) | 582.63 ± 0.11 | 101.46 ± 116.45 |               |                  | 409504.42 ± 223999.03 | 409344.75 ± 223999.03 | 409506.99 ± 223998.81 |
| qwen3.8-27b-fp8 |   tg256 (c20) |   6.53 ± 0.02 |     1.14 ± 1.24 | 100.00 ± 0.00 |      6.47 ± 1.02 |                       |                       |                       |

llama-benchy (0.4.0)
date: 2026-08-16 03:26:32 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
