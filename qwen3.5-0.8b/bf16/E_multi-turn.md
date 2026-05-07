# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-04 23:13:34
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |              test |        t/s (total) |          t/s (req) |       peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|------------------:|-------------------:|-------------------:|---------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-0.8b-bf16 |  pp2048 @ d4 (c1) | 30957.51 ± 1292.15 | 30957.51 ± 1292.15 |                |                  |    84.44 ± 5.03 |    60.41 ± 5.03 |    84.44 ± 5.03 |
| qwen3.5-0.8b-bf16 |   tg512 @ d4 (c1) |     101.51 ± 12.89 |     101.51 ± 12.89 | 124.80 ± 18.82 |   124.80 ± 18.82 |                 |                 |                 |
| qwen3.5-0.8b-bf16 |  pp2048 @ d4 (c5) |  24898.26 ± 297.57 | 10249.46 ± 5458.32 |                |                  |  256.22 ± 95.84 |  232.20 ± 95.84 |  256.22 ± 95.84 |
| qwen3.5-0.8b-bf16 |   tg512 @ d4 (c5) |     499.49 ± 15.94 |      108.19 ± 2.00 |  555.00 ± 0.00 |    113.07 ± 2.02 |                 |                 |                 |
| qwen3.5-0.8b-bf16 | pp2048 @ d4 (c10) |  24480.32 ± 951.32 |  6097.34 ± 4564.62 |                |                  | 467.99 ± 213.99 | 443.96 ± 213.99 | 467.99 ± 213.99 |
| qwen3.5-0.8b-bf16 |  tg512 @ d4 (c10) |     728.51 ± 43.30 |      91.43 ± 13.89 | 938.00 ± 24.06 |   101.09 ± 12.46 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-04 23:12:51 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
