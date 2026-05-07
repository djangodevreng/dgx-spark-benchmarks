# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-05 12:25:08
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |              test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:---------------------|------------------:|----------------:|-----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-35b-a3b-bf16 |  pp2048 @ d4 (c1) | 4323.86 ± 40.99 |  4323.86 ± 40.99 |               |                  |     553.61 ± 9.74 |     436.68 ± 9.74 |     553.61 ± 9.74 |
| qwen3.6-35b-a3b-bf16 |   tg512 @ d4 (c1) |    30.39 ± 0.01 |     30.39 ± 0.01 |  31.00 ± 0.00 |     31.00 ± 0.00 |                   |                   |                   |
| qwen3.6-35b-a3b-bf16 |  pp2048 @ d4 (c5) | 3555.93 ± 31.26 | 1434.45 ± 805.20 |               |                  |  1798.11 ± 693.12 |  1681.18 ± 693.12 |  1798.11 ± 693.12 |
| qwen3.6-35b-a3b-bf16 |   tg512 @ d4 (c5) |    59.66 ± 0.79 |     12.25 ± 0.25 |  73.33 ± 2.36 |     14.67 ± 0.47 |                   |                   |                   |
| qwen3.6-35b-a3b-bf16 | pp2048 @ d4 (c10) | 3503.07 ± 12.41 |  885.03 ± 691.41 |               |                  | 3218.98 ± 1506.48 | 3102.04 ± 1506.48 | 3218.98 ± 1506.48 |
| qwen3.6-35b-a3b-bf16 |  tg512 @ d4 (c10) |    79.83 ± 1.02 |      8.34 ± 0.21 | 100.00 ± 0.00 |     10.70 ± 1.00 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-05 12:18:45 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
