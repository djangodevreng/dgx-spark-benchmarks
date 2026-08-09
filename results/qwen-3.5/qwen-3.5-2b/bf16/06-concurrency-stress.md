# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-07 14:52:49
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |      t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|--------------:|-----------------:|------------------:|---------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.5-2b-bf16 | pp25000 (c20) | 13159.56 ± 49.55 | 2393.66 ± 2810.47 |                |                  | 17847.35 ± 9925.95 | 17805.88 ± 9925.95 | 17847.94 ± 9925.80 |
| qwen3.5-2b-bf16 |   tg256 (c20) |    118.21 ± 1.85 |      14.29 ± 7.80 | 540.67 ± 13.20 |    36.15 ± 10.19 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-07 14:50:00 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
