# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-06 04:16:10
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-fp8 |  pp2048 @ d4 (c1) | 2957.82 ± 156.65 | 2957.82 ± 156.65 |               |                  |   722.32 ± 27.53 |   644.84 ± 27.53 |   722.32 ± 27.53 |
| nemotron-3-nano-omni-30b-fp8 |   tg512 @ d4 (c1) |     55.78 ± 0.02 |     55.78 ± 0.02 |  57.00 ± 0.00 |     57.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-omni-30b-fp8 |  pp2048 @ d4 (c5) | 4894.69 ± 157.77 | 1137.95 ± 239.22 |               |                  | 1798.70 ± 278.32 | 1721.21 ± 278.32 | 1798.70 ± 278.32 |
| nemotron-3-nano-omni-30b-fp8 |   tg512 @ d4 (c5) |    104.16 ± 0.61 |     21.35 ± 0.30 | 121.67 ± 2.36 |     24.60 ± 0.88 |                  |                  |                  |
| nemotron-3-nano-omni-30b-fp8 | pp2048 @ d4 (c10) | 7044.62 ± 498.96 | 1135.10 ± 556.76 |               |                  | 1997.92 ± 633.39 | 1920.44 ± 633.39 | 1997.92 ± 633.39 |
| nemotron-3-nano-omni-30b-fp8 |  tg512 @ d4 (c10) |    137.26 ± 1.26 |     14.81 ± 0.64 | 173.00 ± 4.24 |     18.37 ± 1.64 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 04:11:23 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
