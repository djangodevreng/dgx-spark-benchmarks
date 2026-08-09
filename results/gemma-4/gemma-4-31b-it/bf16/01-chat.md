# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-06 15:18:28
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model       |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------|-------------:|----------------:|----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| gemma-4-31b |  pp1024 (c1) | 588.94 ± 118.85 | 588.94 ± 118.85 |               |                  |  2114.97 ± 367.64 |  1725.71 ± 367.64 |  2114.97 ± 367.64 |
| gemma-4-31b |  tg1024 (c1) |     3.67 ± 0.01 |     3.67 ± 0.01 |   5.00 ± 0.00 |      5.00 ± 0.00 |                   |                   |                   |
| gemma-4-31b |  pp1024 (c5) |  749.02 ± 85.19 | 227.78 ± 147.05 |               |                  | 5312.47 ± 1470.11 | 4923.22 ± 1470.11 | 5312.47 ± 1470.11 |
| gemma-4-31b |  tg1024 (c5) |    10.88 ± 0.63 |     3.48 ± 0.10 | 29.67 ± 10.34 |      5.93 ± 2.08 |                   |                   |                   |
| gemma-4-31b | pp1024 (c10) | 1055.20 ± 16.97 |  191.14 ± 89.95 |               |                  | 6384.93 ± 2483.87 | 5995.67 ± 2483.87 | 6384.93 ± 2483.87 |
| gemma-4-31b | tg1024 (c10) |    18.31 ± 1.62 |     3.33 ± 0.25 |  40.00 ± 0.00 |      4.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-06 14:44:52 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
