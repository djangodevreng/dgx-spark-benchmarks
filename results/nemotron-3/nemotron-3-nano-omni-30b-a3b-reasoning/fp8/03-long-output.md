# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-06 04:11:23
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-omni-30b-fp8 |   pp256 (c1) | 2727.22 ± 54.92 | 2727.22 ± 54.92 |               |                  |  161.79 ± 2.47 |   85.36 ± 2.47 |   161.79 ± 2.47 |
| nemotron-3-nano-omni-30b-fp8 |  tg4096 (c1) |    55.97 ± 0.02 |    55.97 ± 0.02 |  57.67 ± 0.94 |     57.67 ± 0.94 |                |                |                 |
| nemotron-3-nano-omni-30b-fp8 |   pp256 (c5) | 1513.46 ± 41.11 |  353.02 ± 39.09 |               |                  | 743.88 ± 58.34 | 667.44 ± 58.34 |  743.88 ± 58.34 |
| nemotron-3-nano-omni-30b-fp8 |  tg4096 (c5) |    88.11 ± 4.33 |    27.93 ± 5.65 | 125.33 ± 1.89 |    37.80 ± 11.81 |                |                |                 |
| nemotron-3-nano-omni-30b-fp8 |  pp256 (c10) | 2657.50 ± 50.14 |  305.34 ± 49.75 |               |                  | 862.64 ± 73.51 | 786.21 ± 73.51 |  862.64 ± 73.51 |
| nemotron-3-nano-omni-30b-fp8 | tg4096 (c10) |   120.57 ± 4.12 |    18.75 ± 3.67 | 176.67 ± 4.71 |    28.63 ± 12.21 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-06 03:58:07 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
