# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-13 17:00:12
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model kat-coder-v2-5-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| kat-coder-v2-5-bf16 |   pp256 (c1) |  1655.73 ± 45.69 | 1655.73 ± 45.69 |               |                  |   259.95 ± 6.06 |   139.85 ± 6.06 |   259.95 ± 6.06 |
| kat-coder-v2-5-bf16 |  tg4096 (c1) |     30.41 ± 0.25 |    30.41 ± 0.25 |  31.00 ± 0.00 |     31.00 ± 0.00 |                 |                 |                 |
| kat-coder-v2-5-bf16 |   pp256 (c5) |  2603.74 ± 26.60 |  707.88 ± 37.62 |               |                  |   455.70 ± 6.44 |   335.61 ± 6.44 |   455.70 ± 6.44 |
| kat-coder-v2-5-bf16 |  tg4096 (c5) |    56.30 ± 12.19 |    16.75 ± 3.36 |  81.33 ± 1.89 |     22.67 ± 5.56 |                 |                 |                 |
| kat-coder-v2-5-bf16 |  pp256 (c10) | 3078.71 ± 409.81 | 402.86 ± 101.54 |               |                  | 739.22 ± 123.25 | 619.13 ± 123.25 | 739.22 ± 123.25 |
| kat-coder-v2-5-bf16 | tg4096 (c10) |     65.18 ± 9.93 |    10.59 ± 2.98 | 114.00 ± 4.32 |     17.17 ± 6.27 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-13 16:44:19 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
