# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-08 09:47:20
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                  |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-4b-fp8 |   pp256 (c1) | 11346.79 ± 2135.70 | 11346.79 ± 2135.70 |               |                  |    64.94 ± 5.36 |    21.48 ± 5.36 |    64.94 ± 5.36 |
| nemotron-3-nano-4b-fp8 |  tg4096 (c1) |       42.08 ± 0.23 |       42.08 ± 0.23 |  43.67 ± 0.94 |     43.67 ± 0.94 |                 |                 |                 |
| nemotron-3-nano-4b-fp8 |   pp256 (c5) |   2839.03 ± 266.47 |     667.62 ± 87.24 |               |                  |  400.14 ± 61.55 |  356.68 ± 61.55 |  400.14 ± 61.55 |
| nemotron-3-nano-4b-fp8 |  tg4096 (c5) |     118.33 ± 13.37 |       41.82 ± 0.61 | 210.00 ± 0.00 |     44.13 ± 1.67 |                 |                 |                 |
| nemotron-3-nano-4b-fp8 |  pp256 (c10) |  6882.06 ± 1584.03 |    993.04 ± 639.47 |               |                  | 331.35 ± 108.31 | 287.89 ± 108.31 | 331.35 ± 108.31 |
| nemotron-3-nano-4b-fp8 | tg4096 (c10) |     197.08 ± 21.22 |       37.13 ± 1.90 | 360.00 ± 0.00 |     40.93 ± 3.47 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-08 09:37:18 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
