# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-06 08:42:07
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-26b-a4b |   pp256 (c1) |  1925.10 ± 72.59 | 1925.10 ± 72.59 |               |                  |  239.34 ± 1.99 |  120.93 ± 1.99 |   239.34 ± 1.99 |
| gemma-4-26b-a4b |  tg4096 (c1) |     24.02 ± 0.03 |    24.02 ± 0.03 |  25.00 ± 0.00 |     25.00 ± 0.00 |                |                |                 |
| gemma-4-26b-a4b |   pp256 (c5) |  3179.70 ± 61.82 |  941.34 ± 36.26 |               |                  |  366.34 ± 8.05 |  247.93 ± 8.05 |   366.34 ± 8.05 |
| gemma-4-26b-a4b |  tg4096 (c5) |     49.71 ± 3.79 |    14.48 ± 1.49 |  73.33 ± 2.36 |     18.40 ± 3.84 |                |                |                 |
| gemma-4-26b-a4b |  pp256 (c10) | 4175.46 ± 481.04 |  605.67 ± 81.61 |               |                  | 511.15 ± 50.11 | 392.75 ± 50.11 |  511.15 ± 50.11 |
| gemma-4-26b-a4b | tg4096 (c10) |     81.43 ± 0.94 |    11.36 ± 0.86 | 123.33 ± 4.71 |     15.47 ± 3.92 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-06 08:35:36 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
