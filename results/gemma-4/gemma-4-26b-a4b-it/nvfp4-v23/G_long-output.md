# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-06-23 02:42:36
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-26b-a4b-nvfp4 |   pp256 (c1) | 4304.87 ± 183.12 | 4304.87 ± 183.12 |               |                  |  114.75 ± 2.92 |   51.23 ± 2.92 |   114.75 ± 2.92 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c1) |     31.01 ± 0.01 |     31.01 ± 0.01 |  32.00 ± 0.00 |     32.00 ± 0.00 |                |                |                 |
| gemma-4-26b-a4b-nvfp4 |   pp256 (c5) | 4967.71 ± 170.40 | 1688.58 ± 598.81 |               |                  | 215.18 ± 36.50 | 151.66 ± 36.50 |  215.18 ± 36.50 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c5) |     96.45 ± 5.88 |     27.30 ± 1.11 | 136.67 ± 2.36 |     30.67 ± 2.60 |                |                |                 |
| gemma-4-26b-a4b-nvfp4 |  pp256 (c10) | 5837.79 ± 583.67 |  929.57 ± 971.14 |               |                  | 368.83 ± 54.97 | 305.31 ± 54.97 |  368.83 ± 54.97 |
| gemma-4-26b-a4b-nvfp4 | tg4096 (c10) |   120.96 ± 50.17 |     23.69 ± 1.65 | 233.00 ± 4.97 |     27.17 ± 3.71 |                |                |                 |

llama-benchy (0.3.8)
date: 2026-06-23 02:35:12 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
