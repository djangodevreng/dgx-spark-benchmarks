# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-04 23:07:37
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |        t/s (total) |          t/s (req) |       peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|-------------------:|-------------------:|---------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.5-0.8b-bf16 |  pp1024 (c1) | 43227.66 ± 3944.85 | 43227.66 ± 3944.85 |                |                  |   45.03 ± 2.95 |   21.16 ± 2.95 |    45.03 ± 2.95 |
| qwen3.5-0.8b-bf16 |  tg1024 (c1) |      109.93 ± 0.77 |      109.93 ± 0.77 |  112.23 ± 0.32 |    112.23 ± 0.32 |                |                |                 |
| qwen3.5-0.8b-bf16 |  pp1024 (c5) |  24425.28 ± 234.71 | 10015.08 ± 6075.57 |                |                  | 143.74 ± 46.13 | 119.88 ± 46.13 |  143.74 ± 46.13 |
| qwen3.5-0.8b-bf16 |  tg1024 (c5) |     421.36 ± 48.89 |      113.01 ± 2.57 | 547.67 ± 24.51 |    118.01 ± 3.67 |                |                |                 |
| qwen3.5-0.8b-bf16 | pp1024 (c10) |  23728.76 ± 584.08 |  4992.82 ± 2968.12 |                |                  | 261.66 ± 98.88 | 237.79 ± 98.88 |  261.66 ± 98.88 |
| qwen3.5-0.8b-bf16 | tg1024 (c10) |      669.04 ± 7.53 |      101.78 ± 5.32 | 1013.33 ± 4.71 |    109.83 ± 5.72 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-04 23:06:28 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
