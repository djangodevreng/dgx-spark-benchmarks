# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-04 14:07:38
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:----------------|--------------:|---------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| qwen3.6-27b-fp8 |  pp25000 (c5) | 1658.26 ± 6.15 | 731.35 ± 452.19 |               |                  |  41821.31 ± 19086.88 |  41669.08 ± 19086.88 |  41822.05 ± 19087.07 |
| qwen3.6-27b-fp8 |    tg256 (c5) |   14.03 ± 0.16 |     4.58 ± 1.38 |  35.00 ± 0.00 |      7.80 ± 0.40 |                      |                      |                      |
| qwen3.6-27b-fp8 | pp25000 (c10) | 1617.11 ± 7.84 | 470.47 ± 408.59 |               |                  |  76532.34 ± 39956.27 |  76380.11 ± 39956.27 |  76532.97 ± 39956.00 |
| qwen3.6-27b-fp8 |   tg256 (c10) |   15.30 ± 0.03 |     3.07 ± 1.37 |  70.00 ± 0.00 |      7.40 ± 0.49 |                      |                      |                      |
| qwen3.6-27b-fp8 | pp25000 (c20) | 1563.43 ± 7.46 | 286.71 ± 339.59 |               |                  | 149347.07 ± 83463.73 | 149194.83 ± 83463.73 | 149348.40 ± 83463.77 |
| qwen3.6-27b-fp8 |   tg256 (c20) |   15.89 ± 0.14 |     1.96 ± 1.22 | 100.00 ± 0.00 |      6.45 ± 1.02 |                      |                      |                      |

llama-benchy (0.3.7)
date: 2026-05-04 13:36:15 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
