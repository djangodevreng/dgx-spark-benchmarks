# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-07 16:30:02
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-4b-bf16 |  pp1024 (c1) | 2556.15 ± 782.12 |  2556.15 ± 782.12 |               |                  | 499.42 ± 151.32 | 422.46 ± 151.32 | 499.42 ± 151.32 |
| qwen3.5-4b-bf16 |  tg1024 (c1) |     20.54 ± 0.03 |      20.54 ± 0.03 |  23.00 ± 0.82 |     23.00 ± 0.82 |                 |                 |                 |
| qwen3.5-4b-bf16 |  pp1024 (c5) | 5463.50 ± 188.97 | 2592.91 ± 1966.24 |               |                  | 599.44 ± 237.84 | 522.49 ± 237.84 | 599.44 ± 237.84 |
| qwen3.5-4b-bf16 |  tg1024 (c5) |    117.89 ± 0.07 |      23.81 ± 0.11 | 126.67 ± 2.36 |     25.33 ± 0.47 |                 |                 |                 |
| qwen3.5-4b-bf16 | pp1024 (c10) |  6024.65 ± 25.94 | 1695.97 ± 1760.73 |               |                  | 986.71 ± 440.63 | 909.76 ± 440.63 | 986.71 ± 440.63 |
| qwen3.5-4b-bf16 | tg1024 (c10) |    216.04 ± 2.63 |      22.02 ± 0.33 | 240.00 ± 8.16 |     24.00 ± 0.82 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 16:20:27 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
