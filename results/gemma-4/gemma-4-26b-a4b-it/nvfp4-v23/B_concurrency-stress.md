# Run B — 25k context, c=5/10/20

**Generated:** 2026-06-23 02:16:51
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b-nvfp4 |  pp25000 (c5) | 3290.22 ± 3.43 | 1437.05 ± 898.16 |               |                  |  21260.49 ± 9632.62 |  21195.26 ± 9632.62 |  21260.49 ± 9632.62 |
| gemma-4-26b-a4b-nvfp4 |    tg256 (c5) |   33.03 ± 0.06 |     12.45 ± 5.50 | 115.00 ± 0.00 |     23.40 ± 0.49 |                     |                     |                     |
| gemma-4-26b-a4b-nvfp4 | pp25000 (c10) | 3287.99 ± 8.09 |  922.29 ± 806.01 |               |                  | 38574.50 ± 19635.50 | 38509.26 ± 19635.50 | 38574.56 ± 19635.40 |
| gemma-4-26b-a4b-nvfp4 |   tg256 (c10) |   33.61 ± 0.13 |      7.45 ± 4.27 | 180.00 ± 0.00 |     19.73 ± 1.77 |                     |                     |                     |
| gemma-4-26b-a4b-nvfp4 | pp25000 (c20) | 3283.25 ± 2.94 |  560.88 ± 647.61 |               |                  | 73231.07 ± 39525.49 | 73165.84 ± 39525.49 | 73231.79 ± 39525.94 |
| gemma-4-26b-a4b-nvfp4 |   tg256 (c20) |   33.33 ± 0.29 |      4.05 ± 2.65 | 240.00 ± 0.00 |     16.03 ± 3.56 |                     |                     |                     |

llama-benchy (0.3.8)
date: 2026-06-23 01:57:35 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
