# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-08 00:53:34
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-30b-fp8 |  pp2048 @ d4 (c1) |  3153.66 ± 69.73 |  3153.66 ± 69.73 |               |                  |   687.12 ± 19.10 |   603.85 ± 19.10 |   687.12 ± 19.10 |
| nemotron-3-nano-30b-fp8 |   tg512 @ d4 (c1) |     47.21 ± 0.42 |     47.21 ± 0.42 |  48.33 ± 0.47 |     48.33 ± 0.47 |                  |                  |                  |
| nemotron-3-nano-30b-fp8 |  pp2048 @ d4 (c5) | 5884.50 ± 268.64 | 1509.49 ± 510.31 |               |                  | 1431.14 ± 330.14 | 1347.86 ± 330.14 | 1431.14 ± 330.14 |
| nemotron-3-nano-30b-fp8 |   tg512 @ d4 (c5) |     94.53 ± 1.04 |     19.37 ± 0.33 | 110.00 ± 4.08 |     22.00 ± 0.82 |                  |                  |                  |
| nemotron-3-nano-30b-fp8 | pp2048 @ d4 (c10) | 6669.92 ± 406.65 | 1084.22 ± 643.73 |               |                  | 2159.23 ± 697.72 | 2075.96 ± 697.72 | 2159.23 ± 697.72 |
| nemotron-3-nano-30b-fp8 |  tg512 @ d4 (c10) |    128.78 ± 1.95 |     13.79 ± 0.62 | 163.00 ± 4.24 |     17.13 ± 1.28 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-08 00:48:19 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
