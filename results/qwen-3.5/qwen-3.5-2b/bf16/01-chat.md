# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-07 14:33:34
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-2b-bf16 |  pp1024 (c1) | 24649.46 ± 2293.82 | 24649.46 ± 2293.82 |               |                  |    88.17 ± 3.29 |    37.97 ± 3.29 |    88.17 ± 3.29 |
| qwen3.5-2b-bf16 |  tg1024 (c1) |       43.04 ± 0.18 |       43.04 ± 0.18 |  44.00 ± 0.00 |     44.00 ± 0.00 |                 |                 |                 |
| qwen3.5-2b-bf16 |  pp1024 (c5) | 10075.15 ± 1124.14 |  3385.32 ± 1481.65 |               |                  | 368.46 ± 101.78 | 318.26 ± 101.78 | 368.46 ± 101.78 |
| qwen3.5-2b-bf16 |  tg1024 (c5) |      173.43 ± 8.80 |       52.91 ± 0.75 | 276.67 ± 2.36 |     55.80 ± 0.65 |                 |                 |                 |
| qwen3.5-2b-bf16 | pp1024 (c10) |  14109.39 ± 186.89 |  3420.23 ± 2700.11 |               |                  | 435.00 ± 173.24 | 384.79 ± 173.24 | 435.00 ± 173.24 |
| qwen3.5-2b-bf16 | tg1024 (c10) |     321.02 ± 32.52 |       50.02 ± 1.63 | 513.33 ± 4.71 |     53.53 ± 1.78 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 14:29:48 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
