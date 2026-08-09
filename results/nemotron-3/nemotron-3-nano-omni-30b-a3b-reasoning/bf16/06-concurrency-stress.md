# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-06 01:33:11
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                         |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-omni-30b-bf16 | pp25000 (c20) | 6370.44 ± 17.78 | 1137.19 ± 1351.63 |               |                  | 36919.12 ± 20261.22 | 36783.13 ± 20261.22 | 36921.54 ± 20260.89 |
| nemotron-3-nano-omni-30b-bf16 |   tg256 (c20) |    45.43 ± 0.89 |       3.70 ± 1.11 | 133.67 ± 8.96 |      9.27 ± 2.99 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-06 01:25:39 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
