# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-14 00:44:33
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |              test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:-----------------|------------------:|----------------:|----------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.6-27b-bf16 |  pp2048 @ d4 (c1) | 1316.17 ± 30.40 | 1316.17 ± 30.40 |              |                  |    1671.78 ± 85.17 |    1416.80 ± 85.17 |    1671.78 ± 85.17 |
| qwen3.6-27b-bf16 |   tg512 @ d4 (c1) |     4.52 ± 0.02 |     4.52 ± 0.02 |  5.00 ± 0.00 |      5.00 ± 0.00 |                    |                    |                    |
| qwen3.6-27b-bf16 |  pp2048 @ d4 (c5) |  1117.99 ± 2.26 | 429.36 ± 237.33 |              |                  |  5693.73 ± 2171.10 |  5438.74 ± 2171.10 |  5693.73 ± 2171.10 |
| qwen3.6-27b-bf16 |   tg512 @ d4 (c5) |    20.24 ± 0.01 |     4.17 ± 0.06 | 25.00 ± 0.00 |      5.00 ± 0.00 |                    |                    |                    |
| qwen3.6-27b-bf16 | pp2048 @ d4 (c10) |  1122.73 ± 2.77 | 275.39 ± 224.95 |              |                  | 10386.33 ± 4809.98 | 10131.35 ± 4809.98 | 10386.33 ± 4809.98 |
| qwen3.6-27b-bf16 |  tg512 @ d4 (c10) |    35.72 ± 1.23 |     3.92 ± 0.12 | 50.00 ± 0.00 |      5.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-14 00:18:28 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
