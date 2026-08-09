# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-06 01:01:26
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                         |              test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------------|------------------:|----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-bf16 |  pp2048 @ d4 (c1) | 5285.81 ± 53.50 |   5285.81 ± 53.50 |               |                  |   492.33 ± 10.98 |   354.08 ± 10.98 |   492.33 ± 10.98 |
| nemotron-3-nano-omni-30b-bf16 |   tg512 @ d4 (c1) |    29.30 ± 0.04 |      29.30 ± 0.04 |  30.00 ± 0.00 |     30.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 |  pp2048 @ d4 (c5) |  6068.17 ± 7.22 | 2031.23 ± 1385.63 |               |                  | 1340.57 ± 408.95 | 1202.32 ± 408.95 | 1340.57 ± 408.95 |
| nemotron-3-nano-omni-30b-bf16 |   tg512 @ d4 (c5) |    55.31 ± 0.94 |      11.39 ± 0.47 |  72.33 ± 2.05 |     15.40 ± 1.62 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 | pp2048 @ d4 (c10) | 6169.60 ± 21.49 | 1339.61 ± 1199.43 |               |                  | 2129.81 ± 780.74 | 1991.56 ± 780.74 | 2129.81 ± 780.74 |
| nemotron-3-nano-omni-30b-bf16 |  tg512 @ d4 (c10) |    74.15 ± 0.27 |       8.30 ± 0.40 | 103.33 ± 4.71 |     11.57 ± 0.76 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 00:53:07 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
