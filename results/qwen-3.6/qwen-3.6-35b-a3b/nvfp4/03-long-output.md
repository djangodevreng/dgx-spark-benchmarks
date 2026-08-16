# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-14 07:37:49
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.6-35b-a3b-nvfp4 |   pp256 (c1) | 3619.15 ± 281.98 | 3619.15 ± 281.98 |               |                  |  113.94 ± 3.21 |   58.63 ± 3.21 |   113.94 ± 3.21 |
| qwen3.6-35b-a3b-nvfp4 |  tg4096 (c1) |     42.74 ± 0.02 |     42.74 ± 0.02 |  44.00 ± 0.00 |     44.00 ± 0.00 |                |                |                 |
| qwen3.6-35b-a3b-nvfp4 |   pp256 (c5) | 3506.87 ± 307.53 |  993.51 ± 324.46 |               |                  | 303.40 ± 53.76 | 248.09 ± 53.76 |  303.40 ± 53.76 |
| qwen3.6-35b-a3b-nvfp4 |  tg4096 (c5) |    103.57 ± 5.56 |     30.08 ± 2.63 | 151.67 ± 4.71 |     37.47 ± 4.92 |                |                |                 |
| qwen3.6-35b-a3b-nvfp4 |  pp256 (c10) |  4275.33 ± 36.66 |  619.15 ± 225.28 |               |                  | 466.30 ± 77.52 | 410.99 ± 77.52 |  466.30 ± 77.52 |
| qwen3.6-35b-a3b-nvfp4 | tg4096 (c10) |    176.06 ± 3.32 |     22.40 ± 1.54 | 250.00 ± 0.00 |     29.70 ± 4.83 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-14 07:15:01 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
