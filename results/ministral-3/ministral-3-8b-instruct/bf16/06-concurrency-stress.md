# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-07 04:03:17
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                        |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| ministral-3-8b-instruct-bf16 | pp25000 (c20) | 5127.40 ± 8.14 | 923.79 ± 1098.77 |               |                  | 45791.72 ± 25329.02 | 45730.75 ± 25329.02 | 45792.18 ± 25329.33 |
| ministral-3-8b-instruct-bf16 |   tg256 (c20) |   40.99 ± 0.09 |      3.48 ± 1.17 | 131.00 ± 0.00 |      9.98 ± 3.29 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-07 03:54:40 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
