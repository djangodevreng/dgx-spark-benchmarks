# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-07 17:47:01
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.5-4b-bf16 | pp25000 (c20) | 5239.06 ± 1.34 | 978.54 ± 1186.88 |               |                  | 44647.77 ± 25058.68 | 44588.91 ± 25058.68 | 44648.88 ± 25058.86 |
| qwen3.5-4b-bf16 |   tg256 (c20) |   51.26 ± 0.03 |      5.94 ± 3.19 | 240.00 ± 0.00 |     16.98 ± 3.64 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-07 17:39:59 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
