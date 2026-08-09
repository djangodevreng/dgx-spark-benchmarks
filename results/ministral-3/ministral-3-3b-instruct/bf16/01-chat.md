# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-09 00:23:07
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |        t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|-------------------:|-----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| ministral-3-3b-instruct-bf16 |  pp1024 (c1) |   3024.60 ± 568.92 | 3024.60 ± 568.92 |               |                  |  363.69 ± 34.01 |  319.82 ± 34.01 |  363.69 ± 34.01 |
| ministral-3-3b-instruct-bf16 |  tg1024 (c1) |       52.04 ± 0.20 |     52.04 ± 0.20 |  53.00 ± 0.00 |     53.00 ± 0.00 |                 |                 |                 |
| ministral-3-3b-instruct-bf16 |  pp1024 (c5) |    6211.62 ± 96.49 | 1412.59 ± 162.43 |               |                  |  700.20 ± 73.44 |  656.33 ± 73.44 |  700.20 ± 73.44 |
| ministral-3-3b-instruct-bf16 |  tg1024 (c5) |      194.51 ± 5.06 |     49.29 ± 0.46 | 255.00 ± 0.00 |     51.67 ± 0.70 |                 |                 |                 |
| ministral-3-3b-instruct-bf16 | pp1024 (c10) | 10083.28 ± 1230.71 | 1217.52 ± 457.88 |               |                  | 863.67 ± 182.28 | 819.80 ± 182.28 | 863.67 ± 182.28 |
| ministral-3-3b-instruct-bf16 | tg1024 (c10) |      356.50 ± 9.72 |     42.31 ± 0.63 | 450.00 ± 0.00 |     45.80 ± 1.96 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-09 00:19:17 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
