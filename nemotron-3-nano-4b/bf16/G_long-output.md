# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-05 15:43:57
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:------------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-4b-bf16 |   pp256 (c1) | 10612.21 ± 663.22 | 10612.21 ± 663.22 |               |                  |  77.59 ± 12.98 |  15.02 ± 10.62 |   77.59 ± 12.98 |
| nemotron-3-nano-4b-bf16 |  tg4096 (c1) |      25.70 ± 0.03 |      25.70 ± 0.03 |  26.00 ± 0.00 |     26.00 ± 0.00 |                |                |                 |
| nemotron-3-nano-4b-bf16 |   pp256 (c5) |  6455.57 ± 260.29 |  2035.38 ± 158.61 |               |                  |  177.39 ± 4.22 |  113.15 ± 4.22 |   177.39 ± 4.22 |
| nemotron-3-nano-4b-bf16 |  tg4096 (c5) |      59.29 ± 9.26 |      27.73 ± 0.54 | 140.00 ± 0.00 |     29.33 ± 0.79 |                |                |                 |
| nemotron-3-nano-4b-bf16 |  pp256 (c10) |  6610.10 ± 239.18 | 1258.11 ± 1673.32 |               |                  | 302.28 ± 45.00 | 238.05 ± 45.00 |  302.28 ± 45.00 |
| nemotron-3-nano-4b-bf16 | tg4096 (c10) |     96.05 ± 10.59 |      25.64 ± 0.82 | 253.33 ± 4.71 |     27.77 ± 1.63 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-05 15:28:24 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
