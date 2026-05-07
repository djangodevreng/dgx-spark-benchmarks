# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-05 16:55:16
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                  |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-4b-fp8 |  pp1024 (c1) | 12919.08 ± 1142.11 | 12919.08 ± 1142.11 |               |                  |   117.62 ± 9.01 |    72.85 ± 9.01 |   117.62 ± 9.01 |
| nemotron-3-nano-4b-fp8 |  tg1024 (c1) |       42.33 ± 0.09 |       42.33 ± 0.09 |  43.00 ± 0.00 |     43.00 ± 0.00 |                 |                 |                 |
| nemotron-3-nano-4b-fp8 |  pp1024 (c5) |   9865.25 ± 399.38 |  3416.27 ± 1723.13 |               |                  | 363.72 ± 104.37 | 318.96 ± 104.37 | 363.72 ± 104.37 |
| nemotron-3-nano-4b-fp8 |  tg1024 (c5) |      190.68 ± 5.84 |       39.83 ± 0.28 | 200.00 ± 0.00 |     41.60 ± 0.80 |                 |                 |                 |
| nemotron-3-nano-4b-fp8 | pp1024 (c10) |   10489.52 ± 14.77 |  2212.08 ± 1319.07 |               |                  | 588.27 ± 234.83 | 543.50 ± 234.83 | 588.27 ± 234.83 |
| nemotron-3-nano-4b-fp8 | tg1024 (c10) |     309.54 ± 12.82 |       35.10 ± 0.72 | 350.00 ± 0.00 |     37.13 ± 1.31 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-05 16:51:17 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
