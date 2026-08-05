# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-09 15:10:00
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.5-9b-bf16 |  pp2048 @ d4 (c1) | 4615.19 ± 362.79 |  4615.19 ± 362.79 |               |                  |    504.88 ± 33.07 |    396.51 ± 33.07 |    504.88 ± 33.07 |
| qwen3.5-9b-bf16 |   tg512 @ d4 (c1) |     12.64 ± 0.03 |      12.64 ± 0.03 |  13.00 ± 0.00 |     13.00 ± 0.00 |                   |                   |                   |
| qwen3.5-9b-bf16 |  pp2048 @ d4 (c5) |  3962.12 ± 92.53 | 1941.78 ± 1387.00 |               |                  |  1504.47 ± 668.03 |  1396.10 ± 668.03 |  1504.47 ± 668.03 |
| qwen3.5-9b-bf16 |   tg512 @ d4 (c5) |     63.52 ± 0.10 |      13.08 ± 0.19 |  70.00 ± 0.00 |     14.00 ± 0.00 |                   |                   |                   |
| qwen3.5-9b-bf16 | pp2048 @ d4 (c10) |  3956.98 ± 22.32 | 1138.14 ± 1040.53 |               |                  | 2789.57 ± 1391.29 | 2681.20 ± 1391.29 | 2789.57 ± 1391.29 |
| qwen3.5-9b-bf16 |  tg512 @ d4 (c10) |    115.64 ± 0.18 |      12.28 ± 0.35 | 130.00 ± 0.00 |     13.23 ± 0.42 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-09 15:03:31 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
