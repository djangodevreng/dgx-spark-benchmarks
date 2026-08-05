# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-09 15:20:05
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|-------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.5-9b-bf16 |  pp8192 (c5) | 3923.16 ± 12.51 | 1691.85 ± 1010.58 |               |                  |   5867.17 ± 2564.24 |   5770.04 ± 2564.24 |   5867.17 ± 2564.24 |
| qwen3.5-9b-bf16 |   tg512 (c5) |    54.73 ± 0.10 |      12.08 ± 0.62 |  70.00 ± 0.00 |     14.00 ± 0.00 |                     |                     |                     |
| qwen3.5-9b-bf16 | pp8192 (c10) |  3900.46 ± 7.44 |  1097.76 ± 934.96 |               |                  |  10661.37 ± 5427.43 |  10564.24 ± 5427.43 |  10661.37 ± 5427.43 |
| qwen3.5-9b-bf16 |  tg512 (c10) |    86.73 ± 0.06 |      10.49 ± 0.99 | 130.00 ± 0.00 |     13.30 ± 0.46 |                     |                     |                     |
| qwen3.5-9b-bf16 | pp8192 (c20) |  3794.22 ± 7.29 |   675.57 ± 789.75 |               |                  | 20421.72 ± 11250.38 | 20324.59 ± 11250.38 | 20421.72 ± 11250.38 |
| qwen3.5-9b-bf16 |  tg512 (c20) |   119.17 ± 0.30 |       8.08 ± 1.23 | 220.00 ± 0.00 |     12.35 ± 1.01 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-09 15:10:01 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
