# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-03 10:12:53
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                          |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-------------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-omni-30b-nvfp4 |   pp256 (c1) | 2122.29 ± 243.36 | 2122.29 ± 243.36 |               |                  | 179.13 ± 18.13 | 114.05 ± 18.13 |  179.13 ± 18.13 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg4096 (c1) |     55.44 ± 0.14 |     55.44 ± 0.14 |  56.67 ± 0.47 |     56.67 ± 0.47 |                |                |                 |
| nemotron-3-nano-omni-30b-nvfp4 |   pp256 (c5) | 2617.86 ± 265.83 |  664.34 ± 110.82 |               |                  | 427.08 ± 63.58 | 362.00 ± 63.58 |  427.08 ± 63.58 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg4096 (c5) |   107.10 ± 12.19 |     34.63 ± 4.65 | 155.00 ± 0.00 |     41.87 ± 8.80 |                |                |                 |
| nemotron-3-nano-omni-30b-nvfp4 |  pp256 (c10) |  5974.74 ± 44.17 |  831.62 ± 269.66 |               |                  | 362.73 ± 57.67 | 297.65 ± 57.67 |  362.73 ± 57.67 |
| nemotron-3-nano-omni-30b-nvfp4 | tg4096 (c10) |   172.29 ± 15.99 |     25.18 ± 2.89 | 246.67 ± 4.71 |     34.00 ± 9.25 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-03 10:06:05 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
