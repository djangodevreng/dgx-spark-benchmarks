# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-07 21:54:15
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.5-9b-bf16 | pp25000 (c20) | 3288.25 ± 4.03 | 610.11 ± 753.08 |               |                  | 71437.95 ± 39733.10 | 71346.86 ± 39733.10 | 71439.16 ± 39733.27 |
| qwen3.5-9b-bf16 |   tg256 (c20) |   32.35 ± 0.05 |     3.82 ± 2.07 | 163.00 ± 0.00 |     11.05 ± 1.78 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-07 21:43:07 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
