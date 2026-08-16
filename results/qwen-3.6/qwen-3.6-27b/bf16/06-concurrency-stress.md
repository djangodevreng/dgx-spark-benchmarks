# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-14 02:57:10
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model            |          test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:-----------------|--------------:|---------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| qwen3.6-27b-bf16 | pp25000 (c20) | 1028.82 ± 0.50 | 182.03 ± 211.35 |              |                  | 231009.42 ± 127007.02 | 230756.88 ± 127007.02 | 231011.08 ± 127007.12 |
| qwen3.6-27b-bf16 |   tg256 (c20) |   10.33 ± 0.01 |     1.26 ± 0.73 | 65.67 ± 0.47 |      4.05 ± 0.67 |                       |                       |                       |

llama-benchy (0.4.0)
date: 2026-08-14 02:22:14 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
