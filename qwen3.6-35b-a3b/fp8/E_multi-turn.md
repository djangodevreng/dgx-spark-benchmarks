# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-04 21:35:57
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-fp8 |  pp2048 @ d4 (c1) | 6322.22 ± 264.65 | 6322.22 ± 264.65 |               |                  |    363.63 ± 5.08 |    298.68 ± 5.08 |    363.63 ± 5.08 |
| qwen3.6-35b-a3b-fp8 |   tg512 @ d4 (c1) |     52.35 ± 0.01 |     52.35 ± 0.01 |  53.00 ± 0.00 |     53.00 ± 0.00 |                  |                  |                  |
| qwen3.6-35b-a3b-fp8 |  pp2048 @ d4 (c5) | 5320.37 ± 141.02 | 1990.58 ± 996.95 |               |                  | 1210.74 ± 442.51 | 1145.80 ± 442.51 | 1210.74 ± 442.51 |
| qwen3.6-35b-a3b-fp8 |   tg512 @ d4 (c5) |     98.35 ± 1.78 |     20.23 ± 0.50 | 115.00 ± 4.08 |     23.07 ± 0.77 |                  |                  |                  |
| qwen3.6-35b-a3b-fp8 | pp2048 @ d4 (c10) |  5400.95 ± 71.75 | 1274.49 ± 937.24 |               |                  | 2130.90 ± 965.90 | 2065.95 ± 965.90 | 2130.90 ± 965.90 |
| qwen3.6-35b-a3b-fp8 |  tg512 @ d4 (c10) |    139.36 ± 0.37 |     14.63 ± 0.35 | 176.67 ± 4.71 |     17.80 ± 0.54 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-04 21:32:12 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
