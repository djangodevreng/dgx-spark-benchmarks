# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-08 16:12:44
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model lfm2-5-2-6b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model            |         test |        t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|-------------:|-------------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| lfm2-5-2-6b-bf16 |  pp8192 (c5) | 11859.95 ± 1579.65 | 5936.27 ± 4072.20 |               |                  |  1900.65 ± 993.64 |  1855.45 ± 993.64 |  1900.65 ± 993.64 |
| lfm2-5-2-6b-bf16 |   tg512 (c5) |      159.17 ± 4.32 |      34.90 ± 2.28 | 196.33 ± 1.89 |     39.27 ± 0.44 |                   |                   |                   |
| lfm2-5-2-6b-bf16 | pp8192 (c10) |   12986.66 ± 39.52 | 3791.00 ± 3563.25 |               |                  | 3345.14 ± 1728.45 | 3299.94 ± 1728.45 | 3345.14 ± 1728.45 |
| lfm2-5-2-6b-bf16 |  tg512 (c10) |      254.87 ± 3.89 |      30.01 ± 2.96 | 360.00 ± 0.00 |     36.00 ± 0.00 |                   |                   |                   |
| lfm2-5-2-6b-bf16 | pp8192 (c20) |  12705.09 ± 483.15 | 2235.61 ± 2882.32 |               |                  | 6510.11 ± 3429.94 | 6464.91 ± 3429.94 | 6510.11 ± 3429.94 |
| lfm2-5-2-6b-bf16 |  tg512 (c20) |      346.81 ± 4.66 |      22.36 ± 3.15 | 580.00 ± 0.00 |     29.58 ± 0.88 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-08 16:08:10 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
