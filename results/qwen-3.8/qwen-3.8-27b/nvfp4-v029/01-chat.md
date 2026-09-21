# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-09-18 14:02:34
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-27b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |    t/s (total) |      t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------------|-------------:|---------------:|---------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.8-27b-nvfp4 |  pp1024 (c1) | 728.97 ± 65.12 | 728.97 ± 65.12 |               |                  |  1483.93 ± 132.79 |  1322.38 ± 132.79 |  1483.93 ± 132.79 |
| qwen3.8-27b-nvfp4 |  tg1024 (c1) |   12.16 ± 0.03 |   12.16 ± 0.03 |  13.67 ± 0.47 |     13.67 ± 0.47 |                   |                   |                   |
| qwen3.8-27b-nvfp4 |  pp1024 (c5) |  789.48 ± 4.53 | 221.24 ± 89.51 |               |                  | 4930.61 ± 1264.47 | 4769.06 ± 1264.47 | 4930.61 ± 1264.47 |
| qwen3.8-27b-nvfp4 |  tg1024 (c5) |   54.24 ± 0.02 |   11.14 ± 0.14 |  61.67 ± 2.36 |     12.33 ± 0.47 |                   |                   |                   |
| qwen3.8-27b-nvfp4 | pp1024 (c10) |  793.26 ± 8.72 | 145.41 ± 96.17 |               |                  | 8320.10 ± 3071.46 | 8158.55 ± 3071.46 | 8320.10 ± 3071.46 |
| qwen3.8-27b-nvfp4 | tg1024 (c10) |   92.52 ± 2.13 |   10.07 ± 0.29 | 113.33 ± 4.71 |     11.33 ± 0.47 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-09-18 13:42:56 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
