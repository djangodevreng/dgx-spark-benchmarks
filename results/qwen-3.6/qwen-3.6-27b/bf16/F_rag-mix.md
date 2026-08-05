# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-09 22:12:10
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|----------------:|-------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-27b-bf16 |  pp8192 (c5) | 1314.59 ± 3.32 | 541.61 ± 315.06 |              |                  |  17974.86 ± 7596.95 |  17718.95 ± 7596.95 |  17974.86 ± 7596.95 |
| qwen3.6-27b-bf16 |   tg512 (c5) |   17.30 ± 0.02 |     3.80 ± 0.18 | 25.00 ± 0.00 |      5.00 ± 0.00 |                     |                     |                     |
| qwen3.6-27b-bf16 | pp8192 (c10) | 1274.89 ± 2.11 | 351.77 ± 292.20 |              |                  | 32635.60 ± 16496.91 | 32379.69 ± 16496.91 | 32635.60 ± 16496.91 |
| qwen3.6-27b-bf16 |  tg512 (c10) |   27.43 ± 0.06 |     3.29 ± 0.30 | 40.00 ± 0.00 |      4.50 ± 0.50 |                     |                     |                     |
| qwen3.6-27b-bf16 | pp8192 (c20) | 1204.40 ± 0.50 | 217.14 ± 247.23 |              |                  | 63618.10 ± 35682.34 | 63362.18 ± 35682.34 | 63618.10 ± 35682.34 |
| qwen3.6-27b-bf16 |  tg512 (c20) |   37.47 ± 0.02 |     2.52 ± 0.38 | 80.00 ± 0.00 |      4.25 ± 0.43 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-09 21:40:24 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
