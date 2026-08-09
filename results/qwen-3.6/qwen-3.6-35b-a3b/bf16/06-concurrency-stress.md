# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-08 13:48:34
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-bf16 | pp25000 (c20) | 3215.60 ± 0.36 | 573.42 ± 671.89 |               |                  | 73973.55 ± 40708.63 | 73864.28 ± 40708.63 | 73975.62 ± 40708.67 |
| qwen3.6-35b-a3b-bf16 |   tg256 (c20) |   31.28 ± 0.03 |     3.56 ± 1.85 | 145.00 ± 0.00 |     11.70 ± 5.12 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-08 13:37:06 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
