# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-07 14:12:10
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|------------------:|------------------:|---------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-2b-bf16 |  pp1024 (c1) | 26919.88 ± 895.79 | 26919.88 ± 895.79 |                |                  |    72.38 ± 0.86 |    33.87 ± 0.86 |    72.38 ± 0.86 |
| qwen3.5-2b-bf16 |  tg1024 (c1) |      43.46 ± 0.04 |      43.46 ± 0.04 |   44.33 ± 0.47 |     44.33 ± 0.47 |                 |                 |                 |
| qwen3.5-2b-bf16 |  pp1024 (c5) | 14774.73 ± 183.09 | 6305.44 ± 4351.85 |                |                  |  229.48 ± 74.78 |  190.96 ± 74.78 |  229.48 ± 74.78 |
| qwen3.5-2b-bf16 |  tg1024 (c5) |    131.32 ± 42.00 |      51.30 ± 2.29 | 256.33 ± 15.92 |     54.70 ± 0.81 |                 |                 |                 |
| qwen3.5-2b-bf16 | pp1024 (c10) | 15420.77 ± 180.02 | 3742.40 ± 3058.42 |                |                  | 392.51 ± 162.98 | 354.00 ± 162.98 | 392.51 ± 162.98 |
| qwen3.5-2b-bf16 | tg1024 (c10) |    329.26 ± 27.15 |      49.83 ± 2.01 |  506.67 ± 4.71 |     52.87 ± 1.52 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-07 14:09:18 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
