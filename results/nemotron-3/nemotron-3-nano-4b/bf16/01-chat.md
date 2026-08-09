# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-06 05:38:08
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-4b-bf16 |  pp1024 (c1) | 3241.16 ± 862.10 |  3241.16 ± 862.10 |               |                  |  372.67 ± 99.39 |  307.39 ± 99.39 |  372.67 ± 99.39 |
| nemotron-3-nano-4b-bf16 |  tg1024 (c1) |     24.94 ± 0.07 |      24.94 ± 0.07 |  27.00 ± 0.82 |     27.00 ± 0.82 |                 |                 |                 |
| nemotron-3-nano-4b-bf16 |  pp1024 (c5) | 6254.72 ± 352.20 | 2707.58 ± 2083.89 |               |                  | 544.92 ± 197.58 | 479.64 ± 197.58 | 544.92 ± 197.58 |
| nemotron-3-nano-4b-bf16 |  tg1024 (c5) |    124.73 ± 3.76 |      27.24 ± 0.14 | 140.00 ± 0.00 |     28.80 ± 0.40 |                 |                 |                 |
| nemotron-3-nano-4b-bf16 | pp1024 (c10) | 6903.03 ± 142.95 | 1779.01 ± 1622.99 |               |                  | 883.21 ± 385.12 | 817.93 ± 385.12 | 883.21 ± 385.12 |
| nemotron-3-nano-4b-bf16 | tg1024 (c10) |    224.49 ± 8.29 |      24.14 ± 0.35 | 253.00 ± 4.24 |     26.10 ± 0.60 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-06 05:30:03 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
