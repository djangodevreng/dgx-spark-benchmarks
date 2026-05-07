# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-04 14:40:22
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------|------------------:|-----------------:|-----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-27b-fp8 |  pp2048 @ d4 (c1) | 1825.81 ± 802.01 | 1825.81 ± 802.01 |              |                  |  1633.96 ± 964.47 |  1480.17 ± 964.47 |  1633.96 ± 964.47 |
| qwen3.6-27b-fp8 |   tg512 @ d4 (c1) |      7.79 ± 0.01 |      7.79 ± 0.01 |  8.33 ± 0.47 |      8.33 ± 0.47 |                   |                   |                   |
| qwen3.6-27b-fp8 |  pp2048 @ d4 (c5) | 1745.40 ± 159.18 |  686.08 ± 375.95 |              |                  | 3657.10 ± 1514.21 | 3503.30 ± 1514.21 | 3657.10 ± 1514.21 |
| qwen3.6-27b-fp8 |   tg512 @ d4 (c5) |     35.52 ± 0.26 |      7.35 ± 0.14 | 40.00 ± 0.00 |      8.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-fp8 | pp2048 @ d4 (c10) | 1860.21 ± 100.35 |  448.85 ± 343.76 |              |                  | 6248.65 ± 2958.23 | 6094.85 ± 2958.23 | 6248.65 ± 2958.23 |
| qwen3.6-27b-fp8 |  tg512 @ d4 (c10) |     63.04 ± 0.46 |      6.75 ± 0.23 | 80.00 ± 0.00 |      8.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-04 14:28:58 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
