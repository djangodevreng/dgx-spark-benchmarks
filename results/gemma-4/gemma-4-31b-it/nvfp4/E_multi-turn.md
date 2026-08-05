# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-08 13:01:14
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |              test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------------|------------------:|-----------------:|-----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| gemma-4-31b-nvfp4 |  pp2048 @ d4 (c1) | 1992.27 ± 123.78 | 1992.27 ± 123.78 |              |                  |   1149.37 ± 65.94 |    935.39 ± 65.94 |   1149.37 ± 65.94 |
| gemma-4-31b-nvfp4 |   tg512 @ d4 (c1) |      6.42 ± 0.38 |      6.42 ± 0.38 |  7.00 ± 0.00 |      7.00 ± 0.00 |                   |                   |                   |
| gemma-4-31b-nvfp4 |  pp2048 @ d4 (c5) |  1521.22 ± 34.24 |   347.27 ± 21.73 |              |                  |  5631.91 ± 301.07 |  5417.93 ± 301.07 |  5631.91 ± 301.07 |
| gemma-4-31b-nvfp4 |   tg512 @ d4 (c5) |     24.15 ± 1.75 |      6.21 ± 0.11 | 35.00 ± 0.00 |      7.00 ± 0.00 |                   |                   |                   |
| gemma-4-31b-nvfp4 | pp2048 @ d4 (c10) |  1624.63 ± 45.22 |  316.85 ± 234.68 |              |                  | 8158.30 ± 3177.93 | 7944.33 ± 3177.93 | 8158.30 ± 3177.93 |
| gemma-4-31b-nvfp4 |  tg512 @ d4 (c10) |     37.21 ± 1.36 |      5.59 ± 0.30 | 60.00 ± 0.00 |      6.80 ± 0.40 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-08 12:50:35 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
