# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-13 14:12:21
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                     |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-30b-nvfp4 |  pp2048 @ d4 (c1) | 6536.68 ± 106.43 |  6536.68 ± 106.43 |               |                  |    345.01 ± 7.14 |    291.13 ± 7.14 |    345.01 ± 7.14 |
| nemotron-3-nano-30b-nvfp4 |   tg512 @ d4 (c1) |     62.74 ± 0.04 |      62.74 ± 0.04 |  63.00 ± 0.00 |     63.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-30b-nvfp4 |  pp2048 @ d4 (c5) |  6455.15 ± 24.12 | 2217.65 ± 1751.43 |               |                  | 1221.18 ± 422.41 | 1167.29 ± 422.41 | 1221.18 ± 422.41 |
| nemotron-3-nano-30b-nvfp4 |   tg512 @ d4 (c5) |    144.36 ± 0.21 |      30.35 ± 0.72 | 163.33 ± 2.36 |     32.67 ± 0.47 |                  |                  |                  |
| nemotron-3-nano-30b-nvfp4 | pp2048 @ d4 (c10) |  6468.39 ± 12.84 | 1394.30 ± 1445.60 |               |                  | 2065.94 ± 806.22 | 2012.06 ± 806.22 | 2065.94 ± 806.22 |
| nemotron-3-nano-30b-nvfp4 |  tg512 @ d4 (c10) |    196.24 ± 3.88 |      21.34 ± 0.73 | 240.00 ± 0.00 |     24.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-13 14:08:48 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
