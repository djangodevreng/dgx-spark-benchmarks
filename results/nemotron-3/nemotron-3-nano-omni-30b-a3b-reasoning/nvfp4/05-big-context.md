# Test 05-big-context — Context scaling 4k tot 25k, c=1/5/10

**Generated:** 2026-08-07 13:03:45
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 4096 8192 16384 25000 --tg 256 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                          |          test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:-------------------------------|--------------:|-----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-3-nano-omni-30b-nvfp4 |   pp4096 (c1) |  5555.00 ± 27.25 |   5555.00 ± 27.25 |               |                  |      721.40 ± 8.88 |      664.81 ± 8.88 |      721.40 ± 8.88 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c1) |     64.25 ± 0.03 |      64.25 ± 0.03 |  65.00 ± 0.00 |     65.00 ± 0.00 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |   pp4096 (c5) |  6508.76 ± 10.67 | 2307.62 ± 1412.70 |               |                  |   2108.31 ± 761.26 |   2051.72 ± 761.26 |   2108.31 ± 761.26 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c5) |    126.23 ± 0.26 |      29.33 ± 2.36 | 168.33 ± 2.36 |     33.67 ± 0.47 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |  pp4096 (c10) |  6911.21 ± 80.93 | 1638.65 ± 1325.93 |               |                  |  3350.97 ± 1558.99 |  3294.38 ± 1558.99 |  3350.97 ± 1558.99 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg256 (c10) |    159.97 ± 4.53 |      19.81 ± 2.89 | 253.33 ± 4.71 |     25.33 ± 0.47 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |   pp8192 (c1) | 6342.49 ± 327.82 |  6342.49 ± 327.82 |               |                  |    1231.70 ± 58.28 |    1175.11 ± 58.28 |    1231.70 ± 58.28 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c1) |     64.07 ± 0.02 |      64.07 ± 0.02 |  65.00 ± 0.00 |     65.00 ± 0.00 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |   pp8192 (c5) |  6984.96 ± 84.20 | 2846.55 ± 1617.06 |               |                  |  3443.00 ± 1459.20 |  3386.41 ± 1459.20 |  3443.00 ± 1459.20 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c5) |    105.67 ± 0.38 |      26.18 ± 3.80 | 166.67 ± 2.36 |     33.40 ± 0.49 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |  pp8192 (c10) |  7451.26 ± 97.33 | 1848.41 ± 1454.96 |               |                  |  5943.88 ± 2872.21 |  5887.29 ± 2872.21 |  5943.88 ± 2872.21 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg256 (c10) |    128.79 ± 0.48 |      17.51 ± 3.32 | 240.00 ± 0.00 |     24.47 ± 0.81 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |  pp16384 (c1) |  6703.91 ± 53.05 |   6703.91 ± 53.05 |               |                  |    2275.02 ± 20.93 |    2218.43 ± 20.93 |    2276.53 ± 20.72 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c1) |     62.98 ± 0.93 |      62.98 ± 0.93 |  64.67 ± 0.47 |     64.67 ± 0.47 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |  pp16384 (c5) |  7427.39 ± 39.40 | 3122.52 ± 1940.91 |               |                  |  6355.38 ± 2817.55 |  6298.79 ± 2817.55 |  6355.73 ± 2817.10 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c5) |     78.29 ± 1.37 |      23.34 ± 5.85 | 160.67 ± 4.19 |     36.40 ± 4.42 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 | pp16384 (c10) |  7532.37 ± 38.14 | 2047.05 ± 1780.78 |               |                  | 11275.71 ± 5587.05 | 11219.12 ± 5587.05 | 11276.63 ± 5587.03 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg256 (c10) |     85.99 ± 2.13 |      14.21 ± 4.47 | 233.33 ± 4.71 |     26.50 ± 3.22 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |  pp25000 (c1) |  6751.79 ± 59.06 |   6751.79 ± 59.06 |               |                  |    3413.87 ± 47.21 |    3357.28 ± 47.21 |    3415.85 ± 46.99 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c1) |     63.09 ± 0.29 |      63.09 ± 0.29 |  64.33 ± 0.47 |     64.33 ± 0.47 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 |  pp25000 (c5) |  7220.34 ± 19.21 | 3121.72 ± 1970.69 |               |                  |  9812.48 ± 4400.72 |  9755.89 ± 4400.72 |  9813.28 ± 4401.05 |
| nemotron-3-nano-omni-30b-nvfp4 |    tg256 (c5) |     59.22 ± 1.46 |      20.86 ± 8.44 | 164.00 ± 0.00 |     39.73 ± 4.11 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 | pp25000 (c10) |   7304.27 ± 9.33 | 2019.36 ± 1740.42 |               |                  | 17378.07 ± 8736.95 | 17321.48 ± 8736.95 | 17380.05 ± 8736.70 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg256 (c10) |     62.38 ± 0.24 |      11.66 ± 4.93 | 229.67 ± 0.47 |     26.73 ± 3.18 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-07 12:50:33 | latency mode: generation

---

Volledige log in `05-big-context.log`. Server-config in `meta.json`.
