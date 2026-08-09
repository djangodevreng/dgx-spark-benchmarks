# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-07 12:47:18
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                          |         test |       t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-------------------------------|-------------:|------------------:|-----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-omni-30b-nvfp4 |   pp256 (c1) |  4192.32 ± 256.61 | 4192.32 ± 256.61 |               |                  |   110.59 ± 0.97 |    55.28 ± 0.97 |   110.59 ± 0.97 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg4096 (c1) |      63.98 ± 0.28 |     63.98 ± 0.28 |  65.00 ± 0.00 |     65.00 ± 0.00 |                 |                 |                 |
| nemotron-3-nano-omni-30b-nvfp4 |   pp256 (c5) | 2662.83 ± 1052.95 |  720.83 ± 489.89 |               |                  | 466.90 ± 155.05 | 411.59 ± 155.05 | 466.90 ± 155.05 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg4096 (c5) |    116.08 ± 14.55 |     38.82 ± 6.28 | 171.00 ± 1.41 |    47.93 ± 11.02 |                 |                 |                 |
| nemotron-3-nano-omni-30b-nvfp4 |  pp256 (c10) |   2774.59 ± 67.52 |   310.78 ± 47.01 |               |                  |  821.07 ± 75.21 |  765.76 ± 75.21 |  821.07 ± 75.21 |
| nemotron-3-nano-omni-30b-nvfp4 | tg4096 (c10) |     159.47 ± 5.22 |     29.15 ± 4.91 | 266.67 ± 4.71 |    38.43 ± 11.94 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 12:37:00 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
