# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-15 05:50:56
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |              test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |      est_ppt (ms) |      e2e_ttft (ms) |
|:-----------------|------------------:|----------------:|----------------:|--------------:|-----------------:|-------------------:|------------------:|-------------------:|
| nemotron-3-super |  pp2048 @ d4 (c1) | 1304.72 ± 13.13 | 1304.72 ± 13.13 |               |                  |    1553.01 ± 27.74 |   1348.68 ± 27.74 |    1553.01 ± 27.74 |
| nemotron-3-super |   tg512 @ d4 (c1) |    22.64 ± 1.27 |    22.64 ± 1.27 |  33.00 ± 2.16 |     33.00 ± 2.16 |                    |                   |                    |
| nemotron-3-super |  pp2048 @ d4 (c5) |  1201.44 ± 5.32 | 373.06 ± 151.61 |               |                  |  5918.83 ± 1769.72 | 5714.50 ± 1769.72 |  5918.83 ± 1769.72 |
| nemotron-3-super |   tg512 @ d4 (c5) |    48.48 ± 1.35 |    10.56 ± 0.61 |  77.33 ± 1.25 |     18.07 ± 1.98 |                    |                   |                    |
| nemotron-3-super | pp2048 @ d4 (c10) |  1196.77 ± 5.19 | 246.75 ± 153.05 |               |                  | 10060.79 ± 4253.63 | 9856.46 ± 4253.63 | 10060.79 ± 4253.63 |
| nemotron-3-super |  tg512 @ d4 (c10) |    63.66 ± 0.40 |     7.60 ± 0.55 | 105.33 ± 2.05 |     15.07 ± 2.64 |                    |                   |                    |

llama-benchy (0.4.0)
date: 2026-08-15 05:40:07 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
