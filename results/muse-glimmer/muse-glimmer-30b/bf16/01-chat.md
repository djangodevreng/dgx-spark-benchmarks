# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-12 03:55:24
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|-------------:|-----------------:|------------------:|------------------:|-----------------:|
| muse-glimmer-30b-bf16 |  pp1024 (c1) | 1570.74 ± 211.50 | 1570.74 ± 211.50 |              |                  |   955.85 ± 106.14 |   615.94 ± 106.14 |  1595.88 ± 95.36 |
| muse-glimmer-30b-bf16 |  tg1024 (c1) |      4.28 ± 0.04 |      4.28 ± 0.04 |  5.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                  |
| muse-glimmer-30b-bf16 |  pp1024 (c5) |  1100.81 ± 23.52 |  681.53 ± 764.68 |              |                  | 2938.88 ± 1111.07 | 2598.96 ± 1111.07 | 4077.71 ± 272.46 |
| muse-glimmer-30b-bf16 |  tg1024 (c5) |     20.80 ± 0.05 |      4.17 ± 0.03 | 25.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                  |
| muse-glimmer-30b-bf16 | pp1024 (c10) |  1317.97 ± 64.50 |  417.32 ± 653.25 |              |                  | 4927.30 ± 1873.71 | 4587.39 ± 1873.71 | 6792.27 ± 311.65 |
| muse-glimmer-30b-bf16 | tg1024 (c10) |     40.61 ± 0.01 |      4.07 ± 0.03 | 50.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                  |

llama-benchy (0.4.0)
date: 2026-08-12 03:06:00 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
