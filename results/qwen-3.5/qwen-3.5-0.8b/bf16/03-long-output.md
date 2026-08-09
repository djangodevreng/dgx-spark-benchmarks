# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-07 09:28:04
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |        t/s (total) |          t/s (req) |       peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|-------------------:|-------------------:|---------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.5-0.8b-bf16 |   pp256 (c1) | 21425.74 ± 9601.01 | 21425.74 ± 9601.01 |                |                  |  36.39 ± 10.14 |  15.31 ± 10.14 |   36.39 ± 10.14 |
| qwen3.5-0.8b-bf16 |  tg4096 (c1) |      114.67 ± 0.28 |      114.67 ± 0.28 |  116.66 ± 0.93 |    116.66 ± 0.93 |                |                |                 |
| qwen3.5-0.8b-bf16 |   pp256 (c5) |  16535.26 ± 111.14 |  5472.52 ± 1334.72 |                |                  |   64.56 ± 7.38 |   43.48 ± 7.38 |    64.56 ± 7.38 |
| qwen3.5-0.8b-bf16 |  tg4096 (c5) |     278.35 ± 26.40 |      115.16 ± 1.44 | 581.33 ± 15.76 |    119.29 ± 3.00 |                |                |                 |
| qwen3.5-0.8b-bf16 |  pp256 (c10) | 17603.93 ± 1483.51 |  2694.24 ± 1232.25 |                |                  | 118.61 ± 22.48 |  97.54 ± 22.48 |  118.61 ± 22.48 |
| qwen3.5-0.8b-bf16 | tg4096 (c10) |    484.16 ± 133.75 |      105.89 ± 3.61 | 1025.00 ± 7.07 |    111.61 ± 7.14 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-07 09:26:16 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
