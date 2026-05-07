# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-05 13:10:06
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:---------------------|-------------:|-----------------:|----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.6-35b-a3b-bf16 |   pp256 (c1) |  1604.02 ± 31.22 | 1604.02 ± 31.22 |               |                  |   261.89 ± 7.90 |   149.19 ± 7.90 |   261.89 ± 7.90 |
| qwen3.6-35b-a3b-bf16 |  tg4096 (c1) |     30.37 ± 0.04 |    30.37 ± 0.04 |  31.00 ± 0.00 |     31.00 ± 0.00 |                 |                 |                 |
| qwen3.6-35b-a3b-bf16 |   pp256 (c5) | 2157.28 ± 378.04 | 671.25 ± 391.03 |               |                  | 532.37 ± 126.42 | 419.67 ± 126.42 | 532.37 ± 126.42 |
| qwen3.6-35b-a3b-bf16 |  tg4096 (c5) |     57.59 ± 2.25 |    14.91 ± 2.12 |  81.67 ± 2.36 |     22.67 ± 5.29 |                 |                 |                 |
| qwen3.6-35b-a3b-bf16 |  pp256 (c10) |  2752.27 ± 34.39 | 411.20 ± 128.87 |               |                  | 727.68 ± 146.62 | 614.98 ± 146.62 | 727.68 ± 146.62 |
| qwen3.6-35b-a3b-bf16 | tg4096 (c10) |     75.68 ± 1.35 |     9.95 ± 1.44 | 120.00 ± 0.00 |     16.63 ± 5.38 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-05 12:38:04 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
