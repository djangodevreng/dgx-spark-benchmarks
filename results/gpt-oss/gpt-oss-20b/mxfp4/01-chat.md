# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-14 11:51:54
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|------------------:|------------------:|---------------:|-----------------:|----------------:|----------------:|----------------:|
| gpt-oss-20b-mxfp4 |  pp1024 (c1) | 11792.96 ± 265.41 | 11792.96 ± 265.41 |                |                  |   153.26 ± 4.35 |    74.98 ± 4.35 |   216.94 ± 4.56 |
| gpt-oss-20b-mxfp4 |  tg1024 (c1) |      46.47 ± 0.35 |      46.47 ± 0.35 |   48.00 ± 0.00 |     48.00 ± 0.00 |                 |                 |                 |
| gpt-oss-20b-mxfp4 |  pp1024 (c5) |   6739.34 ± 26.55 | 2900.23 ± 2600.17 |                |                  | 491.64 ± 168.85 | 436.72 ± 149.53 |  671.01 ± 12.66 |
| gpt-oss-20b-mxfp4 |  tg1024 (c5) |    129.65 ± 17.18 |      30.34 ± 1.96 | 144.67 ± 12.04 |     33.29 ± 2.99 |                 |                 |                 |
| gpt-oss-20b-mxfp4 | pp1024 (c10) |  7705.55 ± 147.31 | 1624.91 ± 1938.48 |                |                  | 878.16 ± 335.21 | 842.98 ± 304.19 | 1189.77 ± 20.56 |
| gpt-oss-20b-mxfp4 | tg1024 (c10) |    180.39 ± 44.74 |      24.06 ± 6.36 | 222.00 ± 36.99 |     29.59 ± 6.65 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-14 11:45:39 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
