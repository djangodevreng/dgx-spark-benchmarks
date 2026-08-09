# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-07 17:15:42
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|------------------:|------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.5-4b-bf16 |   pp256 (c1) | 8748.10 ± 1136.02 | 8748.10 ± 1136.02 |               |                  |   85.44 ± 3.71 |   27.86 ± 3.71 |    85.44 ± 3.71 |
| qwen3.5-4b-bf16 |  tg4096 (c1) |      20.57 ± 0.00 |      20.57 ± 0.00 |  21.00 ± 0.00 |     21.00 ± 0.00 |                |                |                 |
| qwen3.5-4b-bf16 |   pp256 (c5) |   4661.51 ± 22.01 | 2450.46 ± 2631.43 |               |                  | 222.60 ± 65.30 | 165.01 ± 65.30 |  222.60 ± 65.30 |
| qwen3.5-4b-bf16 |  tg4096 (c5) |     118.54 ± 0.04 |      23.73 ± 0.01 | 129.33 ± 4.19 |     25.87 ± 0.88 |                |                |                 |
| qwen3.5-4b-bf16 |  pp256 (c10) |  5308.55 ± 330.47 | 1232.08 ± 1862.42 |               |                  | 389.47 ± 98.23 | 331.89 ± 98.23 |  389.47 ± 98.23 |
| qwen3.5-4b-bf16 | tg4096 (c10) |     219.32 ± 1.43 |      22.10 ± 0.05 | 246.67 ± 4.71 |     24.67 ± 0.47 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-07 16:38:25 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
