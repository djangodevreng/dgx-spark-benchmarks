# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-07 14:27:13
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |         t/s (total) |           t/s (req) |       peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|--------------------:|--------------------:|---------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.5-2b-bf16 |   pp256 (c1) | 22051.35 ± 19810.51 | 22051.35 ± 19810.51 |                |                  |  82.86 ± 49.79 |  45.63 ± 49.79 |   82.86 ± 49.79 |
| qwen3.5-2b-bf16 |  tg4096 (c1) |        43.62 ± 0.03 |        43.62 ± 0.03 |   44.00 ± 0.00 |     44.00 ± 0.00 |                |                |                 |
| qwen3.5-2b-bf16 |   pp256 (c5) |  10101.25 ± 1696.99 |   4611.34 ± 2516.61 |                |                  | 104.52 ± 31.41 |  67.29 ± 31.41 |  104.52 ± 31.41 |
| qwen3.5-2b-bf16 |  tg4096 (c5) |       84.38 ± 20.77 |        51.82 ± 2.91 | 256.33 ± 19.33 |     55.29 ± 1.18 |                |                |                 |
| qwen3.5-2b-bf16 |  pp256 (c10) |   10684.08 ± 415.72 |   1956.75 ± 1593.70 |                |                  | 185.68 ± 36.52 | 148.45 ± 36.52 |  185.68 ± 36.52 |
| qwen3.5-2b-bf16 | tg4096 (c10) |      215.47 ± 97.33 |        50.67 ± 1.82 |  509.67 ± 0.47 |     53.40 ± 1.70 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-07 14:21:33 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
