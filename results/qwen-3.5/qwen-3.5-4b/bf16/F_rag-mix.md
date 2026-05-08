# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-07 21:32:16
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.5-4b-bf16 |  pp8192 (c5) | 6508.30 ± 25.05 | 2809.48 ± 1647.21 |               |                  |  3528.57 ± 1552.50 |  3469.26 ± 1552.50 |  3528.57 ± 1552.50 |
| qwen3.5-4b-bf16 |   tg512 (c5) |    95.91 ± 0.02 |      21.29 ± 1.17 | 120.00 ± 0.00 |     24.00 ± 0.00 |                    |                    |                    |
| qwen3.5-4b-bf16 | pp8192 (c10) | 6403.72 ± 13.25 | 1785.37 ± 1489.73 |               |                  |  6454.42 ± 3262.98 |  6395.10 ± 3262.98 |  6454.42 ± 3262.98 |
| qwen3.5-4b-bf16 |  tg512 (c10) |   146.81 ± 0.20 |      17.81 ± 1.75 | 210.00 ± 0.00 |     22.30 ± 1.10 |                    |                    |                    |
| qwen3.5-4b-bf16 | pp8192 (c20) | 6145.53 ± 19.29 | 1062.63 ± 1165.32 |               |                  | 12616.50 ± 6918.96 | 12557.18 ± 6918.96 | 12616.50 ± 6918.96 |
| qwen3.5-4b-bf16 |  tg512 (c20) |   188.58 ± 0.17 |      12.59 ± 1.86 | 322.67 ± 1.89 |     19.80 ± 2.63 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-07 21:26:10 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
