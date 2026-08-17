# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-16 12:32:12
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |     ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:---------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|--------------:|---------------:|----------------:|
| gemma-4-26b-a4b-bf16 |   pp256 (c1) | 2173.20 ± 148.24 | 2173.20 ± 148.24 |               |                  | 233.63 ± 7.20 |  111.22 ± 7.20 |   233.63 ± 7.20 |
| gemma-4-26b-a4b-bf16 |  tg4096 (c1) |     24.11 ± 0.02 |     24.11 ± 0.02 |  25.00 ± 0.00 |     25.00 ± 0.00 |               |                |                 |
| gemma-4-26b-a4b-bf16 |   pp256 (c5) |  3194.88 ± 19.23 |   965.79 ± 50.12 |               |                  | 363.19 ± 5.28 |  240.78 ± 5.28 |   363.19 ± 5.28 |
| gemma-4-26b-a4b-bf16 |  tg4096 (c5) |     53.17 ± 3.89 |     14.52 ± 1.35 |  75.00 ± 0.00 |     18.93 ± 3.51 |               |                |                 |
| gemma-4-26b-a4b-bf16 |  pp256 (c10) |  4485.15 ± 49.76 |   585.86 ± 25.65 |               |                  | 523.68 ± 3.02 |  401.27 ± 3.02 |   523.68 ± 3.02 |
| gemma-4-26b-a4b-bf16 | tg4096 (c10) |     80.53 ± 0.96 |     11.50 ± 0.78 | 130.00 ± 0.00 |     15.70 ± 3.48 |               |                |                 |

llama-benchy (0.4.0)
date: 2026-08-16 12:25:37 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
