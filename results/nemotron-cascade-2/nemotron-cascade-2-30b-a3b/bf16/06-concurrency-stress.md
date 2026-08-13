# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-09 12:15:17
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-cascade-2-30b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                       |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-cascade-2-30b-bf16 | pp25000 (c20) | 6654.00 ± 8.52 | 1160.95 ± 1369.26 |               |                  | 35918.51 ± 19475.65 | 35744.72 ± 19475.65 | 35919.40 ± 19475.90 |
| nemotron-cascade-2-30b-bf16 |   tg256 (c20) |   49.43 ± 0.10 |       4.00 ± 1.14 | 140.00 ± 0.00 |      9.40 ± 2.73 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-09 12:08:05 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
