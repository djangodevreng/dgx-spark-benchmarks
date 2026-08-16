# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-13 20:49:01
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|-------------:|----------------:|----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-27b-bf16 |  pp1024 (c1) | 955.71 ± 147.38 | 955.71 ± 147.38 |              |                  |  1284.04 ± 217.39 |  1005.27 ± 217.39 |  1284.04 ± 217.39 |
| qwen3.6-27b-bf16 |  tg1024 (c1) |     4.54 ± 0.00 |     4.54 ± 0.00 |  5.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-bf16 |  pp1024 (c5) |  1076.53 ± 0.95 | 335.42 ± 148.18 |              |                  |  3471.49 ± 957.87 |  3192.72 ± 957.87 |  3471.49 ± 957.87 |
| qwen3.6-27b-bf16 |  tg1024 (c5) |    20.86 ± 0.22 |     4.24 ± 0.02 | 25.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-bf16 | pp1024 (c10) |  1093.72 ± 1.05 | 221.63 ± 155.61 |              |                  | 5883.41 ± 2248.31 | 5604.63 ± 2248.31 | 5883.41 ± 2248.31 |
| qwen3.6-27b-bf16 | tg1024 (c10) |    39.82 ± 0.01 |     4.06 ± 0.03 | 50.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-13 19:59:55 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
