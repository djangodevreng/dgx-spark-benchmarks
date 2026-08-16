# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-14 14:54:37
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-fp8 |  pp8192 (c5) | 3982.28 ± 22.46 | 1638.01 ± 937.85 |               |                  |   5902.50 ± 2502.59 |   5834.19 ± 2502.59 |   5902.50 ± 2502.59 |
| qwen3.6-35b-a3b-fp8 |   tg512 (c5) |    84.93 ± 0.29 |     19.63 ± 1.77 | 120.00 ± 0.00 |     25.53 ± 1.82 |                     |                     |                     |
| qwen3.6-35b-a3b-fp8 | pp8192 (c10) | 3917.12 ± 48.65 | 1063.03 ± 887.01 |               |                  |  10738.66 ± 5348.06 |  10670.36 ± 5348.06 |  10738.66 ± 5348.06 |
| qwen3.6-35b-a3b-fp8 |  tg512 (c10) |   101.26 ± 0.27 |     12.52 ± 1.52 | 166.67 ± 4.71 |     20.47 ± 4.18 |                     |                     |                     |
| qwen3.6-35b-a3b-fp8 | pp8192 (c20) |  3891.19 ± 1.07 |  663.01 ± 745.80 |               |                  | 20289.40 ± 10981.31 | 20221.10 ± 10981.31 | 20289.40 ± 10981.31 |
| qwen3.6-35b-a3b-fp8 |  tg512 (c20) |   130.48 ± 0.33 |      8.97 ± 1.56 | 253.33 ± 9.43 |     16.88 ± 4.64 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-14 14:43:30 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
