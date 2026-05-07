# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-05 15:28:24
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                   |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-nano-4b-bf16 |  pp8192 (c5) | 8207.56 ± 31.13 | 3548.98 ± 2136.56 |               |                  | 2835.89 ± 1233.45 | 2776.54 ± 1233.45 | 2835.89 ± 1233.45 |
| nemotron-3-nano-4b-bf16 |   tg512 (c5) |   111.93 ± 0.14 |      24.68 ± 1.24 | 135.00 ± 0.00 |     27.40 ± 0.49 |                   |                   |                   |
| nemotron-3-nano-4b-bf16 | pp8192 (c10) | 8157.72 ± 12.18 | 2246.95 ± 1886.05 |               |                  | 5090.23 ± 2545.87 | 5030.88 ± 2545.87 | 5090.23 ± 2545.87 |
| nemotron-3-nano-4b-bf16 |  tg512 (c10) |   165.60 ± 4.76 |      20.51 ± 1.98 | 240.00 ± 0.00 |     25.50 ± 1.23 |                   |                   |                   |
| nemotron-3-nano-4b-bf16 | pp8192 (c20) | 8004.73 ± 24.60 | 1384.47 ± 1568.57 |               |                  | 9765.66 ± 5304.09 | 9706.31 ± 5304.09 | 9765.66 ± 5304.09 |
| nemotron-3-nano-4b-bf16 |  tg512 (c20) |   223.68 ± 2.73 |      15.14 ± 2.29 | 380.00 ± 0.00 |     22.63 ± 2.58 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-05 15:23:22 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
