# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-09 03:42:30
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                    |         test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-------------------------|-------------:|-----------------:|----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-30b-bf16 |   pp256 (c1) |  1371.06 ± 53.26 | 1371.06 ± 53.26 |               |                  |   297.37 ± 6.46 |   163.53 ± 6.46 |   297.37 ± 6.46 |
| nemotron-3-nano-30b-bf16 |  tg4096 (c1) |     29.15 ± 0.03 |    29.15 ± 0.03 |  30.33 ± 0.47 |     30.33 ± 0.47 |                 |                 |                 |
| nemotron-3-nano-30b-bf16 |   pp256 (c5) |  2810.97 ± 55.59 |  833.13 ± 49.22 |               |                  |   413.67 ± 6.27 |   279.83 ± 6.27 |   413.67 ± 6.27 |
| nemotron-3-nano-30b-bf16 |  tg4096 (c5) |     51.93 ± 1.41 |    13.18 ± 1.84 |  68.67 ± 0.94 |     20.33 ± 6.02 |                 |                 |                 |
| nemotron-3-nano-30b-bf16 |  pp256 (c10) | 3852.36 ± 550.11 | 528.33 ± 166.65 |               |                  | 611.72 ± 121.33 | 477.89 ± 121.33 | 611.72 ± 121.33 |
| nemotron-3-nano-30b-bf16 | tg4096 (c10) |     66.35 ± 2.44 |     8.43 ± 1.13 | 100.00 ± 0.00 |     14.73 ± 6.24 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-09 03:07:07 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
