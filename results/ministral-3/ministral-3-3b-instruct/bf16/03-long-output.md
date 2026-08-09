# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-09 00:35:05
**Profile:** bf16
**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-3b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| ministral-3-3b-instruct-bf16 |   pp256 (c1) | 15188.37 ± 627.86 | 15188.37 ± 627.86 |               |                  |   45.99 ± 0.20 |   15.42 ± 0.20 |    45.99 ± 0.20 |
| ministral-3-3b-instruct-bf16 |  tg4096 (c1) |      52.43 ± 0.10 |      52.43 ± 0.10 |  54.00 ± 0.00 |     54.00 ± 0.00 |                |                |                 |
| ministral-3-3b-instruct-bf16 |   pp256 (c5) |  3362.47 ± 470.38 |   761.01 ± 118.61 |               |                  | 344.16 ± 45.03 | 313.60 ± 45.03 |  344.16 ± 45.03 |
| ministral-3-3b-instruct-bf16 |  tg4096 (c5) |     159.38 ± 8.10 |      53.62 ± 0.48 | 276.67 ± 2.36 |     55.33 ± 0.47 |                |                |                 |
| ministral-3-3b-instruct-bf16 |  pp256 (c10) |  5008.19 ± 195.58 |    551.65 ± 64.36 |               |                  | 460.97 ± 29.70 | 430.40 ± 29.70 |  460.97 ± 29.70 |
| ministral-3-3b-instruct-bf16 | tg4096 (c10) |    238.93 ± 69.00 |      50.17 ± 0.62 | 523.33 ± 4.71 |     52.80 ± 0.91 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-09 00:30:36 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
