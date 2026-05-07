# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-05 04:26:46
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |     t/s (total) |      t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------|-------------:|----------------:|---------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-super |   pp256 (c1) |  681.80 ± 19.95 | 681.80 ± 19.95 |               |                  |    555.11 ± 3.89 |    356.52 ± 3.89 |    555.11 ± 3.89 |
| nemotron-3-super |  tg4096 (c1) |    23.18 ± 0.88 |   23.18 ± 0.88 |  34.00 ± 0.82 |     34.00 ± 0.82 |                  |                  |                  |
| nemotron-3-super |   pp256 (c5) | 951.17 ± 109.70 | 238.66 ± 34.31 |               |                  | 1202.04 ± 146.32 | 1003.45 ± 146.32 | 1202.04 ± 146.32 |
| nemotron-3-super |  tg4096 (c5) |    42.56 ± 4.27 |   12.01 ± 2.18 |  75.33 ± 2.49 |     22.07 ± 5.74 |                  |                  |                  |
| nemotron-3-super |  pp256 (c10) | 1034.47 ± 34.58 | 128.95 ± 16.64 |               |                  | 2050.60 ± 166.94 | 1852.00 ± 166.94 | 2050.60 ± 166.94 |
| nemotron-3-super | tg4096 (c10) |    60.64 ± 2.60 |    8.99 ± 1.11 | 132.00 ± 6.98 |     17.90 ± 5.35 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-05 04:05:44 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
