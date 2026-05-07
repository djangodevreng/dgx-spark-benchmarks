# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-03 14:15:53
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                         |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:------------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-omni-30b-bf16 |   pp256 (c1) | 1695.44 ± 119.93 | 1695.44 ± 119.93 |               |                  | 289.65 ± 10.40 | 144.22 ± 10.40 |  289.65 ± 10.40 |
| nemotron-3-nano-omni-30b-bf16 |  tg4096 (c1) |     28.68 ± 0.06 |     28.68 ± 0.06 |  29.00 ± 0.00 |     29.00 ± 0.00 |                |                |                 |
| nemotron-3-nano-omni-30b-bf16 |   pp256 (c5) |  2828.40 ± 33.37 |   879.13 ± 59.09 |               |                  |  408.98 ± 1.24 |  263.56 ± 1.24 |   408.98 ± 1.24 |
| nemotron-3-nano-omni-30b-bf16 |  tg4096 (c5) |     50.55 ± 4.71 |     14.32 ± 2.62 |  71.67 ± 2.87 |     20.47 ± 5.67 |                |                |                 |
| nemotron-3-nano-omni-30b-bf16 |  pp256 (c10) | 3936.06 ± 596.63 |   602.06 ± 89.50 |               |                  | 546.60 ± 79.64 | 401.18 ± 79.64 |  546.60 ± 79.64 |
| nemotron-3-nano-omni-30b-bf16 | tg4096 (c10) |     66.76 ± 3.13 |      9.51 ± 1.40 | 110.00 ± 0.00 |     15.50 ± 6.08 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-03 14:00:55 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
