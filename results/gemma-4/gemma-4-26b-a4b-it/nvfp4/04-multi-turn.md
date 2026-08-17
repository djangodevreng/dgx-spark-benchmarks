# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-16 16:00:49
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c1) | 6596.47 ± 130.52 |  6596.47 ± 130.52 |               |                  |    344.79 ± 2.10 |    280.36 ± 2.10 |    344.79 ± 2.10 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c1) |     30.06 ± 0.09 |      30.06 ± 0.09 |  31.00 ± 0.00 |     31.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c5) |  6386.59 ± 25.01 | 2417.96 ± 2145.55 |               |                  | 1238.97 ± 451.31 | 1174.55 ± 451.31 | 1238.97 ± 451.31 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c5) |    108.37 ± 5.54 |      24.53 ± 0.84 | 128.33 ± 4.71 |     27.87 ± 1.96 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp2048 @ d4 (c10) | 6336.11 ± 200.36 | 1482.91 ± 1677.95 |               |                  | 2076.88 ± 838.75 | 2012.46 ± 838.75 | 2076.88 ± 838.75 |
| gemma-4-26b-a4b-nvfp4 |  tg512 @ d4 (c10) |    174.89 ± 2.38 |      19.81 ± 0.72 | 216.67 ± 4.71 |     22.87 ± 0.88 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-16 15:56:20 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
