# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-05 12:38:03
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-bf16 |  pp8192 (c5) | 3561.51 ± 25.26 | 1487.75 ± 866.69 |               |                  |   6605.97 ± 2807.57 |   6490.83 ± 2807.57 |   6605.97 ± 2807.57 |
| qwen3.6-35b-a3b-bf16 |   tg512 (c5) |    51.87 ± 0.38 |     11.43 ± 0.66 |  68.00 ± 1.41 |     15.67 ± 2.09 |                     |                     |                     |
| qwen3.6-35b-a3b-bf16 | pp8192 (c10) |  3470.27 ± 6.23 |  960.17 ± 792.91 |               |                  |  11947.03 ± 6018.86 |  11831.88 ± 6018.86 |  11947.03 ± 6018.86 |
| qwen3.6-35b-a3b-bf16 |  tg512 (c10) |    64.14 ± 0.51 |      7.42 ± 0.58 |  93.33 ± 4.71 |     12.87 ± 3.21 |                     |                     |                     |
| qwen3.6-35b-a3b-bf16 | pp8192 (c20) |  3272.10 ± 5.15 |  590.73 ± 671.88 |               |                  | 23433.57 ± 13096.79 | 23318.43 ± 13096.79 | 23433.57 ± 13096.79 |
| qwen3.6-35b-a3b-bf16 |  tg512 (c20) |    85.78 ± 0.32 |      5.43 ± 0.64 | 143.00 ± 1.63 |     10.45 ± 3.33 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-05 12:25:09 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
