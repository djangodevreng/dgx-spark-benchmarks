# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-08 13:35:21
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |       t/s (total) |         t/s (req) |     peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|------------------:|------------------:|-------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-31b-nvfp4 |   pp256 (c1) | 4947.29 ± 4986.93 | 4947.29 ± 4986.93 |              |                  |  319.22 ± 62.38 |  107.21 ± 62.38 |  319.22 ± 62.38 |
| gemma-4-31b-nvfp4 |  tg4096 (c1) |       6.55 ± 0.31 |       6.55 ± 0.31 |  7.00 ± 0.00 |      7.00 ± 0.00 |                 |                 |                 |
| gemma-4-31b-nvfp4 |   pp256 (c5) |   1683.54 ± 11.45 |    484.42 ± 18.89 |              |                  |   697.01 ± 8.98 |   485.00 ± 8.98 |   697.01 ± 8.98 |
| gemma-4-31b-nvfp4 |  tg4096 (c5) |      16.92 ± 0.60 |       6.57 ± 0.04 | 35.00 ± 0.00 |      7.00 ± 0.00 |                 |                 |                 |
| gemma-4-31b-nvfp4 |  pp256 (c10) |   1871.59 ± 50.56 |    225.45 ± 13.52 |              |                  | 1257.44 ± 37.18 | 1045.43 ± 37.18 | 1257.44 ± 37.18 |
| gemma-4-31b-nvfp4 | tg4096 (c10) |      32.78 ± 4.62 |       6.46 ± 0.05 | 70.00 ± 0.00 |      7.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-08 13:25:40 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
