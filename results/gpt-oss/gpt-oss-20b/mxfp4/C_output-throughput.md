# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-06-26 10:05:37
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|------------------:|------------------:|---------------:|-----------------:|----------------:|----------------:|----------------:|
| gpt-oss-20b-mxfp4 |  pp1024 (c1) | 10876.85 ± 895.64 | 10876.85 ± 895.64 |                |                  |   158.04 ± 9.71 |    85.87 ± 9.71 |   225.11 ± 9.90 |
| gpt-oss-20b-mxfp4 |  tg1024 (c1) |      45.28 ± 0.23 |      45.28 ± 0.23 |   46.00 ± 0.00 |     46.00 ± 0.00 |                 |                 |                 |
| gpt-oss-20b-mxfp4 |  pp1024 (c5) |    6700.97 ± 0.00 | 3411.77 ± 3402.48 |                |                  | 506.94 ± 173.66 | 438.47 ± 171.76 |  674.18 ± 10.62 |
| gpt-oss-20b-mxfp4 |  tg1024 (c5) |     141.82 ± 0.00 |      33.85 ± 1.96 |  155.00 ± 0.00 |     35.80 ± 2.40 |                 |                 |                 |
| gpt-oss-20b-mxfp4 | pp1024 (c10) |  7724.94 ± 178.29 | 1721.21 ± 2053.26 |                |                  | 905.93 ± 318.98 | 830.35 ± 319.17 | 1197.22 ± 20.33 |
| gpt-oss-20b-mxfp4 | tg1024 (c10) |    172.59 ± 43.66 |      25.58 ± 1.04 | 198.67 ± 58.45 |     27.09 ± 1.44 |                 |                 |                 |

llama-benchy (0.3.8)
date: 2026-06-26 09:59:49 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
