# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-06-26 10:46:45
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|------------------:|------------------:|---------------:|-----------------:|---------------:|---------------:|----------------:|
| gpt-oss-20b-mxfp4 |   pp256 (c1) | 8547.91 ± 1027.75 | 8547.91 ± 1027.75 |                |                  |   93.84 ± 2.85 |   22.57 ± 2.85 |   161.61 ± 2.85 |
| gpt-oss-20b-mxfp4 |  tg4096 (c1) |      45.42 ± 0.11 |      45.42 ± 0.11 |   46.67 ± 0.47 |     46.67 ± 0.47 |                |                |                 |
| gpt-oss-20b-mxfp4 |   pp256 (c5) |  3148.38 ± 122.46 | 5796.67 ± 7525.00 |                |                  | 190.82 ± 53.89 | 110.35 ± 60.35 |  303.48 ± 13.93 |
| gpt-oss-20b-mxfp4 |  tg4096 (c5) |    111.58 ± 24.73 |      33.37 ± 3.23 | 119.00 ± 27.53 |     35.81 ± 3.66 |                |                |                 |
| gpt-oss-20b-mxfp4 |  pp256 (c10) |  4333.94 ± 246.30 | 2072.20 ± 3630.75 |                |                  | 319.26 ± 97.71 | 242.64 ± 97.12 |  445.34 ± 18.76 |
| gpt-oss-20b-mxfp4 | tg4096 (c10) |    135.25 ± 75.30 |      25.30 ± 2.22 | 159.33 ± 75.44 |     27.83 ± 2.81 |                |                |                 |

llama-benchy (0.3.8)
date: 2026-06-26 10:25:37 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
