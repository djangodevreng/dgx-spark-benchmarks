# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-08 11:55:56
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-bf16 |  pp1024 (c1) | 1802.37 ± 458.50 | 1802.37 ± 458.50 |               |                  |  675.61 ± 185.10 |  545.45 ± 185.10 |  675.61 ± 185.10 |
| qwen3.6-35b-a3b-bf16 |  tg1024 (c1) |     30.49 ± 0.05 |     30.49 ± 0.05 |  33.67 ± 0.94 |     33.67 ± 0.94 |                  |                  |                  |
| qwen3.6-35b-a3b-bf16 |  pp1024 (c5) |  3042.99 ± 21.01 |  970.62 ± 436.62 |               |                  | 1203.16 ± 310.02 | 1072.99 ± 310.02 | 1203.16 ± 310.02 |
| qwen3.6-35b-a3b-bf16 |  tg1024 (c5) |     64.61 ± 2.16 |     13.02 ± 0.44 |  80.00 ± 4.08 |     16.00 ± 0.82 |                  |                  |                  |
| qwen3.6-35b-a3b-bf16 | pp1024 (c10) |  3279.72 ± 29.82 |  689.10 ± 467.58 |               |                  | 1903.25 ± 706.50 | 1773.08 ± 706.50 | 1903.25 ± 706.50 |
| qwen3.6-35b-a3b-bf16 | tg1024 (c10) |     84.61 ± 0.82 |      8.63 ± 0.19 | 110.67 ± 0.94 |     11.80 ± 1.33 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-08 11:40:12 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
