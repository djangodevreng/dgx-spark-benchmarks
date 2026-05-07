# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-03 09:53:37
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                          |          test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-------------------------------|--------------:|-----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-omni-30b-nvfp4 |  pp25000 (c5) | 9990.56 ± 157.74 | 4103.44 ± 2374.46 |               |                  |   7207.99 ± 3063.89 |   7132.04 ± 3063.89 |   7209.40 ± 3064.14 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c5) |     71.02 ± 1.59 |      20.75 ± 5.30 | 146.67 ± 2.36 |     31.60 ± 2.92 |                     |                     |                     |
| nemotron-3-nano-omni-30b-nvfp4 | pp25000 (c10) |  10119.34 ± 5.73 | 2640.08 ± 2082.59 |               |                  |  12735.72 ± 6225.94 |  12659.77 ± 6225.94 |  12736.61 ± 6226.06 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg256 (c10) |     76.68 ± 3.21 |      12.99 ± 4.85 | 222.67 ± 1.89 |     26.37 ± 3.44 |                     |                     |                     |
| nemotron-3-nano-omni-30b-nvfp4 | pp25000 (c20) | 9717.12 ± 376.50 | 1648.97 ± 1836.53 |               |                  | 24076.28 ± 12906.64 | 24000.32 ± 12906.64 | 24077.07 ± 12906.73 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg256 (c20) |     83.73 ± 2.55 |       7.79 ± 3.45 | 326.33 ± 9.67 |     20.23 ± 3.84 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-03 09:47:46 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
