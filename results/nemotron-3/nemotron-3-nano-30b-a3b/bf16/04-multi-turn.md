# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-09 03:51:20
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                    |              test |     t/s (total) |         t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------------|------------------:|----------------:|------------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-30b-bf16 |  pp2048 @ d4 (c1) |  5009.58 ± 9.08 |    5009.58 ± 9.08 |              |                  |    490.02 ± 1.15 |    358.45 ± 1.15 |    490.02 ± 1.15 |
| nemotron-3-nano-30b-bf16 |   tg512 @ d4 (c1) |    29.12 ± 0.08 |      29.12 ± 0.08 | 30.00 ± 0.00 |     30.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-30b-bf16 |  pp2048 @ d4 (c5) | 6028.18 ± 27.98 | 2039.99 ± 1454.74 |              |                  | 1342.49 ± 413.65 | 1210.92 ± 413.65 | 1342.49 ± 413.65 |
| nemotron-3-nano-30b-bf16 |   tg512 @ d4 (c5) |    54.96 ± 0.80 |      11.32 ± 0.37 | 66.00 ± 4.32 |     14.07 ± 1.95 |                  |                  |                  |
| nemotron-3-nano-30b-bf16 | pp2048 @ d4 (c10) | 6129.06 ± 49.99 | 1308.20 ± 1196.16 |              |                  | 2119.17 ± 773.86 | 1987.60 ± 773.86 | 2119.17 ± 773.86 |
| nemotron-3-nano-30b-bf16 |  tg512 @ d4 (c10) |    74.22 ± 0.81 |       7.63 ± 0.10 | 93.33 ± 4.71 |      9.37 ± 0.48 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-09 03:42:31 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
