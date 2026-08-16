# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-15 23:36:00
**Profile:** fp8
**Model:** Qwen/Qwen3.8-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |   t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:----------------|-------------:|--------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| qwen3.8-27b-fp8 |  pp8192 (c5) | 609.90 ± 0.37 | 242.95 ± 136.56 |               |                  |  39193.09 ± 16342.65 |  39035.40 ± 16342.65 |  39193.09 ± 16342.65 |
| qwen3.8-27b-fp8 |   tg512 (c5) |  21.68 ± 1.04 |     5.86 ± 1.17 |  40.00 ± 0.00 |      8.00 ± 0.00 |                      |                      |                      |
| qwen3.8-27b-fp8 | pp8192 (c10) | 608.66 ± 0.17 | 159.37 ± 128.42 |               |                  |  70145.37 ± 34540.28 |  69987.68 ± 34540.28 |  70145.37 ± 34540.28 |
| qwen3.8-27b-fp8 |  tg512 (c10) |  28.13 ± 0.06 |     4.44 ± 1.27 |  72.33 ± 3.30 |      7.87 ± 0.34 |                      |                      |                      |
| qwen3.8-27b-fp8 | pp8192 (c20) | 604.44 ± 0.82 |  99.75 ± 109.09 |               |                  | 131707.65 ± 70761.81 | 131549.96 ± 70761.81 | 131707.65 ± 70761.81 |
| qwen3.8-27b-fp8 |  tg512 (c20) |  32.06 ± 0.08 |     2.98 ± 1.21 | 126.33 ± 8.96 |      7.25 ± 0.70 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-08-15 22:51:50 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
