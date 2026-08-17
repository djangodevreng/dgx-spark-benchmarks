# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-16 12:11:05
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-bf16 |  pp1024 (c1) | 2387.55 ± 566.54 |  2387.55 ± 566.54 |               |                  |  556.16 ± 124.32 |  424.71 ± 124.32 |  556.16 ± 124.32 |
| gemma-4-26b-a4b-bf16 |  tg1024 (c1) |     24.12 ± 0.04 |      24.12 ± 0.04 |  25.00 ± 0.00 |     25.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 |  pp1024 (c5) | 4084.82 ± 294.56 | 1572.71 ± 1161.46 |               |                  |  948.83 ± 318.76 |  817.38 ± 318.76 |  948.83 ± 318.76 |
| gemma-4-26b-a4b-bf16 |  tg1024 (c5) |     58.63 ± 1.00 |      13.89 ± 0.86 |  73.33 ± 2.36 |     18.80 ± 3.75 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 | pp1024 (c10) |  5077.55 ± 24.91 | 1101.91 ± 1166.62 |               |                  | 1472.77 ± 545.80 | 1341.32 ± 545.80 | 1472.77 ± 545.80 |
| gemma-4-26b-a4b-bf16 | tg1024 (c10) |     84.56 ± 1.70 |      10.89 ± 0.60 | 123.33 ± 4.71 |     15.77 ± 4.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-16 12:02:31 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
