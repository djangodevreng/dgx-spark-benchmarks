# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-06 10:55:47
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c1) | 6949.16 ± 118.57 |  6949.16 ± 118.57 |               |                  |    327.54 ± 8.99 |    262.85 ± 8.99 |    327.54 ± 8.99 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c1) |     29.61 ± 0.07 |      29.61 ± 0.07 |  30.00 ± 0.00 |     30.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c5) |  6548.85 ± 18.42 |  2025.57 ± 720.61 |               |                  | 1109.13 ± 325.07 | 1044.44 ± 325.07 | 1109.13 ± 325.07 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c5) |    100.62 ± 1.39 |      23.98 ± 1.75 | 121.67 ± 2.36 |     27.33 ± 2.49 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp2048 @ d4 (c10) |  6727.71 ± 45.84 | 1339.30 ± 1167.73 |               |                  | 1936.35 ± 733.62 | 1871.67 ± 733.62 | 1936.35 ± 733.62 |
| gemma-4-26b-a4b-nvfp4 |  tg512 @ d4 (c10) |    167.58 ± 6.56 |      19.51 ± 1.74 | 213.33 ± 4.71 |     23.60 ± 1.89 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-06 10:52:30 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
