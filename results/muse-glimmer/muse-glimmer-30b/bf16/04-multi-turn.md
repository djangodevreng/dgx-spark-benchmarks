# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-12 08:05:16
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------------|------------------:|----------------:|----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| muse-glimmer-30b-bf16 |  pp2048 @ d4 (c1) | 1819.81 ± 23.07 | 1819.81 ± 23.07 |              |                  |   1287.43 ± 56.35 |   1022.04 ± 56.35 |  2134.69 ± 205.37 |
| muse-glimmer-30b-bf16 |   tg512 @ d4 (c1) |     4.27 ± 0.02 |     4.27 ± 0.02 |  5.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| muse-glimmer-30b-bf16 |  pp2048 @ d4 (c5) | 1413.61 ± 30.30 | 646.37 ± 584.19 |              |                  | 4706.88 ± 1755.03 | 4441.50 ± 1755.03 |  6485.87 ± 145.87 |
| muse-glimmer-30b-bf16 |   tg512 @ d4 (c5) |    20.73 ± 0.07 |     4.16 ± 0.03 | 25.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| muse-glimmer-30b-bf16 | pp2048 @ d4 (c10) |  1441.48 ± 5.58 | 398.76 ± 474.49 |              |                  | 8327.32 ± 3592.25 | 8061.93 ± 3592.25 | 12691.49 ± 225.97 |
| muse-glimmer-30b-bf16 |  tg512 @ d4 (c10) |    39.74 ± 0.14 |     4.00 ± 0.04 | 50.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-12 07:39:10 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
