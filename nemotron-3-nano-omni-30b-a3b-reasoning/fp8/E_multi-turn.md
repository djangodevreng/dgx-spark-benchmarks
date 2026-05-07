# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-03 11:34:19
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-fp8 |  pp2048 @ d4 (c1) | 8134.11 ± 347.48 |  8134.11 ± 347.48 |               |                  |    314.72 ± 5.73 |    233.10 ± 5.73 |    314.72 ± 5.73 |
| nemotron-3-nano-omni-30b-fp8 |   tg512 @ d4 (c1) |     49.72 ± 0.52 |      49.72 ± 0.52 |  51.00 ± 0.00 |     51.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-omni-30b-fp8 |  pp2048 @ d4 (c5) |  8202.78 ± 42.89 | 2552.78 ± 1000.75 |               |                  |  930.22 ± 273.71 |  848.59 ± 273.71 |  930.22 ± 273.71 |
| nemotron-3-nano-omni-30b-fp8 |   tg512 @ d4 (c5) |    100.27 ± 1.52 |      20.87 ± 1.31 | 115.33 ± 0.47 |     24.60 ± 2.65 |                  |                  |                  |
| nemotron-3-nano-omni-30b-fp8 | pp2048 @ d4 (c10) |  8788.52 ± 41.08 |  1589.78 ± 889.44 |               |                  | 1550.77 ± 542.55 | 1469.14 ± 542.55 | 1550.77 ± 542.55 |
| nemotron-3-nano-omni-30b-fp8 |  tg512 @ d4 (c10) |    134.34 ± 1.63 |      14.88 ± 0.69 | 176.67 ± 4.71 |     19.63 ± 1.05 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-03 11:30:43 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
