# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-07 15:32:26
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| ministral-3-3b-instruct-bf16 |  pp1024 (c1) | 20605.86 ± 4224.25 | 20605.86 ± 4224.25 |               |                  |    80.57 ± 9.22 |    44.93 ± 9.22 |    80.57 ± 9.22 |
| ministral-3-3b-instruct-bf16 |  tg1024 (c1) |       51.19 ± 0.01 |       51.19 ± 0.01 |  52.00 ± 0.00 |     52.00 ± 0.00 |                 |                 |                 |
| ministral-3-3b-instruct-bf16 |  pp1024 (c5) |  16248.78 ± 247.54 |  6742.52 ± 6027.31 |               |                  |  246.53 ± 80.87 |  210.89 ± 80.87 |  246.53 ± 80.87 |
| ministral-3-3b-instruct-bf16 |  tg1024 (c5) |     214.89 ± 22.71 |       51.33 ± 0.49 | 265.00 ± 0.00 |     53.27 ± 0.44 |                 |                 |                 |
| ministral-3-3b-instruct-bf16 | pp1024 (c10) |  16716.66 ± 302.76 |  3661.48 ± 5476.84 |               |                  | 490.58 ± 136.29 | 454.93 ± 136.29 | 490.58 ± 136.29 |
| ministral-3-3b-instruct-bf16 | tg1024 (c10) |     338.72 ± 38.66 |       48.68 ± 0.68 | 503.00 ± 4.24 |     51.40 ± 1.40 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-07 15:29:43 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
