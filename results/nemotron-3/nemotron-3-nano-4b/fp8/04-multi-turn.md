# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-08 09:50:16
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                  |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------|------------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-4b-fp8 |  pp2048 @ d4 (c1) |  6036.70 ± 948.56 |  6036.70 ± 948.56 |               |                  |   361.17 ± 58.89 |   318.57 ± 58.89 |   361.17 ± 58.89 |
| nemotron-3-nano-4b-fp8 |   tg512 @ d4 (c1) |      42.17 ± 0.24 |      42.17 ± 0.24 |  43.00 ± 0.00 |     43.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-4b-fp8 |  pp2048 @ d4 (c5) | 6892.20 ± 1039.81 | 2597.53 ± 1246.45 |               |                  |  941.35 ± 387.90 |  898.74 ± 387.90 |  941.35 ± 387.90 |
| nemotron-3-nano-4b-fp8 |   tg512 @ d4 (c5) |    171.87 ± 13.44 |      39.15 ± 1.34 | 205.00 ± 0.00 |     42.27 ± 1.24 |                  |                  |                  |
| nemotron-3-nano-4b-fp8 | pp2048 @ d4 (c10) |  8845.20 ± 253.63 | 2091.10 ± 1304.36 |               |                  | 1245.77 ± 570.52 | 1203.17 ± 570.52 | 1245.77 ± 570.52 |
| nemotron-3-nano-4b-fp8 |  tg512 @ d4 (c10) |     300.32 ± 3.53 |      32.63 ± 1.05 | 350.00 ± 0.00 |     35.83 ± 0.64 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-08 09:47:20 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
