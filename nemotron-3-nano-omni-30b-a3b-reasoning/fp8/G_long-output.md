# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-03 11:52:47
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-omni-30b-fp8 |   pp256 (c1) | 2825.24 ± 139.57 | 2825.24 ± 139.57 |               |                  |  160.32 ± 2.47 |   80.92 ± 2.47 |   160.32 ± 2.47 |
| nemotron-3-nano-omni-30b-fp8 |  tg4096 (c1) |     49.75 ± 0.11 |     49.75 ± 0.11 |  51.00 ± 0.00 |     51.00 ± 0.00 |                |                |                 |
| nemotron-3-nano-omni-30b-fp8 |   pp256 (c5) | 3108.81 ± 140.85 | 1090.89 ± 398.07 |               |                  | 318.54 ± 68.75 | 239.14 ± 68.75 |  318.54 ± 68.75 |
| nemotron-3-nano-omni-30b-fp8 |  tg4096 (c5) |     89.46 ± 1.94 |     25.56 ± 3.52 | 120.00 ± 0.00 |     33.33 ± 9.57 |                |                |                 |
| nemotron-3-nano-omni-30b-fp8 |  pp256 (c10) |  4963.28 ± 17.87 |  693.31 ± 272.61 |               |                  | 448.74 ± 75.73 | 369.34 ± 75.73 |  448.74 ± 75.73 |
| nemotron-3-nano-omni-30b-fp8 | tg4096 (c10) |     94.62 ± 5.83 |     18.40 ± 4.88 | 180.00 ± 8.16 |    26.53 ± 10.34 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-03 11:40:44 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
