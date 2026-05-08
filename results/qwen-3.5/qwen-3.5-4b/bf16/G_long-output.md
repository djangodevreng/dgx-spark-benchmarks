# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-07 21:59:51
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-4b-bf16 |   pp256 (c1) | 12407.57 ± 3534.10 | 12407.57 ± 3534.10 |               |                  |    81.16 ± 4.94 |    20.56 ± 4.94 |    81.16 ± 4.94 |
| qwen3.5-4b-bf16 |  tg4096 (c1) |       20.76 ± 0.03 |       20.76 ± 0.03 |  21.33 ± 0.47 |     21.33 ± 0.47 |                 |                 |                 |
| qwen3.5-4b-bf16 |   pp256 (c5) |   5340.37 ± 196.66 |  2621.79 ± 1478.55 |               |                  |  172.79 ± 42.76 |  112.19 ± 42.76 |  172.79 ± 42.76 |
| qwen3.5-4b-bf16 |  tg4096 (c5) |      120.90 ± 0.15 |       24.19 ± 0.03 | 125.00 ± 0.00 |     25.00 ± 0.00 |                 |                 |                 |
| qwen3.5-4b-bf16 |  pp256 (c10) |   6166.08 ± 158.45 |   1358.14 ± 858.83 |               |                  | 299.03 ± 107.11 | 238.43 ± 107.11 | 299.03 ± 107.11 |
| qwen3.5-4b-bf16 | tg4096 (c10) |      224.63 ± 0.12 |       22.48 ± 0.02 | 240.00 ± 0.00 |     24.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-07 21:32:17 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
