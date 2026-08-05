# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-06-26 10:18:34
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |              test |      t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|------------------:|-----------------:|------------------:|---------------:|-----------------:|-----------------:|-----------------:|----------------:|
| gpt-oss-20b-mxfp4 |  pp2048 @ d4 (c1) | 9426.76 ± 304.51 |  9426.76 ± 304.51 |                |                  |    276.05 ± 7.96 |    204.75 ± 7.96 |   341.05 ± 7.08 |
| gpt-oss-20b-mxfp4 |   tg512 @ d4 (c1) |     44.71 ± 0.12 |      44.71 ± 0.12 |   46.00 ± 0.00 |     46.00 ± 0.00 |                  |                  |                 |
| gpt-oss-20b-mxfp4 |  pp2048 @ d4 (c5) |  7542.64 ± 68.08 | 3069.86 ± 2524.48 |                |                  |  960.32 ± 351.14 |  889.01 ± 351.14 | 1245.11 ± 13.15 |
| gpt-oss-20b-mxfp4 |   tg512 @ d4 (c5) |    138.87 ± 3.14 |      28.99 ± 1.19 |  155.00 ± 0.00 |     32.87 ± 3.10 |                  |                  |                 |
| gpt-oss-20b-mxfp4 | pp2048 @ d4 (c10) | 7947.72 ± 104.43 | 2010.79 ± 1775.63 |                |                  | 1612.41 ± 653.01 | 1407.44 ± 635.78 | 2343.53 ± 30.48 |
| gpt-oss-20b-mxfp4 |  tg512 @ d4 (c10) |   151.43 ± 40.11 |      24.60 ± 4.49 | 186.00 ± 23.37 |     27.81 ± 4.59 |                  |                  |                 |

llama-benchy (0.3.8)
date: 2026-06-26 10:15:16 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
