# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-13 21:33:09
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|----------------:|-------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-27b-bf16 |  pp8192 (c5) | 1109.64 ± 0.38 | 458.96 ± 266.97 |              |                  |  21228.24 ± 9019.57 |  20973.61 ± 9019.57 |  21228.24 ± 9019.57 |
| qwen3.6-27b-bf16 |   tg512 (c5) |   17.31 ± 0.01 |     3.87 ± 0.23 | 25.00 ± 0.00 |      5.00 ± 0.00 |                     |                     |                     |
| qwen3.6-27b-bf16 | pp8192 (c10) | 1110.87 ± 0.99 | 297.05 ± 240.38 |              |                  | 37901.50 ± 18916.38 | 37646.88 ± 18916.38 | 37901.50 ± 18916.38 |
| qwen3.6-27b-bf16 |  tg512 (c10) |   27.25 ± 0.08 |     3.36 ± 0.36 | 48.00 ± 2.83 |      4.93 ± 0.25 |                     |                     |                     |
| qwen3.6-27b-bf16 | pp8192 (c20) | 1100.79 ± 0.54 | 185.34 ± 206.40 |              |                  | 71852.68 ± 38787.23 | 71598.05 ± 38787.23 | 71852.68 ± 38787.23 |
| qwen3.6-27b-bf16 |  tg512 (c20) |   34.45 ± 0.11 |     2.33 ± 0.36 | 69.00 ± 2.83 |      4.28 ± 0.69 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-13 20:49:01 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
