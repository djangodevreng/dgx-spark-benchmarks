# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-05 15:10:04
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-4b-bf16 |  pp1024 (c1) | 13668.14 ± 2734.89 | 13668.14 ± 2734.89 |               |                  |  126.60 ± 15.49 |   70.03 ± 15.49 |  126.60 ± 15.49 |
| nemotron-3-nano-4b-bf16 |  tg1024 (c1) |       25.63 ± 0.04 |       25.63 ± 0.04 |  26.00 ± 0.00 |     26.00 ± 0.00 |                 |                 |                 |
| nemotron-3-nano-4b-bf16 |  pp1024 (c5) |   8023.12 ± 106.47 |  3353.47 ± 2413.12 |               |                  | 413.36 ± 139.86 | 356.79 ± 139.86 | 413.36 ± 139.86 |
| nemotron-3-nano-4b-bf16 |  tg1024 (c5) |      130.79 ± 4.18 |       27.38 ± 0.18 | 140.00 ± 0.00 |     28.53 ± 0.50 |                 |                 |                 |
| nemotron-3-nano-4b-bf16 | pp1024 (c10) |   8114.36 ± 106.71 |  1799.57 ± 1135.41 |               |                  | 746.05 ± 307.80 | 689.49 ± 307.80 | 746.05 ± 307.80 |
| nemotron-3-nano-4b-bf16 | tg1024 (c10) |      223.83 ± 7.54 |       24.75 ± 0.25 | 250.00 ± 0.00 |     26.13 ± 0.56 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-05 15:04:31 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
