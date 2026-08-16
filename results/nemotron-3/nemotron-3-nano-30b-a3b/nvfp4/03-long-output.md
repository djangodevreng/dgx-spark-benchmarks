# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-13 14:08:47
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                     |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-30b-nvfp4 |   pp256 (c1) | 3904.78 ± 21.08 |  3904.78 ± 21.08 |               |                  |  113.34 ± 1.63 |   59.07 ± 1.63 |   113.34 ± 1.63 |
| nemotron-3-nano-30b-nvfp4 |  tg4096 (c1) |    62.94 ± 0.02 |     62.94 ± 0.02 |  64.67 ± 0.94 |     64.67 ± 0.94 |                |                |                 |
| nemotron-3-nano-30b-nvfp4 |   pp256 (c5) | 3713.89 ± 41.57 | 1168.50 ± 509.67 |               |                  | 284.84 ± 65.56 | 230.57 ± 65.56 |  284.84 ± 65.56 |
| nemotron-3-nano-30b-nvfp4 |  tg4096 (c5) |   141.28 ± 1.54 |     34.52 ± 3.58 | 169.67 ± 3.30 |    46.87 ± 11.15 |                |                |                 |
| nemotron-3-nano-30b-nvfp4 |  pp256 (c10) | 4827.98 ± 38.19 |  718.44 ± 532.29 |               |                  | 445.28 ± 95.88 | 391.00 ± 95.88 |  445.28 ± 95.88 |
| nemotron-3-nano-30b-nvfp4 | tg4096 (c10) |  192.15 ± 10.03 |     24.85 ± 3.14 | 250.00 ± 0.00 |    37.37 ± 12.68 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-13 13:57:18 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
