# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-09 20:39:36
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-27b-bf16 |  pp1024 (c1) | 1761.70 ± 9.65 |  1761.70 ± 9.65 |              |                  |     777.98 ± 6.71 |     522.45 ± 6.71 |     777.98 ± 6.71 |
| qwen3.6-27b-bf16 |  tg1024 (c1) |    4.43 ± 0.00 |     4.43 ± 0.00 |  5.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-bf16 |  pp1024 (c5) | 1302.65 ± 8.17 | 380.54 ± 101.57 |              |                  |  2890.67 ± 621.35 |  2635.14 ± 621.35 |  2890.67 ± 621.35 |
| qwen3.6-27b-bf16 |  tg1024 (c5) |   20.79 ± 0.05 |     4.17 ± 0.02 | 25.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-bf16 | pp1024 (c10) | 1316.28 ± 9.99 | 247.17 ± 130.29 |              |                  | 4883.58 ± 1798.06 | 4628.05 ± 1798.06 | 4883.58 ± 1798.06 |
| qwen3.6-27b-bf16 | tg1024 (c10) |   39.63 ± 0.01 |     4.01 ± 0.02 | 50.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-09 20:02:11 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
