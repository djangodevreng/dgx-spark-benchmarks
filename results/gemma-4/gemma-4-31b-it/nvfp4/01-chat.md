# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-16 18:38:17
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------------|-------------:|---------------:|----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| gemma-4-31b-nvfp4 |  pp1024 (c1) | 767.56 ± 54.22 |  767.56 ± 54.22 |              |                  |   1405.47 ± 87.37 |   1193.48 ± 87.37 |   1405.47 ± 87.37 |
| gemma-4-31b-nvfp4 |  tg1024 (c1) |    6.92 ± 0.06 |     6.92 ± 0.06 |  7.00 ± 0.00 |      7.00 ± 0.00 |                   |                   |                   |
| gemma-4-31b-nvfp4 |  pp1024 (c5) | 859.38 ± 10.41 | 261.66 ± 121.14 |              |                  | 4362.61 ± 1379.18 | 4150.62 ± 1379.18 | 4362.61 ± 1379.18 |
| gemma-4-31b-nvfp4 |  tg1024 (c5) |   23.02 ± 3.17 |     6.52 ± 0.17 | 36.33 ± 1.89 |      7.27 ± 0.44 |                   |                   |                   |
| gemma-4-31b-nvfp4 | pp1024 (c10) | 885.95 ± 33.74 |  135.77 ± 94.08 |              |                  | 8404.22 ± 2254.92 | 8192.24 ± 2254.92 | 8404.22 ± 2254.92 |
| gemma-4-31b-nvfp4 | tg1024 (c10) |   36.95 ± 4.62 |     6.03 ± 0.26 | 70.00 ± 0.00 |      7.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-16 18:20:53 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
