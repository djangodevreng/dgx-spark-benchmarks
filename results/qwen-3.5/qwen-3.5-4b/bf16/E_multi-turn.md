# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-07 21:26:10
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.5-4b-bf16 |  pp2048 @ d4 (c1) | 8170.28 ± 139.44 |  8170.28 ± 139.44 |               |                  |    288.20 ± 4.84 |    224.89 ± 4.84 |    288.20 ± 4.84 |
| qwen3.5-4b-bf16 |   tg512 @ d4 (c1) |     20.74 ± 0.04 |      20.74 ± 0.04 |  21.67 ± 0.47 |     21.67 ± 0.47 |                  |                  |                  |
| qwen3.5-4b-bf16 |  pp2048 @ d4 (c5) |  6720.48 ± 42.85 | 3082.23 ± 2024.86 |               |                  |  900.33 ± 383.84 |  837.01 ± 383.84 |  900.33 ± 383.84 |
| qwen3.5-4b-bf16 |   tg512 @ d4 (c5) |    115.09 ± 0.12 |      23.72 ± 0.36 | 125.00 ± 0.00 |     25.00 ± 0.00 |                  |                  |                  |
| qwen3.5-4b-bf16 | pp2048 @ d4 (c10) | 6577.68 ± 115.58 | 1942.27 ± 1818.87 |               |                  | 1667.77 ± 841.88 | 1604.46 ± 841.88 | 1667.77 ± 841.88 |
| qwen3.5-4b-bf16 |  tg512 @ d4 (c10) |    202.73 ± 0.10 |      21.59 ± 0.65 | 230.00 ± 0.00 |     23.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-07 21:22:24 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
