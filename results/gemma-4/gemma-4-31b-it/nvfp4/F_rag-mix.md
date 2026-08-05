# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-08 13:25:39
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model             |         test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------|-------------:|---------------:|----------------:|-------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-31b-nvfp4 |  pp8192 (c5) | 1301.71 ± 7.62 | 565.90 ± 367.04 |              |                  |  18111.96 ± 8171.29 |  17898.71 ± 8171.29 |  18111.96 ± 8171.29 |
| gemma-4-31b-nvfp4 |   tg512 (c5) |   21.20 ± 1.23 |     5.34 ± 0.52 | 35.00 ± 0.00 |      7.00 ± 0.00 |                     |                     |                     |
| gemma-4-31b-nvfp4 | pp8192 (c10) | 1279.95 ± 4.74 | 360.12 ± 339.63 |              |                  | 34140.44 ± 17562.62 | 33927.18 ± 17562.62 | 34140.44 ± 17562.62 |
| gemma-4-31b-nvfp4 |  tg512 (c10) |   29.26 ± 0.34 |     4.29 ± 0.86 | 60.00 ± 0.00 |      6.43 ± 0.50 |                     |                     |                     |
| gemma-4-31b-nvfp4 | pp8192 (c20) | 1275.21 ± 1.61 | 215.83 ± 261.56 |              |                  | 63638.14 ± 33787.91 | 63424.88 ± 33787.91 | 63638.14 ± 33787.91 |
| gemma-4-31b-nvfp4 |  tg512 (c20) |   38.52 ± 0.98 |     3.05 ± 0.91 | 98.33 ± 2.36 |      5.68 ± 0.92 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-08 13:01:15 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
