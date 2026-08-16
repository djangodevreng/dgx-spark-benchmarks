# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-15 11:46:49
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|-------------:|-----------------:|-----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.8-27b-bf16 |  pp1024 (c1) | 1094.68 ± 115.70 | 1094.68 ± 115.70 |              |                  |   1240.99 ± 79.48 |    853.09 ± 79.48 |   1240.99 ± 79.48 |
| qwen3.8-27b-bf16 |  tg1024 (c1) |      4.50 ± 0.00 |      4.50 ± 0.00 |  5.67 ± 0.47 |      5.67 ± 0.47 |                   |                   |                   |
| qwen3.8-27b-bf16 |  pp1024 (c5) |   1078.90 ± 9.18 |  353.60 ± 174.27 |              |                  |  3479.10 ± 942.85 |  3091.20 ± 942.85 |  3479.10 ± 942.85 |
| qwen3.8-27b-bf16 |  tg1024 (c5) |     20.61 ± 0.03 |      4.18 ± 0.03 | 25.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| qwen3.8-27b-bf16 | pp1024 (c10) |  1069.15 ± 24.70 |  220.97 ± 167.28 |              |                  | 6085.79 ± 2265.30 | 5697.89 ± 2265.30 | 6085.79 ± 2265.30 |
| qwen3.8-27b-bf16 | tg1024 (c10) |     39.14 ± 0.04 |      3.99 ± 0.03 | 50.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-15 10:57:18 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
