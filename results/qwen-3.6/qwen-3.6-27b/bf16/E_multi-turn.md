# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-09 21:40:23
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |              test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|------------------:|----------------:|----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-27b-bf16 |  pp2048 @ d4 (c1) | 1587.42 ± 21.60 | 1587.42 ± 21.60 |              |                  |   1442.81 ± 45.12 |   1185.13 ± 45.12 |   1442.81 ± 45.12 |
| qwen3.6-27b-bf16 |   tg512 @ d4 (c1) |     4.43 ± 0.00 |     4.43 ± 0.00 |  5.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-bf16 |  pp2048 @ d4 (c5) | 1339.40 ± 14.28 | 512.21 ± 279.79 |              |                  | 4881.33 ± 1818.13 | 4623.65 ± 1818.13 | 4881.33 ± 1818.13 |
| qwen3.6-27b-bf16 |   tg512 @ d4 (c5) |    20.04 ± 0.05 |     4.11 ± 0.05 | 25.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-bf16 | pp2048 @ d4 (c10) |  1306.57 ± 5.16 | 316.71 ± 240.74 |              |                  | 8813.54 ± 4094.98 | 8555.87 ± 4094.98 | 8813.54 ± 4094.98 |
| qwen3.6-27b-bf16 |  tg512 @ d4 (c10) |    36.55 ± 0.02 |     3.87 ± 0.10 | 50.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-09 21:20:33 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
