# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-06-23 02:35:11
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b-nvfp4 |  pp8192 (c5) |  5301.73 ± 5.70 | 2325.03 ± 1475.15 |               |                  |  4417.00 ± 1988.58 |  4351.68 ± 1988.58 |  4417.00 ± 1988.58 |
| gemma-4-26b-a4b-nvfp4 |   tg512 (c5) |    91.63 ± 0.66 |      21.67 ± 1.85 | 125.00 ± 0.00 |     26.87 ± 1.02 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c10) | 5288.13 ± 41.73 | 1432.18 ± 1277.55 |               |                  |  8308.60 ± 4213.50 |  8243.28 ± 4213.50 |  8308.60 ± 4213.50 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c10) |   118.91 ± 1.44 |      16.29 ± 2.75 | 200.00 ± 0.00 |     22.60 ± 1.52 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c20) |  5319.69 ± 8.68 |  910.11 ± 1092.00 |               |                  | 15207.93 ± 8098.09 | 15142.62 ± 8098.09 | 15207.93 ± 8098.09 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c20) |   153.93 ± 2.23 |      10.65 ± 1.98 | 300.00 ± 0.00 |     17.88 ± 2.07 |                    |                    |                    |

llama-benchy (0.3.8)
date: 2026-06-23 02:26:25 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
