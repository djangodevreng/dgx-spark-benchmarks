# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-06 04:36:00
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                        |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-omni-30b-fp8 | pp25000 (c20) | 8884.14 ± 12.59 | 1532.61 ± 1776.32 |               |                  | 26828.30 ± 14469.96 | 26753.43 ± 14469.96 | 26830.53 ± 14470.09 |
| nemotron-3-nano-omni-30b-fp8 |   tg256 (c20) |    70.65 ± 1.46 |       6.28 ± 2.21 | 240.00 ± 0.00 |     15.58 ± 3.79 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-06 04:31:07 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
