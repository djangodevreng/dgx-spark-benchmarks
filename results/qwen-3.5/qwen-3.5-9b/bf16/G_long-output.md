# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-09 16:07:52
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-9b-bf16 |   pp256 (c1) | 6399.44 ± 1965.51 | 6399.44 ± 1965.51 |               |                  |   131.81 ± 8.87 |    39.39 ± 8.87 |   131.81 ± 8.87 |
| qwen3.5-9b-bf16 |  tg4096 (c1) |      12.66 ± 0.01 |      12.66 ± 0.01 |  13.00 ± 0.00 |     13.00 ± 0.00 |                 |                 |                 |
| qwen3.5-9b-bf16 |   pp256 (c5) |   3456.84 ± 92.69 | 2091.34 ± 1792.24 |               |                  |  278.64 ± 92.11 |  186.22 ± 92.11 |  278.64 ± 92.11 |
| qwen3.5-9b-bf16 |  tg4096 (c5) |      64.64 ± 2.77 |      13.34 ± 0.02 |  70.00 ± 0.00 |     14.00 ± 0.00 |                 |                 |                 |
| qwen3.5-9b-bf16 |  pp256 (c10) |    3761.19 ± 9.50 |   945.42 ± 900.50 |               |                  | 503.91 ± 187.97 | 411.49 ± 187.97 | 503.91 ± 187.97 |
| qwen3.5-9b-bf16 | tg4096 (c10) |     126.67 ± 0.54 |      12.76 ± 0.01 | 140.00 ± 0.00 |     14.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-09 15:20:06 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
