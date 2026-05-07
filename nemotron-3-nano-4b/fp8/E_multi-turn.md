# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-05 17:05:47
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                  |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |    est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------|------------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|----------------:|-----------------:|
| nemotron-3-nano-4b-fp8 |  pp2048 @ d4 (c1) | 8413.07 ± 2369.60 | 8413.07 ± 2369.60 |               |                  |   289.89 ± 85.03 |  237.79 ± 85.03 |   289.89 ± 85.03 |
| nemotron-3-nano-4b-fp8 |   tg512 @ d4 (c1) |      42.65 ± 0.41 |      42.65 ± 0.41 |  46.33 ± 2.05 |     46.33 ± 2.05 |                  |                 |                  |
| nemotron-3-nano-4b-fp8 |  pp2048 @ d4 (c5) | 10378.13 ± 385.09 | 4415.87 ± 2649.02 |               |                  |  611.52 ± 241.26 | 559.41 ± 241.26 |  611.52 ± 241.26 |
| nemotron-3-nano-4b-fp8 |   tg512 @ d4 (c5) |     184.91 ± 5.34 |      39.05 ± 0.87 | 205.00 ± 0.00 |     41.27 ± 0.44 |                  |                 |                  |
| nemotron-3-nano-4b-fp8 | pp2048 @ d4 (c10) |  10844.80 ± 43.29 | 2937.66 ± 2542.72 |               |                  | 1038.12 ± 496.47 | 986.01 ± 496.47 | 1038.12 ± 496.47 |
| nemotron-3-nano-4b-fp8 |  tg512 @ d4 (c10) |     306.60 ± 9.01 |      33.27 ± 1.30 | 350.00 ± 0.00 |     35.83 ± 0.97 |                  |                 |                  |

llama-benchy (0.3.7)
date: 2026-05-05 17:03:37 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
