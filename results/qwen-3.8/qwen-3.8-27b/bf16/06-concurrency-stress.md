# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-15 18:19:05
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model            |          test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:-----------------|--------------:|---------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| qwen3.8-27b-bf16 | pp25000 (c20) | 1037.12 ± 0.12 | 185.16 ± 219.23 |              |                  | 228576.41 ± 125763.39 | 228192.78 ± 125763.39 | 228577.60 ± 125763.61 |
| qwen3.8-27b-bf16 |   tg256 (c20) |   10.40 ± 0.03 |     1.26 ± 0.73 | 66.00 ± 0.00 |      4.00 ± 0.63 |                       |                       |                       |

llama-benchy (0.4.0)
date: 2026-08-15 17:44:38 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
