# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-06 06:28:26
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                   |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-4b-bf16 | pp25000 (c20) | 6742.79 ± 6.96 | 1223.50 ± 1442.81 |               |                  | 34587.90 ± 19253.18 | 34523.55 ± 19253.18 | 34588.64 ± 19253.15 |
| nemotron-3-nano-4b-bf16 |   tg256 (c20) |   65.74 ± 0.18 |       7.49 ± 3.86 | 300.00 ± 0.00 |     20.63 ± 4.21 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-06 06:22:59 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
