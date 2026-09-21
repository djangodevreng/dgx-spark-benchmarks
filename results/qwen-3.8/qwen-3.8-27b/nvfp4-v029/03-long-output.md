# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-09-18 15:45:15
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.8-27b-nvfp4 |   pp256 (c1) | 907.81 ± 118.19 | 907.81 ± 118.19 |               |                  |   391.53 ± 34.39 |   273.62 ± 34.39 |   391.53 ± 34.39 |
| qwen3.8-27b-nvfp4 |  tg4096 (c1) |    12.12 ± 0.03 |    12.12 ± 0.03 |  13.00 ± 0.00 |     13.00 ± 0.00 |                  |                  |                  |
| qwen3.8-27b-nvfp4 |   pp256 (c5) |  713.40 ± 22.26 |  177.91 ± 50.04 |               |                  | 1434.02 ± 246.34 | 1316.11 ± 246.34 | 1434.02 ± 246.34 |
| qwen3.8-27b-nvfp4 |  tg4096 (c5) |    48.41 ± 3.39 |    11.24 ± 0.04 |  60.00 ± 0.00 |     12.27 ± 0.44 |                  |                  |                  |
| qwen3.8-27b-nvfp4 |  pp256 (c10) |  711.97 ± 36.74 |   83.59 ± 21.57 |               |                  | 2935.88 ± 445.53 | 2817.97 ± 445.53 | 2935.88 ± 445.53 |
| qwen3.8-27b-nvfp4 | tg4096 (c10) |    90.80 ± 7.55 |    10.42 ± 0.17 | 113.33 ± 4.71 |     11.40 ± 0.49 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-09-18 14:36:01 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
