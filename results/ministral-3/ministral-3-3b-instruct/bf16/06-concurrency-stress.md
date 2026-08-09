# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-09 01:00:55
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                        |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| ministral-3-3b-instruct-bf16 | pp25000 (c20) | 6959.45 ± 7.14 | 1467.23 ± 1832.15 |               |                  | 31186.76 ± 18617.27 | 31156.86 ± 18617.27 | 31186.76 ± 18617.27 |
| ministral-3-3b-instruct-bf16 |   tg256 (c20) |   44.34 ± 0.08 |       3.17 ± 0.71 | 103.67 ± 0.47 |      8.93 ± 3.90 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-09 00:53:02 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
