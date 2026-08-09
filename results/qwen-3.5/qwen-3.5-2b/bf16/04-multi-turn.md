# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-07 14:41:59
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|------------------:|------------------:|------------------:|---------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-2b-bf16 |  pp2048 @ d4 (c1) | 16103.51 ± 730.63 | 16103.51 ± 730.63 |                |                  |   155.79 ± 3.41 |   117.75 ± 3.41 |   155.79 ± 3.41 |
| qwen3.5-2b-bf16 |   tg512 @ d4 (c1) |      42.68 ± 0.05 |      42.68 ± 0.05 |   43.33 ± 0.47 |     43.33 ± 0.47 |                 |                 |                 |
| qwen3.5-2b-bf16 |  pp2048 @ d4 (c5) | 15466.46 ± 102.20 | 7681.56 ± 5324.02 |                |                  | 387.13 ± 167.20 | 349.09 ± 167.20 | 387.13 ± 167.20 |
| qwen3.5-2b-bf16 |   tg512 @ d4 (c5) |    201.80 ± 70.51 |      51.04 ± 1.84 | 261.67 ± 11.79 |     54.05 ± 1.61 |                 |                 |                 |
| qwen3.5-2b-bf16 | pp2048 @ d4 (c10) |  15449.62 ± 29.94 | 4654.46 ± 4455.94 |                |                  | 711.85 ± 353.17 | 673.81 ± 353.17 | 711.85 ± 353.17 |
| qwen3.5-2b-bf16 |  tg512 @ d4 (c10) |    379.25 ± 41.99 |      47.90 ± 2.22 |  510.00 ± 0.00 |     52.17 ± 1.00 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 14:39:55 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
