# Run B — 25k context, c=5/10/20

**Generated:** 2026-06-23 00:06:45
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b |  pp25000 (c5) | 3227.93 ± 1.12 | 1412.71 ± 889.76 |               |                  |  21776.06 ± 9893.75 |  21666.70 ± 9893.75 |  21776.06 ± 9893.75 |
| gemma-4-26b-a4b |    tg256 (c5) |   27.03 ± 0.08 |      8.61 ± 2.71 |  70.00 ± 0.00 |     14.60 ± 0.80 |                     |                     |                     |
| gemma-4-26b-a4b | pp25000 (c10) | 3230.29 ± 3.15 |  911.23 ± 796.04 |               |                  | 39089.58 ± 19976.17 | 38980.22 ± 19976.17 | 39089.93 ± 19976.20 |
| gemma-4-26b-a4b |   tg256 (c10) |   29.02 ± 0.03 |      5.32 ± 2.18 | 110.00 ± 0.00 |     12.37 ± 1.58 |                     |                     |                     |
| gemma-4-26b-a4b | pp25000 (c20) | 3211.57 ± 1.46 |  552.35 ± 640.02 |               |                  | 74546.79 ± 40322.78 | 74437.43 ± 40322.78 | 74547.47 ± 40323.15 |
| gemma-4-26b-a4b |   tg256 (c20) |   29.66 ± 0.41 |      3.02 ± 1.48 | 140.33 ± 0.47 |     10.07 ± 2.51 |                     |                     |                     |

llama-benchy (0.3.8)
date: 2026-06-22 23:44:52 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
