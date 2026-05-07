# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-07 16:30:57
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |        t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|------------------:|-------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-2b-bf16 |  pp2048 @ d4 (c1) |  6575.31 ± 2986.49 | 6575.31 ± 2986.49 |               |                  | 454.83 ± 250.55 | 406.23 ± 250.55 | 454.83 ± 250.55 |
| qwen3.5-2b-bf16 |   tg512 @ d4 (c1) |       44.09 ± 0.18 |      44.09 ± 0.18 |  45.00 ± 0.00 |     45.00 ± 0.00 |                 |                 |                 |
| qwen3.5-2b-bf16 |  pp2048 @ d4 (c5) | 13392.48 ± 1753.87 | 6023.04 ± 4321.18 |               |                  | 480.60 ± 200.39 | 432.00 ± 200.39 | 480.60 ± 200.39 |
| qwen3.5-2b-bf16 |   tg512 @ d4 (c5) |     244.35 ± 10.09 |      52.10 ± 0.87 | 271.67 ± 2.36 |     54.53 ± 0.50 |                 |                 |                 |
| qwen3.5-2b-bf16 | pp2048 @ d4 (c10) |  15297.91 ± 218.83 | 4183.68 ± 3478.66 |               |                  | 735.96 ± 346.21 | 687.36 ± 346.21 | 735.96 ± 346.21 |
| qwen3.5-2b-bf16 |  tg512 @ d4 (c10) |     378.92 ± 30.36 |      47.70 ± 2.88 | 504.00 ± 4.32 |     52.17 ± 0.93 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-07 16:29:22 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
