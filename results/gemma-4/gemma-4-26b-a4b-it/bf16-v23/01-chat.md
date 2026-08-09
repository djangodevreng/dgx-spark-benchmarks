# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-06 08:21:03
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b |  pp1024 (c1) | 2014.62 ± 372.58 |  2014.62 ± 372.58 |               |                  |   590.01 ± 95.51 |   462.67 ± 95.51 |   590.01 ± 95.51 |
| gemma-4-26b-a4b |  tg1024 (c1) |     23.88 ± 0.03 |      23.88 ± 0.03 |  24.33 ± 0.47 |     24.33 ± 0.47 |                  |                  |                  |
| gemma-4-26b-a4b |  pp1024 (c5) |  4262.37 ± 58.72 | 1505.47 ± 1088.19 |               |                  |  943.20 ± 280.79 |  815.86 ± 280.79 |  943.20 ± 280.79 |
| gemma-4-26b-a4b |  tg1024 (c5) |     52.22 ± 3.90 |      14.13 ± 1.13 |  70.33 ± 0.47 |     18.53 ± 3.74 |                  |                  |                  |
| gemma-4-26b-a4b | pp1024 (c10) |  5079.67 ± 16.78 | 1022.11 ± 1077.38 |               |                  | 1555.23 ± 532.87 | 1427.89 ± 532.87 | 1555.23 ± 532.87 |
| gemma-4-26b-a4b | tg1024 (c10) |     90.81 ± 1.12 |      10.55 ± 0.35 | 126.67 ± 4.71 |     15.23 ± 3.35 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 08:12:09 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
