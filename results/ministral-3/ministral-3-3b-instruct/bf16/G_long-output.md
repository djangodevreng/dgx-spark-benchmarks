# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-07 15:49:38
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |         t/s (total) |           t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|--------------------:|--------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| ministral-3-3b-instruct-bf16 |   pp256 (c1) | 23411.13 ± 27775.39 | 23411.13 ± 27775.39 |               |                  |  79.11 ± 35.32 |  48.52 ± 35.32 |   79.11 ± 35.32 |
| ministral-3-3b-instruct-bf16 |  tg4096 (c1) |        51.61 ± 0.07 |        51.61 ± 0.07 |  52.00 ± 0.00 |     52.00 ± 0.00 |                |                |                 |
| ministral-3-3b-instruct-bf16 |   pp256 (c5) |   9783.83 ± 1264.80 |    2976.52 ± 783.71 |               |                  | 116.15 ± 22.17 |  85.57 ± 22.17 |  116.15 ± 22.17 |
| ministral-3-3b-instruct-bf16 |  tg4096 (c5) |      146.75 ± 39.57 |        53.65 ± 0.69 | 275.67 ± 0.94 |     55.13 ± 0.34 |                |                |                 |
| ministral-3-3b-instruct-bf16 |  pp256 (c10) |  12229.44 ± 1526.27 |   1757.33 ± 1015.69 |               |                  | 185.29 ± 39.65 | 154.71 ± 39.65 |  185.29 ± 39.65 |
| ministral-3-3b-instruct-bf16 | tg4096 (c10) |      340.37 ± 35.07 |        52.55 ± 0.31 | 540.00 ± 0.00 |     54.30 ± 0.46 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-07 15:46:15 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
