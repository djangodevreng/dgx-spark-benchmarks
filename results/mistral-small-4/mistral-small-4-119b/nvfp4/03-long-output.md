# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-13 10:31:33
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model mistral-small-4-119b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                      |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:---------------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| mistral-small-4-119b-nvfp4 |   pp256 (c1) | 1130.16 ± 19.55 | 1130.16 ± 19.55 |               |                  |  334.51 ± 4.37 |  222.67 ± 4.37 |   334.51 ± 4.37 |
| mistral-small-4-119b-nvfp4 |  tg4096 (c1) |    30.88 ± 0.08 |    30.88 ± 0.08 |  32.00 ± 0.00 |     32.00 ± 0.00 |                |                |                 |
| mistral-small-4-119b-nvfp4 |   pp256 (c5) | 2402.50 ± 42.78 |  622.28 ± 37.64 |               |                  |  492.46 ± 4.18 |  380.62 ± 4.18 |   492.46 ± 4.18 |
| mistral-small-4-119b-nvfp4 |  tg4096 (c5) |    48.89 ± 8.93 |    18.31 ± 3.63 |  81.67 ± 2.36 |     22.14 ± 5.81 |                |                |                 |
| mistral-small-4-119b-nvfp4 |  pp256 (c10) | 3321.26 ± 24.66 |  395.97 ± 24.82 |               |                  | 696.87 ± 12.23 | 585.02 ± 12.23 |  696.87 ± 12.23 |
| mistral-small-4-119b-nvfp4 | tg4096 (c10) |    82.87 ± 2.97 |    12.17 ± 1.33 | 119.33 ± 0.94 |     17.09 ± 6.09 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-13 10:27:08 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
