# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-08 16:08:09
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model lfm2-5-2-6b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |        t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------|-------------:|-------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| lfm2-5-2-6b-bf16 |  pp1024 (c1) |  17617.01 ± 296.11 | 17617.01 ± 296.11 |               |                  |    97.59 ± 2.23 |    51.25 ± 2.23 |    97.59 ± 2.23 |
| lfm2-5-2-6b-bf16 |  tg1024 (c1) |       32.26 ± 0.53 |      32.26 ± 0.53 |  33.33 ± 0.47 |     33.33 ± 0.47 |                 |                 |                 |
| lfm2-5-2-6b-bf16 |  pp1024 (c5) |  11850.95 ± 110.02 | 5440.91 ± 5491.93 |               |                  | 334.61 ± 116.23 | 288.27 ± 116.23 | 334.61 ± 116.23 |
| lfm2-5-2-6b-bf16 |  tg1024 (c5) |      197.17 ± 0.06 |      39.80 ± 0.16 | 205.00 ± 0.00 |     41.00 ± 0.00 |                 |                 |                 |
| lfm2-5-2-6b-bf16 | pp1024 (c10) | 10236.95 ± 2970.88 | 2815.44 ± 4048.19 |               |                  | 750.45 ± 397.71 | 704.11 ± 397.71 | 750.45 ± 397.71 |
| lfm2-5-2-6b-bf16 | tg1024 (c10) |      369.81 ± 8.71 |      37.87 ± 0.70 | 406.67 ± 9.43 |     40.67 ± 0.94 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-08 16:02:24 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
