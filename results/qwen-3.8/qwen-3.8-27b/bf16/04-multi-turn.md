# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-15 16:06:58
**Profile:** bf16
**Model:** Qwen/Qwen3.8-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |              test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |      est_ppt (ms) |      e2e_ttft (ms) |
|:-----------------|------------------:|----------------:|----------------:|-------------:|-----------------:|-------------------:|------------------:|-------------------:|
| qwen3.8-27b-bf16 |  pp2048 @ d4 (c1) | 1383.06 ± 20.66 | 1383.06 ± 20.66 |              |                  |    1684.51 ± 48.40 |   1372.32 ± 48.40 |    1684.51 ± 48.40 |
| qwen3.8-27b-bf16 |   tg512 @ d4 (c1) |     4.50 ± 0.00 |     4.50 ± 0.00 |  5.00 ± 0.00 |      5.00 ± 0.00 |                    |                   |                    |
| qwen3.8-27b-bf16 |  pp2048 @ d4 (c5) | 1146.25 ± 15.89 | 443.78 ± 249.47 |              |                  |  5767.29 ± 2174.23 | 5455.09 ± 2174.23 |  5767.29 ± 2174.23 |
| qwen3.8-27b-bf16 |   tg512 @ d4 (c5) |    20.12 ± 0.02 |     4.15 ± 0.06 | 25.00 ± 0.00 |      5.00 ± 0.00 |                    |                   |                    |
| qwen3.8-27b-bf16 | pp2048 @ d4 (c10) |  1135.66 ± 4.93 | 286.01 ± 232.79 |              |                  | 10258.78 ± 4821.20 | 9946.58 ± 4821.20 | 10258.78 ± 4821.20 |
| qwen3.8-27b-bf16 |  tg512 @ d4 (c10) |    36.39 ± 0.03 |     3.89 ± 0.12 | 50.00 ± 0.00 |      5.00 ± 0.00 |                    |                   |                    |

llama-benchy (0.4.0)
date: 2026-08-15 15:40:42 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
