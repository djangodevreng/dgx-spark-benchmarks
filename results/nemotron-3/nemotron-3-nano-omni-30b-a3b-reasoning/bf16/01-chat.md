# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-06 00:09:44
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                         |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-bf16 |  pp1024 (c1) | 2185.10 ± 286.27 | 2185.10 ± 286.27 |               |                  |   560.70 ± 38.72 |   419.33 ± 38.72 |   560.70 ± 38.72 |
| nemotron-3-nano-omni-30b-bf16 |  tg1024 (c1) |     29.39 ± 0.06 |     29.39 ± 0.06 |  31.33 ± 0.94 |     31.33 ± 0.94 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 |  pp1024 (c5) | 3868.52 ± 370.58 | 1343.63 ± 854.19 |               |                  | 1006.03 ± 302.55 |  864.65 ± 302.55 | 1006.03 ± 302.55 |
| nemotron-3-nano-omni-30b-bf16 |  tg1024 (c5) |     58.64 ± 2.23 |     12.86 ± 1.46 |  71.33 ± 0.94 |     16.07 ± 2.08 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 | pp1024 (c10) |  5098.81 ± 56.98 |  941.32 ± 779.40 |               |                  | 1477.31 ± 489.52 | 1335.94 ± 489.52 | 1477.31 ± 489.52 |
| nemotron-3-nano-omni-30b-bf16 | tg1024 (c10) |     73.44 ± 2.50 |      8.75 ± 0.87 | 106.67 ± 4.71 |     11.40 ± 0.61 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-05 23:55:08 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
