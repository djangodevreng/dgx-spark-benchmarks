# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-08 01:15:02
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                   |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-30b-fp8 | pp25000 (c20) | 8173.67 ± 34.57 | 1386.57 ± 1585.15 |               |                  | 29327.41 ± 15760.46 | 29244.64 ± 15760.46 | 29328.29 ± 15760.86 |
| nemotron-3-nano-30b-fp8 |   tg256 (c20) |    67.55 ± 0.09 |       5.93 ± 2.09 | 220.00 ± 0.00 |     14.47 ± 3.68 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-08 01:09:44 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
