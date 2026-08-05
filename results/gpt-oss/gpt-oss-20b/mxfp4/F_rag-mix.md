# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-06-26 10:25:36
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model             |         test |     t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------|-------------:|----------------:|------------------:|---------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gpt-oss-20b-mxfp4 |  pp8192 (c5) | 6843.70 ± 40.68 | 3757.41 ± 2019.68 |                |                  |  3369.77 ± 1493.62 |  2540.05 ± 1255.26 |   5096.93 ± 313.46 |
| gpt-oss-20b-mxfp4 |   tg512 (c5) |   88.89 ± 13.73 |      27.44 ± 0.57 |  98.00 ± 15.56 |     29.40 ± 0.49 |                    |                    |                    |
| gpt-oss-20b-mxfp4 | pp8192 (c10) | 6913.70 ± 54.75 | 2062.16 ± 1860.79 |                |                  |  6203.22 ± 3133.97 |  5663.55 ± 2954.82 |  8459.23 ± 2227.60 |
| gpt-oss-20b-mxfp4 |  tg512 (c10) |  163.86 ± 17.26 |      21.71 ± 1.85 | 225.00 ± 20.41 |     25.04 ± 0.19 |                    |                    |                    |
| gpt-oss-20b-mxfp4 | pp8192 (c20) | 6983.89 ± 26.98 | 1229.65 ± 1420.69 |                |                  | 11512.33 ± 6055.57 | 10611.55 ± 5635.10 | 13988.16 ± 5321.19 |
| gpt-oss-20b-mxfp4 |  tg512 (c20) |   199.70 ± 6.41 |      15.07 ± 2.42 | 344.67 ± 12.39 |     20.36 ± 1.10 |                    |                    |                    |

llama-benchy (0.3.8)
date: 2026-06-26 10:18:35 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
