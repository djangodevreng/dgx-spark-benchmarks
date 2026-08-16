# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-15 12:30:41
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|----------------:|-------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.8-27b-bf16 |  pp8192 (c5) | 1118.05 ± 4.52 | 463.80 ± 275.64 |              |                  |  21245.13 ± 8955.39 |  20865.04 ± 8955.39 |  21245.13 ± 8955.39 |
| qwen3.8-27b-bf16 |   tg512 (c5) |   17.26 ± 0.05 |     3.85 ± 0.22 | 25.00 ± 0.00 |      5.00 ± 0.00 |                     |                     |                     |
| qwen3.8-27b-bf16 | pp8192 (c10) | 1118.96 ± 1.32 | 303.85 ± 252.08 |              |                  | 37787.48 ± 18871.84 | 37407.39 ± 18871.84 | 37787.48 ± 18871.84 |
| qwen3.8-27b-bf16 |  tg512 (c10) |   27.16 ± 0.03 |     3.35 ± 0.36 | 42.33 ± 0.47 |      4.80 ± 0.40 |                     |                     |                     |
| qwen3.8-27b-bf16 | pp8192 (c20) | 1106.49 ± 3.38 | 188.52 ± 214.28 |              |                  | 71532.18 ± 38610.78 | 71152.09 ± 38610.78 | 71532.18 ± 38610.78 |
| qwen3.8-27b-bf16 |  tg512 (c20) |   34.69 ± 0.10 |     2.35 ± 0.36 | 72.00 ± 5.72 |      4.28 ± 0.66 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-15 11:46:49 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
