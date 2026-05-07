# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-04 21:43:44
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:--------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.6-35b-a3b-fp8 |  pp8192 (c5) | 5260.11 ± 41.99 | 2203.11 ± 1257.35 |               |                  |  4415.36 ± 1887.96 |  4347.27 ± 1887.96 |  4415.36 ± 1887.96 |
| qwen3.6-35b-a3b-fp8 |   tg512 (c5) |    82.65 ± 0.33 |      18.31 ± 1.15 | 106.67 ± 2.36 |     23.07 ± 2.08 |                    |                    |                    |
| qwen3.6-35b-a3b-fp8 | pp8192 (c10) | 5214.57 ± 30.28 | 1411.95 ± 1151.81 |               |                  |  8051.04 ± 4029.59 |  7982.95 ± 4029.59 |  8051.04 ± 4029.59 |
| qwen3.6-35b-a3b-fp8 |  tg512 (c10) |   109.53 ± 0.84 |      12.96 ± 1.19 | 160.00 ± 0.00 |     19.50 ± 3.65 |                    |                    |                    |
| qwen3.6-35b-a3b-fp8 | pp8192 (c20) | 5043.75 ± 15.13 |   867.44 ± 948.36 |               |                  | 15362.62 ± 8434.44 | 15294.53 ± 8434.44 | 15362.62 ± 8434.44 |
| qwen3.6-35b-a3b-fp8 |  tg512 (c20) |   143.46 ± 0.73 |       9.29 ± 1.23 | 240.00 ± 0.00 |     16.25 ± 4.06 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-04 21:35:58 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
