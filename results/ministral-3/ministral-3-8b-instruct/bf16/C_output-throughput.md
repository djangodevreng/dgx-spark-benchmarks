# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-07 17:34:57
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| ministral-3-8b-instruct-bf16 |  pp1024 (c1) | 10713.15 ± 1592.68 | 10713.15 ± 1592.68 |               |                  |  155.89 ± 17.25 |   86.39 ± 17.25 |  155.89 ± 17.25 |
| ministral-3-8b-instruct-bf16 |  tg1024 (c1) |       21.83 ± 0.16 |       21.83 ± 0.16 |  23.00 ± 0.00 |     23.00 ± 0.00 |                 |                 |                 |
| ministral-3-8b-instruct-bf16 |  pp1024 (c5) |   8049.02 ± 153.54 |  3653.18 ± 3701.64 |               |                  | 495.10 ± 168.72 | 425.59 ± 168.72 | 495.10 ± 168.72 |
| ministral-3-8b-instruct-bf16 |  tg1024 (c5) |     102.83 ± 11.12 |       23.49 ± 0.24 | 125.00 ± 0.00 |     25.00 ± 0.00 |                 |                 |                 |
| ministral-3-8b-instruct-bf16 | pp1024 (c10) |   8511.82 ± 116.44 |  1929.09 ± 2999.17 |               |                  | 961.29 ± 269.23 | 891.79 ± 269.23 | 961.29 ± 269.23 |
| ministral-3-8b-instruct-bf16 | tg1024 (c10) |     160.17 ± 18.71 |       22.75 ± 0.18 | 240.00 ± 0.00 |     24.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-07 17:28:24 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
