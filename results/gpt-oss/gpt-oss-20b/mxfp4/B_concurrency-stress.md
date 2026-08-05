# Run B — 25k context, c=5/10/20

**Generated:** 2026-06-26 09:59:47
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model             |          test |     t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------|--------------:|----------------:|------------------:|---------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gpt-oss-20b-mxfp4 |  pp25000 (c5) | 4696.87 ± 65.14 | 2192.58 ± 1279.84 |                |                  |  14682.04 ± 6525.30 |  13228.90 ± 5898.03 |  17900.21 ± 5219.85 |
| gpt-oss-20b-mxfp4 |    tg256 (c5) |    46.88 ± 4.51 |      18.25 ± 5.94 | 118.00 ± 10.71 |     27.77 ± 1.85 |                     |                     |                     |
| gpt-oss-20b-mxfp4 | pp25000 (c10) | 4665.58 ± 20.34 | 1395.85 ± 1161.21 |                |                  | 26681.78 ± 13549.65 | 24289.42 ± 12250.18 | 29363.03 ± 12058.39 |
| gpt-oss-20b-mxfp4 |   tg256 (c10) |    43.60 ± 2.04 |       9.89 ± 4.59 |  181.00 ± 6.16 |     22.04 ± 1.77 |                     |                     |                     |
| gpt-oss-20b-mxfp4 | pp25000 (c20) | 4635.17 ± 10.28 |   833.43 ± 946.94 |                |                  | 50483.26 ± 27450.16 | 48039.88 ± 26086.68 | 53214.39 ± 26030.93 |
| gpt-oss-20b-mxfp4 |   tg256 (c20) |    45.87 ± 1.08 |       5.55 ± 3.36 |  284.67 ± 0.47 |     18.54 ± 3.49 |                     |                     |                     |

llama-benchy (0.3.8)
date: 2026-06-26 09:46:00 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
