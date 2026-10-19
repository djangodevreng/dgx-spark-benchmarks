# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-10-18 14:09:59
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-flash-next --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model              |         test |    t/s (total) |       t/s (req) |       peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-------------------|-------------:|---------------:|----------------:|---------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.8-flash-next |  pp8192 (c5) | 2182.51 ± 7.58 | 788.70 ± 411.56 |                |                  |  11770.13 ± 4516.00 |  11599.87 ± 4516.00 |  11770.80 ± 4516.04 |
| qwen3.8-flash-next |   tg512 (c5) |   57.61 ± 1.53 |    14.55 ± 1.78 |  114.33 ± 5.25 |     31.07 ± 4.54 |                     |                     |                     |
| qwen3.8-flash-next | pp8192 (c10) | 2158.32 ± 0.99 | 522.84 ± 397.79 |                |                  |  20570.24 ± 9622.51 |  20399.99 ± 9622.51 |  20570.71 ± 9622.60 |
| qwen3.8-flash-next |  tg512 (c10) |   69.38 ± 1.13 |     9.75 ± 1.93 | 153.33 ± 10.87 |     24.50 ± 3.61 |                     |                     |                     |
| qwen3.8-flash-next | pp8192 (c20) | 2119.45 ± 1.90 | 330.60 ± 340.83 |                |                  | 38266.25 ± 20145.08 | 38096.00 ± 20145.08 | 38266.81 ± 20144.98 |
| qwen3.8-flash-next |  tg512 (c20) |   81.63 ± 0.27 |     6.17 ± 1.39 |  213.67 ± 3.86 |     18.17 ± 3.24 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-10-18 13:52:44 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
