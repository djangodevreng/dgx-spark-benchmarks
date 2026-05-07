# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-05 21:39:58
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:---------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-26b-a4b-bf16 |   pp256 (c1) | 1993.94 ± 262.05 | 1993.94 ± 262.05 |               |                  | 236.87 ± 11.60 | 119.88 ± 11.60 |  236.87 ± 11.60 |
| gemma-4-26b-a4b-bf16 |  tg4096 (c1) |     24.17 ± 0.02 |     24.17 ± 0.02 |  25.00 ± 0.00 |     25.00 ± 0.00 |                |                |                 |
| gemma-4-26b-a4b-bf16 |   pp256 (c5) | 3048.28 ± 496.15 | 1004.20 ± 411.97 |               |                  | 379.48 ± 74.70 | 262.49 ± 74.70 |  379.48 ± 74.70 |
| gemma-4-26b-a4b-bf16 |  tg4096 (c5) |    46.11 ± 11.57 |     14.32 ± 2.18 |  75.00 ± 0.00 |     18.00 ± 3.85 |                |                |                 |
| gemma-4-26b-a4b-bf16 |  pp256 (c10) |  4800.80 ± 50.75 |   636.03 ± 34.16 |               |                  |  480.62 ± 5.51 |  363.63 ± 5.51 |   480.62 ± 5.51 |
| gemma-4-26b-a4b-bf16 | tg4096 (c10) |     83.77 ± 4.04 |     11.75 ± 0.68 | 125.67 ± 4.19 |     15.32 ± 3.54 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-05 21:32:49 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
