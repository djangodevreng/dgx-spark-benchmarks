# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-04 23:15:06
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model             |         test |       t/s (total) |          t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------------|-------------:|------------------:|-------------------:|---------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.5-0.8b-bf16 |  pp8192 (c5) | 24700.84 ± 284.42 | 10187.60 ± 5669.26 |                |                  |   949.02 ± 393.13 |   926.65 ± 393.13 |   949.02 ± 393.13 |
| qwen3.5-0.8b-bf16 |   tg512 (c5) |    339.94 ± 56.24 |      89.23 ± 16.52 | 483.33 ± 37.71 |   102.08 ± 14.58 |                   |                   |                   |
| qwen3.5-0.8b-bf16 | pp8192 (c10) |  24302.28 ± 42.32 |  6357.36 ± 4779.19 |                |                  |  1717.27 ± 839.95 |  1694.91 ± 839.95 |  1717.27 ± 839.95 |
| qwen3.5-0.8b-bf16 |  tg512 (c10) |     564.80 ± 6.56 |       72.58 ± 8.38 |  857.33 ± 3.77 |     90.33 ± 3.14 |                   |                   |                   |
| qwen3.5-0.8b-bf16 | pp8192 (c20) | 22985.74 ± 246.34 |  3862.17 ± 4075.85 |                |                  | 3342.20 ± 1823.91 | 3319.83 ± 1823.91 | 3342.20 ± 1823.91 |
| qwen3.5-0.8b-bf16 |  tg512 (c20) |    666.88 ± 14.08 |       46.12 ± 8.18 | 1160.00 ± 0.00 |     69.42 ± 8.07 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-04 23:13:35 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
