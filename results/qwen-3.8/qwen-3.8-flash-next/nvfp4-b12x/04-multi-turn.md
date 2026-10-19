# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-10-18 15:01:24
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-flash-next --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model              |              test |     t/s (total) |       t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-------------------|------------------:|----------------:|----------------:|---------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.8-flash-next |  pp2048 @ d4 (c1) | 2270.09 ± 40.03 | 2270.09 ± 40.03 |                |                  |    983.73 ± 25.85 |    811.72 ± 25.85 |    984.38 ± 25.78 |
| qwen3.8-flash-next |   tg512 @ d4 (c1) |    36.21 ± 1.88 |    36.21 ± 1.88 |   53.00 ± 1.41 |     53.00 ± 1.41 |                   |                   |                   |
| qwen3.8-flash-next |  pp2048 @ d4 (c5) | 2150.34 ± 12.45 | 559.70 ± 162.17 |                |                  |  3848.88 ± 761.31 |  3676.86 ± 761.31 |  3848.99 ± 761.30 |
| qwen3.8-flash-next |   tg512 @ d4 (c5) |    75.81 ± 1.08 |    17.30 ± 1.56 | 118.00 ± 13.64 |     31.93 ± 3.28 |                   |                   |                   |
| qwen3.8-flash-next | pp2048 @ d4 (c10) | 2151.46 ± 24.20 | 369.80 ± 195.05 |                |                  | 6385.61 ± 2190.92 | 6213.60 ± 2190.92 | 6385.71 ± 2190.95 |
| qwen3.8-flash-next |  tg512 @ d4 (c10) |    98.19 ± 2.93 |    11.62 ± 0.88 | 164.33 ± 10.50 |     24.37 ± 4.14 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-10-18 14:54:23 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
