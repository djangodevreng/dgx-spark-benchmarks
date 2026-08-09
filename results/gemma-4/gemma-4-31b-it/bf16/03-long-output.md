# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-06 16:31:18
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model       |         test |    t/s (total) |      t/s (req) |     peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------|-------------:|---------------:|---------------:|-------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-31b |   pp256 (c1) |  806.97 ± 8.48 |  806.97 ± 8.48 |              |                  |   660.66 ± 6.14 |   279.62 ± 6.14 |   660.66 ± 6.14 |
| gemma-4-31b |  tg4096 (c1) |    3.73 ± 0.00 |    3.73 ± 0.00 |  4.00 ± 0.00 |      4.00 ± 0.00 |                 |                 |                 |
| gemma-4-31b |   pp256 (c5) | 812.94 ± 37.11 | 222.12 ± 16.60 |              |                  | 1432.58 ± 75.05 | 1051.54 ± 75.05 | 1432.58 ± 75.05 |
| gemma-4-31b |  tg4096 (c5) |   10.78 ± 2.14 |    3.63 ± 0.02 | 20.00 ± 0.00 |      4.00 ± 0.00 |                 |                 |                 |
| gemma-4-31b |  pp256 (c10) |  960.19 ± 6.10 |  113.77 ± 5.34 |              |                  |  2446.95 ± 6.02 |  2065.91 ± 6.02 |  2446.95 ± 6.02 |
| gemma-4-31b | tg4096 (c10) |   20.22 ± 2.35 |    3.57 ± 0.02 | 40.00 ± 0.00 |      4.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-06 16:10:15 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
