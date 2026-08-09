# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-08 00:18:29
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-30b-fp8 |  pp1024 (c1) | 1440.91 ± 252.94 | 1440.91 ± 252.94 |               |                  |   739.97 ± 85.85 |   650.41 ± 85.85 |   739.97 ± 85.85 |
| nemotron-3-nano-30b-fp8 |  tg1024 (c1) |     46.43 ± 1.31 |     46.43 ± 1.31 |  49.67 ± 1.25 |     49.67 ± 1.25 |                  |                  |                  |
| nemotron-3-nano-30b-fp8 |  pp1024 (c5) |  3261.23 ± 84.00 |  755.05 ± 126.63 |               |                  | 1340.16 ± 166.50 | 1250.60 ± 166.50 | 1340.16 ± 166.50 |
| nemotron-3-nano-30b-fp8 |  tg1024 (c5) |     96.16 ± 0.59 |     19.35 ± 0.13 | 111.67 ± 4.71 |     22.33 ± 0.94 |                  |                  |                  |
| nemotron-3-nano-30b-fp8 | pp1024 (c10) | 4645.98 ± 730.33 |  550.56 ± 240.56 |               |                  | 1959.28 ± 426.99 | 1869.72 ± 426.99 | 1959.28 ± 426.99 |
| nemotron-3-nano-30b-fp8 | tg1024 (c10) |    129.66 ± 4.56 |     13.53 ± 0.15 | 176.00 ± 4.97 |     17.60 ± 0.55 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-08 00:08:04 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
