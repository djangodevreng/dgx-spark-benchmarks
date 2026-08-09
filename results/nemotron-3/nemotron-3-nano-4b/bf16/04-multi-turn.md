# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-06 06:07:21
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-4b-bf16 |  pp2048 @ d4 (c1) | 9145.46 ± 386.26 |  9145.46 ± 386.26 |               |                  |   274.34 ± 10.25 |   204.72 ± 10.25 |   274.34 ± 10.25 |
| nemotron-3-nano-4b-bf16 |   tg512 @ d4 (c1) |     24.88 ± 0.22 |      24.88 ± 0.22 |  26.00 ± 0.00 |     26.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-4b-bf16 |  pp2048 @ d4 (c5) |   7489.46 ± 7.36 | 3726.72 ± 2620.67 |               |                  |  792.97 ± 348.95 |  723.35 ± 348.95 |  792.97 ± 348.95 |
| nemotron-3-nano-4b-bf16 |   tg512 @ d4 (c5) |    121.67 ± 0.36 |      26.50 ± 0.47 | 140.00 ± 0.00 |     28.80 ± 0.40 |                  |                  |                  |
| nemotron-3-nano-4b-bf16 | pp2048 @ d4 (c10) |  7445.39 ± 86.37 | 2325.57 ± 2305.84 |               |                  | 1458.34 ± 746.46 | 1388.72 ± 746.46 | 1458.34 ± 746.46 |
| nemotron-3-nano-4b-bf16 |  tg512 @ d4 (c10) |    211.03 ± 8.18 |      23.24 ± 0.75 | 253.00 ± 4.24 |     25.73 ± 0.57 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 06:02:58 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
