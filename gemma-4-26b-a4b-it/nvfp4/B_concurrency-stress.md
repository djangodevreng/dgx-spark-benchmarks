# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-06 10:37:03
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|--------------:|----------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b-nvfp4 |  pp25000 (c5) | 3574.32 ± 28.66 | 1561.45 ± 988.64 |               |                  |  19723.34 ± 8956.15 |  19650.16 ± 8956.15 |  19723.71 ± 8956.01 |
| gemma-4-26b-a4b-nvfp4 |    tg256 (c5) |    34.34 ± 0.21 |     12.43 ± 5.04 | 110.00 ± 0.00 |     22.40 ± 0.61 |                     |                     |                     |
| gemma-4-26b-a4b-nvfp4 | pp25000 (c10) |  3558.97 ± 7.74 | 1002.22 ± 878.25 |               |                  | 35508.14 ± 18077.57 | 35434.96 ± 18077.57 | 35508.39 ± 18077.71 |
| gemma-4-26b-a4b-nvfp4 |   tg256 (c10) |    35.58 ± 0.14 |      7.56 ± 4.05 | 177.67 ± 3.30 |     19.40 ± 1.84 |                     |                     |                     |
| gemma-4-26b-a4b-nvfp4 | pp25000 (c20) | 3567.73 ± 16.24 |  605.91 ± 695.21 |               |                  | 67399.11 ± 36295.43 | 67325.93 ± 36295.43 | 67399.94 ± 36295.85 |
| gemma-4-26b-a4b-nvfp4 |   tg256 (c20) |    36.18 ± 0.09 |      4.26 ± 2.67 | 240.00 ± 0.00 |     15.83 ± 3.41 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-06 10:23:29 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
