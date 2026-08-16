# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-13 13:50:00
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                     |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-30b-nvfp4 |  pp1024 (c1) | 2766.01 ± 589.20 |  2766.01 ± 589.20 |               |                  |   427.91 ± 96.81 |   359.96 ± 96.81 |   427.91 ± 96.81 |
| nemotron-3-nano-30b-nvfp4 |  tg1024 (c1) |     63.14 ± 0.22 |      63.14 ± 0.22 |  68.00 ± 2.16 |     68.00 ± 2.16 |                  |                  |                  |
| nemotron-3-nano-30b-nvfp4 |  pp1024 (c5) | 5175.15 ± 103.94 | 1963.27 ± 1364.56 |               |                  |  694.18 ± 254.14 |  626.23 ± 254.14 |  694.18 ± 254.14 |
| nemotron-3-nano-30b-nvfp4 |  tg1024 (c5) |    150.46 ± 0.98 |      30.49 ± 0.31 | 166.67 ± 2.36 |     33.33 ± 0.47 |                  |                  |                  |
| nemotron-3-nano-30b-nvfp4 | pp1024 (c10) |  6002.43 ± 18.50 | 1240.64 ± 1177.71 |               |                  | 1194.57 ± 473.14 | 1126.62 ± 473.14 | 1194.57 ± 473.14 |
| nemotron-3-nano-30b-nvfp4 | tg1024 (c10) |    206.05 ± 6.25 |      22.05 ± 0.52 | 250.00 ± 0.00 |     25.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-13 13:43:24 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
