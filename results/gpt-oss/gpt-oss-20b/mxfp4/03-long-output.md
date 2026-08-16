# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-14 12:19:41
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |       e2e_ttft (ms) |
|:------------------|-------------:|------------------:|------------------:|---------------:|-----------------:|---------------:|---------------:|--------------------:|
| gpt-oss-20b-mxfp4 |   pp256 (c1) |  9894.43 ± 709.47 |  9894.43 ± 709.47 |                |                  |   92.39 ± 1.60 |   20.00 ± 1.60 |       157.37 ± 1.41 |
| gpt-oss-20b-mxfp4 |  tg4096 (c1) |      46.07 ± 0.32 |      46.07 ± 0.32 |   48.00 ± 0.00 |     48.00 ± 0.00 |                |                |                     |
| gpt-oss-20b-mxfp4 |   pp256 (c5) | 2061.07 ± 1452.48 | 2516.01 ± 1635.37 |                |                  | 177.72 ± 49.28 | 108.93 ± 52.01 | 19514.11 ± 45052.28 |
| gpt-oss-20b-mxfp4 |  tg4096 (c5) |     95.58 ± 67.55 |      26.07 ± 8.23 | 107.67 ± 71.90 |    25.00 ± 12.29 |                |                |                     |
| gpt-oss-20b-mxfp4 |  pp256 (c10) | 3001.61 ± 2113.85 | 1434.26 ± 1393.80 |                |                  | 287.29 ± 89.89 | 214.90 ± 89.89 |  6870.22 ± 28707.67 |
| gpt-oss-20b-mxfp4 | tg4096 (c10) |    204.02 ± 34.13 |      23.56 ± 4.53 | 252.00 ± 25.46 |     25.47 ± 6.55 |                |                |                     |

llama-benchy (0.4.0)
date: 2026-08-14 11:58:48 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
