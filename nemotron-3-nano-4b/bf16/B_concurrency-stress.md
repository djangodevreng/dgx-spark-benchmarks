# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-05 15:04:30
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                   |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-4b-bf16 |  pp25000 (c5) | 7670.17 ± 17.32 | 3432.19 ± 2118.96 |               |                  |   8898.09 ± 4101.50 |   8841.00 ± 4101.50 |   8898.40 ± 4101.70 |
| nemotron-3-nano-4b-bf16 |    tg256 (c5) |    58.59 ± 0.23 |      17.85 ± 4.38 | 130.00 ± 0.00 |     26.93 ± 0.93 |                     |                     |                     |
| nemotron-3-nano-4b-bf16 | pp25000 (c10) |  7532.06 ± 3.24 | 2111.27 ± 1780.07 |               |                  |  16659.84 ± 8506.74 |  16602.76 ± 8506.74 |  16660.92 ± 8506.98 |
| nemotron-3-nano-4b-bf16 |   tg256 (c10) |    66.79 ± 0.10 |      12.48 ± 4.54 | 220.00 ± 0.00 |     24.40 ± 2.20 |                     |                     |                     |
| nemotron-3-nano-4b-bf16 | pp25000 (c20) | 7309.31 ± 59.94 | 1318.65 ± 1536.49 |               |                  | 31941.47 ± 17758.33 | 31884.39 ± 17758.33 | 31942.92 ± 17758.28 |
| nemotron-3-nano-4b-bf16 |   tg256 (c20) |    70.91 ± 0.84 |       8.13 ± 4.20 | 320.00 ± 0.00 |     21.22 ± 3.93 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-05 14:57:23 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
