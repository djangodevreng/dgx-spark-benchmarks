# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-16 15:43:40
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c1) | 3123.20 ± 804.30 |  3123.20 ± 804.30 |               |                  |  399.54 ± 113.62 |  334.06 ± 113.62 |  399.54 ± 113.62 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c1) |     29.45 ± 0.45 |      29.45 ± 0.45 |  31.00 ± 0.00 |     31.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c5) | 5532.44 ± 212.43 | 2071.93 ± 1593.62 |               |                  |  683.43 ± 225.33 |  617.95 ± 225.33 |  683.43 ± 225.33 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c5) |     99.32 ± 7.00 |      24.85 ± 0.69 | 130.00 ± 0.00 |     28.87 ± 2.92 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp1024 (c10) | 5717.48 ± 961.17 | 1235.77 ± 1328.37 |               |                  | 1347.47 ± 621.47 | 1281.99 ± 621.47 | 1347.47 ± 621.47 |
| gemma-4-26b-a4b-nvfp4 | tg1024 (c10) |    135.07 ± 7.41 |      21.18 ± 1.39 | 226.67 ± 4.71 |     25.53 ± 3.34 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-16 15:38:10 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
