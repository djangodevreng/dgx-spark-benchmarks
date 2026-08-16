# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-14 20:45:19
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|-------------:|----------------:|----------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-27b-fp8 |   pp256 (c1) | 622.38 ± 107.54 | 622.38 ± 107.54 |              |                  |   531.67 ± 55.67 |   381.91 ± 55.67 |   531.67 ± 55.67 |
| qwen3.6-27b-fp8 |  tg4096 (c1) |     7.89 ± 0.01 |     7.89 ± 0.01 |  8.00 ± 0.00 |      8.00 ± 0.00 |                  |                  |                  |
| qwen3.6-27b-fp8 |   pp256 (c5) |   589.48 ± 2.38 |  139.97 ± 32.92 |              |                  | 1964.22 ± 282.01 | 1814.46 ± 282.01 | 1964.22 ± 282.01 |
| qwen3.6-27b-fp8 |  tg4096 (c5) |    23.86 ± 4.94 |     7.77 ± 0.04 | 40.00 ± 0.00 |      8.00 ± 0.00 |                  |                  |                  |
| qwen3.6-27b-fp8 |  pp256 (c10) |   591.94 ± 7.00 |   67.97 ± 16.86 |              |                  | 3715.40 ± 516.14 | 3565.64 ± 516.14 | 3715.40 ± 516.14 |
| qwen3.6-27b-fp8 | tg4096 (c10) |    53.06 ± 2.67 |     7.36 ± 0.09 | 80.00 ± 0.00 |      8.03 ± 0.18 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-14 19:09:31 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
