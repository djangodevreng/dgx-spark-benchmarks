# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-08 16:32:10
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model lfm2-5-2-6b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |        t/s (total) |          t/s (req) |       peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------|-------------:|-------------------:|-------------------:|---------------:|-----------------:|---------------:|---------------:|----------------:|
| lfm2-5-2-6b-bf16 |   pp256 (c1) | 13012.19 ± 5847.01 | 13012.19 ± 5847.01 |                |                  |   65.58 ± 7.11 |   20.23 ± 7.11 |    65.58 ± 7.11 |
| lfm2-5-2-6b-bf16 |  tg4096 (c1) |       32.25 ± 0.11 |       32.25 ± 0.11 |   33.33 ± 0.47 |     33.33 ± 0.47 |                |                |                 |
| lfm2-5-2-6b-bf16 |   pp256 (c5) |   8848.40 ± 444.87 |  3218.08 ± 1899.93 |                |                  | 129.06 ± 17.10 |  83.71 ± 17.10 |  129.06 ± 17.10 |
| lfm2-5-2-6b-bf16 |  tg4096 (c5) |     131.42 ± 20.02 |       38.88 ± 0.72 |  205.00 ± 0.00 |     41.40 ± 0.80 |                |                |                 |
| lfm2-5-2-6b-bf16 |  pp256 (c10) |   10131.93 ± 74.05 |  2212.89 ± 2430.51 |                |                  | 214.23 ± 55.46 | 168.88 ± 55.46 |  214.23 ± 55.46 |
| lfm2-5-2-6b-bf16 | tg4096 (c10) |      242.59 ± 2.30 |       38.63 ± 0.19 | 410.00 ± 14.14 |     41.37 ± 1.22 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-08 16:12:45 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
