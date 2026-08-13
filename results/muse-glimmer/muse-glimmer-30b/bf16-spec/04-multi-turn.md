# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-12 16:24:18
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16-spec --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                      |              test |     t/s (total) |       t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |      e2e_ttft (ms) |
|:---------------------------|------------------:|----------------:|----------------:|---------------:|-----------------:|------------------:|------------------:|-------------------:|
| muse-glimmer-30b-bf16-spec |  pp2048 @ d4 (c1) | 1578.75 ± 66.55 | 1578.75 ± 66.55 |                |                  |   1572.53 ± 58.23 |   1200.94 ± 58.23 |    1821.95 ± 58.78 |
| muse-glimmer-30b-bf16-spec |   tg512 @ d4 (c1) |    11.24 ± 1.33 |    11.24 ± 1.33 |   49.00 ± 7.48 |     49.00 ± 7.48 |                   |                   |                    |
| muse-glimmer-30b-bf16-spec |  pp2048 @ d4 (c5) | 1391.79 ± 28.48 | 658.46 ± 628.11 |                |                  | 5150.17 ± 2104.78 | 4778.58 ± 2104.78 |  5762.80 ± 1916.61 |
| muse-glimmer-30b-bf16-spec |   tg512 @ d4 (c5) |    37.79 ± 2.05 |   17.40 ± 12.48 |  213.67 ± 6.13 |     47.27 ± 8.36 |                   |                   |                    |
| muse-glimmer-30b-bf16-spec | pp2048 @ d4 (c10) |  1420.93 ± 9.07 | 314.95 ± 345.60 |                |                  | 9078.91 ± 3371.96 | 8707.33 ± 3371.96 | 11857.38 ± 2239.75 |
| muse-glimmer-30b-bf16-spec |  tg512 @ d4 (c10) |    63.92 ± 2.58 |    13.19 ± 9.16 | 329.33 ± 24.25 |     41.40 ± 9.80 |                   |                   |                    |

llama-benchy (0.4.0)
date: 2026-08-12 16:10:25 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
