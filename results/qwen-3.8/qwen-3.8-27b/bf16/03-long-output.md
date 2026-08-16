# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-15 15:40:42
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |       t/s (total) |         t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------|-------------:|------------------:|------------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.8-27b-bf16 |   pp256 (c1) | 3657.50 ± 1962.13 | 3657.50 ± 1962.13 |              |                  |   427.81 ± 96.87 |   116.25 ± 96.87 |   427.81 ± 96.87 |
| qwen3.8-27b-bf16 |  tg4096 (c1) |       4.50 ± 0.00 |       4.50 ± 0.00 |  5.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| qwen3.8-27b-bf16 |   pp256 (c5) |    846.90 ± 16.10 |   277.34 ± 108.93 |              |                  | 1218.59 ± 234.61 |  907.03 ± 234.61 | 1218.59 ± 234.61 |
| qwen3.8-27b-bf16 |  tg4096 (c5) |      21.09 ± 0.01 |       4.22 ± 0.00 | 25.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| qwen3.8-27b-bf16 |  pp256 (c10) |     907.92 ± 7.63 |    134.47 ± 54.51 |              |                  | 2140.59 ± 358.70 | 1829.03 ± 358.70 | 2140.59 ± 358.70 |
| qwen3.8-27b-bf16 | tg4096 (c10) |      37.66 ± 0.93 |       4.07 ± 0.01 | 50.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-15 12:30:42 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
