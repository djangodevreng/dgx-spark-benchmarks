# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-16 19:30:31
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |    t/s (total) |      t/s (req) |     peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|---------------:|---------------:|-------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-31b-nvfp4 |   pp256 (c1) | 847.48 ± 32.72 | 847.48 ± 32.72 |              |                  |   490.24 ± 8.21 |   288.21 ± 8.21 |   490.24 ± 8.21 |
| gemma-4-31b-nvfp4 |  tg4096 (c1) |    7.01 ± 0.00 |    7.01 ± 0.00 |  8.00 ± 0.00 |      8.00 ± 0.00 |                 |                 |                 |
| gemma-4-31b-nvfp4 |   pp256 (c5) | 820.11 ± 16.08 |  193.27 ± 8.58 |              |                  | 1393.41 ± 57.87 | 1191.39 ± 57.87 | 1393.41 ± 57.87 |
| gemma-4-31b-nvfp4 |  tg4096 (c5) |   23.26 ± 6.17 |    6.91 ± 0.02 | 41.33 ± 6.34 |      8.40 ± 1.20 |                 |                 |                 |
| gemma-4-31b-nvfp4 |  pp256 (c10) |  874.04 ± 2.31 |   94.58 ± 3.80 |              |                  | 2706.65 ± 25.55 | 2504.62 ± 25.55 | 2706.65 ± 25.55 |
| gemma-4-31b-nvfp4 | tg4096 (c10) |   36.22 ± 7.89 |    6.76 ± 0.06 | 70.00 ± 0.00 |      7.13 ± 0.34 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-16 19:19:05 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
