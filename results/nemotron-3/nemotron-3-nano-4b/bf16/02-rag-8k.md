# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-06 05:45:16
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                   |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-3-nano-4b-bf16 |  pp8192 (c5) | 7464.13 ± 44.55 | 3256.35 ± 1946.53 |               |                  |  3084.35 ± 1349.98 |  3014.43 ± 1349.98 |  3084.35 ± 1349.98 |
| nemotron-3-nano-4b-bf16 |   tg512 (c5) |   109.82 ± 0.43 |      24.36 ± 1.35 | 139.33 ± 0.47 |     27.93 ± 0.25 |                    |                    |                    |
| nemotron-3-nano-4b-bf16 | pp8192 (c10) | 7459.59 ± 12.21 | 2120.52 ± 1830.86 |               |                  |  5545.75 ± 2811.14 |  5475.83 ± 2811.14 |  5545.75 ± 2811.14 |
| nemotron-3-nano-4b-bf16 |  tg512 (c10) |   161.25 ± 5.47 |      19.96 ± 1.87 | 243.00 ± 4.24 |     25.43 ± 1.20 |                    |                    |                    |
| nemotron-3-nano-4b-bf16 | pp8192 (c20) | 7289.01 ± 37.69 | 1306.51 ± 1527.26 |               |                  | 10574.31 ± 5811.50 | 10504.39 ± 5811.50 | 10574.31 ± 5811.50 |
| nemotron-3-nano-4b-bf16 |  tg512 (c20) |   207.09 ± 2.25 |      13.77 ± 1.88 | 366.67 ± 9.43 |     21.92 ± 3.22 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-06 05:38:08 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
