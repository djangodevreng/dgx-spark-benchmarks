# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-06 11:53:07
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b-nvfp4 |  pp8192 (c5) | 5245.28 ± 15.40 | 2383.09 ± 1555.72 |               |                  |  4374.71 ± 2018.67 |  4309.94 ± 2018.67 |  4374.71 ± 2018.67 |
| gemma-4-26b-a4b-nvfp4 |   tg512 (c5) |    91.44 ± 1.70 |      20.93 ± 1.63 | 120.00 ± 0.00 |     24.87 ± 1.20 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c10) |  5280.96 ± 8.23 | 1509.93 ± 1419.85 |               |                  |  8173.34 ± 4231.34 |  8108.57 ± 4231.34 |  8173.34 ± 4231.34 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c10) |   123.09 ± 3.85 |      16.06 ± 2.10 | 200.00 ± 0.00 |     22.30 ± 1.39 |                    |                    |                    |
| gemma-4-26b-a4b-nvfp4 | pp8192 (c20) |  5280.95 ± 4.55 |  928.50 ± 1168.90 |               |                  | 15251.25 ± 8148.06 | 15186.48 ± 8148.06 | 15251.25 ± 8148.06 |
| gemma-4-26b-a4b-nvfp4 |  tg512 (c20) |   154.84 ± 1.04 |      10.45 ± 1.81 | 286.67 ± 9.43 |     17.08 ± 1.91 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-06 11:44:06 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
