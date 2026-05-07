# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-03 13:50:04
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                         |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-bf16 |  pp2048 @ d4 (c1) |  5570.70 ± 32.52 |   5570.70 ± 32.52 |               |                  |   474.40 ± 12.75 |   327.35 ± 12.75 |   474.40 ± 12.75 |
| nemotron-3-nano-omni-30b-bf16 |   tg512 @ d4 (c1) |     28.69 ± 0.06 |      28.69 ± 0.06 |  29.00 ± 0.00 |     29.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 |  pp2048 @ d4 (c5) | 5856.12 ± 383.79 | 1878.12 ± 1035.63 |               |                  | 1308.51 ± 352.20 | 1161.46 ± 352.20 | 1308.51 ± 352.20 |
| nemotron-3-nano-omni-30b-bf16 |   tg512 @ d4 (c5) |     55.86 ± 1.02 |      11.50 ± 0.44 |  69.33 ± 0.94 |     15.53 ± 1.59 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 | pp2048 @ d4 (c10) |  6626.19 ± 17.51 |  1340.93 ± 865.83 |               |                  | 1998.42 ± 765.01 | 1851.37 ± 765.01 | 1998.42 ± 765.01 |
| nemotron-3-nano-omni-30b-bf16 |  tg512 @ d4 (c10) |     72.64 ± 0.29 |       7.68 ± 0.11 | 100.00 ± 0.00 |     10.37 ± 0.66 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-03 13:43:29 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
