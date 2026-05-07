# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-07 14:21:32
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------|-------------:|------------------:|------------------:|---------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.5-2b-bf16 |  pp8192 (c5) |  15269.62 ± 78.57 | 6406.16 ± 3623.18 |                |                  |  1546.48 ± 642.37 |  1495.05 ± 642.37 |  1546.48 ± 642.37 |
| qwen3.5-2b-bf16 |   tg512 (c5) |     186.27 ± 7.96 |     44.82 ± 10.50 | 242.67 ± 18.87 |    49.80 ± 10.94 |                   |                   |                   |
| qwen3.5-2b-bf16 | pp8192 (c10) | 15219.24 ± 207.37 | 4205.62 ± 3484.59 |                |                  | 2737.85 ± 1360.00 | 2686.42 ± 1360.00 | 2737.85 ± 1360.00 |
| qwen3.5-2b-bf16 |  tg512 (c10) |    283.16 ± 34.16 |      38.67 ± 6.54 | 461.33 ± 12.26 |     47.83 ± 5.96 |                   |                   |                   |
| qwen3.5-2b-bf16 | pp8192 (c20) | 14661.84 ± 190.96 | 2519.07 ± 2800.47 |                |                  | 5312.04 ± 2880.61 | 5260.61 ± 2880.61 | 5312.04 ± 2880.61 |
| qwen3.5-2b-bf16 |  tg512 (c20) |    376.04 ± 22.50 |      28.30 ± 7.78 | 733.67 ± 23.98 |     42.77 ± 7.41 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-07 14:18:58 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
