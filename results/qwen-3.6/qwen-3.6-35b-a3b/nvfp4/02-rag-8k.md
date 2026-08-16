# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-14 07:15:01
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.6-35b-a3b-nvfp4 |  pp8192 (c5) |  5474.60 ± 8.93 | 2264.20 ± 1273.47 |               |                  |  4271.12 ± 1827.91 |  4216.16 ± 1827.91 |  4271.12 ± 1827.91 |
| qwen3.6-35b-a3b-nvfp4 |   tg512 (c5) |   105.34 ± 0.66 |      24.03 ± 1.91 | 141.67 ± 2.36 |     29.13 ± 1.15 |                    |                    |                    |
| qwen3.6-35b-a3b-nvfp4 | pp8192 (c10) | 5433.02 ± 46.21 | 1479.49 ± 1225.24 |               |                  |  7728.73 ± 3875.12 |  7673.78 ± 3875.12 |  7728.73 ± 3875.12 |
| qwen3.6-35b-a3b-nvfp4 |  tg512 (c10) |   135.11 ± 0.79 |      16.59 ± 1.90 | 210.00 ± 0.00 |     24.20 ± 3.38 |                    |                    |                    |
| qwen3.6-35b-a3b-nvfp4 | pp8192 (c20) |  5348.78 ± 2.00 |  911.16 ± 1019.21 |               |                  | 14759.47 ± 8010.08 | 14704.52 ± 8010.08 | 14759.47 ± 8010.08 |
| qwen3.6-35b-a3b-nvfp4 |  tg512 (c20) |   169.20 ± 0.27 |      11.41 ± 1.81 | 304.00 ± 5.66 |     20.20 ± 4.61 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-14 07:06:26 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
