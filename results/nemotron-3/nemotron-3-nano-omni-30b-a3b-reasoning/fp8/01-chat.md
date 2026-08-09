# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-06 03:49:31
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-fp8 |  pp1024 (c1) | 1316.14 ± 71.85 | 1316.14 ± 71.85 |               |                  |   841.84 ± 52.93 |   753.96 ± 52.93 |   841.84 ± 52.93 |
| nemotron-3-nano-omni-30b-fp8 |  tg1024 (c1) |    56.21 ± 0.19 |    56.21 ± 0.19 |  59.33 ± 0.47 |     59.33 ± 0.47 |                  |                  |                  |
| nemotron-3-nano-omni-30b-fp8 |  pp1024 (c5) | 3471.76 ± 42.44 | 802.61 ± 120.68 |               |                  | 1279.83 ± 149.47 | 1191.95 ± 149.47 | 1279.83 ± 149.47 |
| nemotron-3-nano-omni-30b-fp8 |  tg1024 (c5) |   103.26 ± 3.30 |    22.13 ± 1.75 | 121.67 ± 2.36 |     25.73 ± 3.15 |                  |                  |                  |
| nemotron-3-nano-omni-30b-fp8 | pp1024 (c10) | 5866.47 ± 93.08 | 742.03 ± 266.91 |               |                  | 1415.78 ± 243.03 | 1327.91 ± 243.03 | 1415.78 ± 243.03 |
| nemotron-3-nano-omni-30b-fp8 | tg1024 (c10) |   145.09 ± 6.52 |    16.85 ± 1.34 | 183.33 ± 4.71 |     21.03 ± 1.43 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 03:41:10 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
