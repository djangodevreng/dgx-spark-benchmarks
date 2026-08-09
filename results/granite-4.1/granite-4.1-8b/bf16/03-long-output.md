# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-09 07:07:58
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model granite-4-1-8b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| granite-4-1-8b-bf16 |   pp256 (c1) | 2499.21 ± 412.47 | 2499.21 ± 412.47 |               |                  |  202.85 ± 9.18 |   87.28 ± 9.18 |   202.85 ± 9.18 |
| granite-4-1-8b-bf16 |  tg4096 (c1) |     12.62 ± 0.01 |     12.62 ± 0.01 |  13.00 ± 0.00 |     13.00 ± 0.00 |                |                |                 |
| granite-4-1-8b-bf16 |   pp256 (c5) |  2685.85 ± 90.40 |   736.81 ± 56.27 |               |                  | 430.79 ± 23.92 | 315.22 ± 23.92 |  430.79 ± 23.92 |
| granite-4-1-8b-bf16 |  tg4096 (c5) |    30.34 ± 10.28 |     13.11 ± 0.15 |  70.00 ± 0.00 |     14.27 ± 0.44 |                |                |                 |
| granite-4-1-8b-bf16 |  pp256 (c10) |  3263.85 ± 23.36 |   390.12 ± 20.92 |               |                  |  710.29 ± 4.13 |  594.72 ± 4.13 |   710.29 ± 4.13 |
| granite-4-1-8b-bf16 | tg4096 (c10) |     75.84 ± 7.24 |     13.03 ± 0.03 | 140.00 ± 0.00 |     14.00 ± 0.00 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-09 06:56:14 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
