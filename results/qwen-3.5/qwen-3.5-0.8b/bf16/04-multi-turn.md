# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-07 09:29:05
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |              test |       t/s (total) |          t/s (req) |       peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|------------------:|------------------:|-------------------:|---------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-0.8b-bf16 |  pp2048 @ d4 (c1) | 30126.99 ± 656.43 |  30126.99 ± 656.43 |                |                  |    83.02 ± 2.69 |    60.69 ± 2.69 |    83.02 ± 2.69 |
| qwen3.5-0.8b-bf16 |   tg512 @ d4 (c1) |     114.12 ± 0.02 |      114.12 ± 0.02 |  115.00 ± 0.00 |    115.00 ± 0.00 |                 |                 |                 |
| qwen3.5-0.8b-bf16 |  pp2048 @ d4 (c5) | 26540.97 ± 279.39 | 12638.65 ± 8390.49 |                |                  |  229.80 ± 96.04 |  207.47 ± 96.04 |  229.80 ± 96.04 |
| qwen3.5-0.8b-bf16 |   tg512 @ d4 (c5) |    449.99 ± 66.36 |     106.73 ± 14.47 | 536.67 ± 40.07 |   112.51 ± 15.14 |                 |                 |                 |
| qwen3.5-0.8b-bf16 | pp2048 @ d4 (c10) |  26510.42 ± 55.88 |  7731.92 ± 7074.60 |                |                  | 416.80 ± 204.89 | 394.47 ± 204.89 | 416.80 ± 204.89 |
| qwen3.5-0.8b-bf16 |  tg512 @ d4 (c10) |    756.71 ± 19.93 |       95.60 ± 4.98 | 973.67 ± 17.13 |    105.09 ± 4.41 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 09:28:04 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
