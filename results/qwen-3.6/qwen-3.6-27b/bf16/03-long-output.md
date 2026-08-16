# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-14 00:18:28
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------|-------------:|-----------------:|-----------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-27b-bf16 |   pp256 (c1) | 1218.65 ± 644.48 | 1218.65 ± 644.48 |              |                  |   502.31 ± 96.72 |   247.50 ± 96.72 |   502.31 ± 96.72 |
| qwen3.6-27b-bf16 |  tg4096 (c1) |      4.54 ± 0.00 |      4.54 ± 0.00 |  5.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| qwen3.6-27b-bf16 |   pp256 (c5) |   879.71 ± 16.44 |  267.68 ± 106.16 |              |                  | 1226.75 ± 229.03 |  971.94 ± 229.03 | 1226.75 ± 229.03 |
| qwen3.6-27b-bf16 |  tg4096 (c5) |     12.93 ± 1.71 |      4.29 ± 0.05 | 25.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| qwen3.6-27b-bf16 |  pp256 (c10) |  1001.61 ± 36.65 |   132.49 ± 45.76 |              |                  | 2111.93 ± 341.31 | 1857.12 ± 341.31 | 2111.93 ± 341.31 |
| qwen3.6-27b-bf16 | tg4096 (c10) |     30.92 ± 2.98 |      4.13 ± 0.03 | 50.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-13 21:33:09 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
