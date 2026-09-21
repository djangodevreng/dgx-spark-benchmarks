# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-09-18 14:36:00
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model             |         test |   t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:------------------|-------------:|--------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| qwen3.8-27b-nvfp4 |  pp8192 (c5) | 790.86 ± 2.07 | 317.03 ± 178.52 |               |                  |  30052.30 ± 12584.74 |  29935.28 ± 12584.74 |  30052.30 ± 12584.74 |
| qwen3.8-27b-nvfp4 |   tg512 (c5) |  30.84 ± 0.10 |     8.31 ± 1.61 |  55.00 ± 0.00 |     11.40 ± 0.49 |                      |                      |                      |
| qwen3.8-27b-nvfp4 | pp8192 (c10) | 787.53 ± 1.66 | 207.20 ± 166.49 |               |                  |  54104.81 ± 26794.96 |  53987.79 ± 26794.96 |  54104.81 ± 26794.96 |
| qwen3.8-27b-nvfp4 |  tg512 (c10) |  37.38 ± 0.09 |     6.00 ± 1.81 | 100.00 ± 0.00 |     10.87 ± 0.76 |                      |                      |                      |
| qwen3.8-27b-nvfp4 | pp8192 (c20) | 783.90 ± 0.37 | 129.58 ± 143.19 |               |                  | 101688.95 ± 54512.62 | 101571.93 ± 54512.62 | 101688.95 ± 54512.62 |
| qwen3.8-27b-nvfp4 |  tg512 (c20) |  41.78 ± 0.11 |     3.91 ± 1.61 | 160.00 ± 0.00 |      9.78 ± 1.28 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-09-18 14:02:34 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
