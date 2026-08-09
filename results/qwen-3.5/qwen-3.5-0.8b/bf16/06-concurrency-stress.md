# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-07 09:35:20
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model             |          test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------|--------------:|-----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.5-0.8b-bf16 | pp25000 (c20) | 20262.35 ± 18.36 | 3773.25 ± 4501.36 |               |                  | 11496.64 ± 6470.44 | 11475.58 ± 6470.44 | 11499.05 ± 6470.51 |
| qwen3.5-0.8b-bf16 |   tg256 (c20) |    195.74 ± 3.40 |     22.56 ± 12.46 | 819.00 ± 1.41 |    58.70 ± 16.02 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-07 09:33:30 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
