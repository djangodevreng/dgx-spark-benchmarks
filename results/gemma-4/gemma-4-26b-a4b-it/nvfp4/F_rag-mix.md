# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-06 11:02:25
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b-nvfp4 |  pp8192 (c5) | 5472.76 ± 198.19 | 2419.10 ± 1570.99 |               |                  |  4282.21 ± 1952.73 |  4213.71 ± 1952.73 |  4282.21 ± 1952.73 |
| gemma-4-26b-a4b-nvfp4 |   tg512 (c5) |     85.27 ± 5.28 |      20.91 ± 1.76 | 120.00 ± 0.00 |     26.53 ± 2.03 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c10) |  5473.16 ± 99.87 | 1503.67 ± 1352.84 |               |                  |  7997.12 ± 4070.77 |  7928.62 ± 4070.77 |  7997.12 ± 4070.77 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c10) |    123.10 ± 4.09 |      15.96 ± 2.17 | 200.00 ± 0.00 |     21.80 ± 2.07 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c20) |  5562.01 ± 64.28 |  948.83 ± 1139.58 |               |                  | 14454.55 ± 7677.90 | 14386.04 ± 7677.90 | 14454.55 ± 7677.90 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c20) |    157.05 ± 1.81 |      10.57 ± 1.84 | 280.00 ± 0.00 |     16.85 ± 2.10 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-06 10:55:48 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
