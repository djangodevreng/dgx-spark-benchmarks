# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-09 04:23:26
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                    |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-------------------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-30b-bf16 | pp25000 (c20) | 6534.20 ± 4.64 | 1139.50 ± 1342.37 |               |                  | 36553.92 ± 19830.18 | 36421.59 ± 19830.18 | 36554.56 ± 19830.35 |
| nemotron-3-nano-30b-bf16 |   tg256 (c20) |   48.27 ± 0.12 |       3.89 ± 1.10 | 140.00 ± 0.00 |      9.28 ± 2.78 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-09 04:16:04 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
