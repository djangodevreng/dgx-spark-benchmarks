# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-07 14:09:16
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |      t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|--------------:|-----------------:|------------------:|---------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.5-2b-bf16 |  pp25000 (c5) | 13712.35 ± 11.08 | 5932.34 ± 3478.96 |                |                  |   5066.41 ± 2266.22 |   5027.11 ± 2266.22 |   5067.37 ± 2266.15 |
| qwen3.5-2b-bf16 |    tg256 (c5) |    100.13 ± 8.50 |      31.81 ± 8.56 |  235.00 ± 0.00 |     48.27 ± 1.12 |                     |                     |                     |
| qwen3.5-2b-bf16 | pp25000 (c10) | 13395.14 ± 15.77 | 3635.87 ± 2891.25 |                |                  |   9409.47 ± 4735.52 |   9370.17 ± 4735.52 |   9410.26 ± 4735.52 |
| qwen3.5-2b-bf16 |   tg256 (c10) |    109.84 ± 8.94 |      21.65 ± 9.08 |  386.33 ± 5.19 |     43.33 ± 5.42 |                     |                     |                     |
| qwen3.5-2b-bf16 | pp25000 (c20) | 12934.94 ± 82.58 | 2330.54 ± 2684.63 |                |                  | 18025.46 ± 10051.08 | 17986.17 ± 10051.08 | 18026.42 ± 10051.45 |
| qwen3.5-2b-bf16 |   tg256 (c20) |    117.95 ± 2.56 |      14.24 ± 8.22 | 541.33 ± 10.21 |    35.30 ± 11.37 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-07 14:05:19 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
