# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-07 03:29:24
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| ministral-3-8b-instruct-bf16 |   pp256 (c1) |  3495.85 ± 656.63 |  3495.85 ± 656.63 |               |                  |  132.58 ± 14.57 |   73.30 ± 14.57 |  132.58 ± 14.57 |
| ministral-3-8b-instruct-bf16 |  tg4096 (c1) |      25.41 ± 0.04 |      25.41 ± 0.04 |  26.33 ± 0.47 |     26.33 ± 0.47 |                 |                 |                 |
| ministral-3-8b-instruct-bf16 |   pp256 (c5) | 3291.86 ± 1368.93 | 1149.87 ± 1409.68 |               |                  | 402.53 ± 149.56 | 343.24 ± 149.56 | 402.53 ± 149.56 |
| ministral-3-8b-instruct-bf16 |  tg4096 (c5) |     69.10 ± 18.89 |      25.84 ± 0.35 | 135.00 ± 0.00 |     27.00 ± 0.00 |                 |                 |                 |
| ministral-3-8b-instruct-bf16 |  pp256 (c10) |   3611.89 ± 36.89 |    398.08 ± 27.45 |               |                  |   647.33 ± 4.59 |   588.04 ± 4.59 |   647.33 ± 4.59 |
| ministral-3-8b-instruct-bf16 | tg4096 (c10) |     117.83 ± 7.95 |      25.27 ± 0.15 | 260.00 ± 0.00 |     26.20 ± 0.40 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 03:17:30 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
