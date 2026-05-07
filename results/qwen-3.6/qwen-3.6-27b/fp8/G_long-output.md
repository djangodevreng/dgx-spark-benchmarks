# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-04 16:17:16
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|-----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-27b-fp8 |   pp256 (c1) | 3440.25 ± 505.09 | 3440.25 ± 505.09 |              |                  |    225.50 ± 12.99 |     70.77 ± 12.99 |    225.50 ± 12.99 |
| qwen3.6-27b-fp8 |  tg4096 (c1) |      7.80 ± 0.01 |      7.80 ± 0.01 |  8.67 ± 0.47 |      8.67 ± 0.47 |                   |                   |                   |
| qwen3.6-27b-fp8 |   pp256 (c5) | 1332.54 ± 131.72 |  385.73 ± 125.83 |              |                  |   816.95 ± 164.74 |   662.22 ± 164.74 |   816.95 ± 164.74 |
| qwen3.6-27b-fp8 |  tg4096 (c5) |     26.38 ± 2.48 |      7.57 ± 0.04 | 40.00 ± 0.00 |      8.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-fp8 |  pp256 (c10) | 1269.05 ± 503.51 |   174.65 ± 91.78 |              |                  | 2087.75 ± 1288.56 | 1933.02 ± 1288.56 | 2087.75 ± 1288.56 |
| qwen3.6-27b-fp8 | tg4096 (c10) |     46.46 ± 4.96 |      7.19 ± 0.11 | 80.00 ± 0.00 |      8.03 ± 0.18 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-04 14:59:44 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
