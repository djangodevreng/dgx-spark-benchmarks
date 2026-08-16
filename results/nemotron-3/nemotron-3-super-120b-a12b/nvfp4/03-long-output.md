# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-15 05:40:07
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |     t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|--------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-super |   pp256 (c1) |  677.72 ± 6.11 | 677.72 ± 6.11 |               |                  |    572.71 ± 2.33 |    368.87 ± 2.33 |    572.71 ± 2.33 |
| nemotron-3-super |  tg4096 (c1) |   21.73 ± 0.65 |  21.73 ± 0.65 |  33.00 ± 1.63 |     33.00 ± 1.63 |                  |                  |                  |
| nemotron-3-super |   pp256 (c5) |  752.71 ± 9.26 | 179.40 ± 8.98 |               |                  |  1488.63 ± 85.79 |  1284.79 ± 85.79 |  1488.63 ± 85.79 |
| nemotron-3-super |  tg4096 (c5) |   42.58 ± 1.92 |  11.60 ± 1.71 |  79.67 ± 4.03 |     21.80 ± 5.99 |                  |                  |                  |
| nemotron-3-super |  pp256 (c10) | 878.92 ± 21.71 | 106.13 ± 7.85 |               |                  | 2396.02 ± 142.69 | 2192.18 ± 142.69 | 2396.02 ± 142.69 |
| nemotron-3-super | tg4096 (c10) |   60.10 ± 9.79 |   8.62 ± 1.50 | 124.67 ± 8.38 |     17.10 ± 5.33 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-15 05:08:44 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
