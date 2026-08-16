# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-13 16:30:42
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model kat-coder-v2-5-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| kat-coder-v2-5-bf16 |  pp1024 (c1) | 1566.38 ± 441.30 | 1566.38 ± 441.30 |               |                  |  785.25 ± 213.44 |  656.73 ± 213.44 |  785.25 ± 213.44 |
| kat-coder-v2-5-bf16 |  tg1024 (c1) |     30.59 ± 0.27 |     30.59 ± 0.27 |  34.00 ± 0.00 |     34.00 ± 0.00 |                  |                  |                  |
| kat-coder-v2-5-bf16 |  pp1024 (c5) | 3272.29 ± 251.08 |  934.96 ± 337.18 |               |                  | 1214.74 ± 254.70 | 1086.22 ± 254.70 | 1214.74 ± 254.70 |
| kat-coder-v2-5-bf16 |  tg1024 (c5) |     60.16 ± 1.64 |     15.48 ± 2.42 |  81.67 ± 1.70 |     22.67 ± 5.19 |                  |                  |                  |
| kat-coder-v2-5-bf16 | pp1024 (c10) | 4020.47 ± 286.49 |  545.21 ± 221.39 |               |                  | 2009.87 ± 418.56 | 1881.36 ± 418.56 | 2009.87 ± 418.56 |
| kat-coder-v2-5-bf16 | tg1024 (c10) |     75.79 ± 3.47 |     10.44 ± 1.72 | 114.67 ± 3.77 |     16.00 ± 5.23 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-13 16:20:00 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
