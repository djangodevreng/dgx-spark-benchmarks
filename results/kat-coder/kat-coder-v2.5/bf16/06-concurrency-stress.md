# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-13 17:42:59
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model kat-coder-v2-5-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| kat-coder-v2-5-bf16 | pp25000 (c20) | 4482.25 ± 2.87 | 748.13 ± 844.91 |               |                  | 54141.92 ± 28974.53 | 54027.30 ± 28974.53 | 54142.85 ± 28974.88 |
| kat-coder-v2-5-bf16 |   tg256 (c20) |   37.90 ± 0.38 |     3.50 ± 1.36 | 140.00 ± 0.00 |     10.05 ± 3.02 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-13 17:33:40 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
