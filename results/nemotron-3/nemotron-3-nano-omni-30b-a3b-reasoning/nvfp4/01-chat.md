# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-07 12:30:16
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                          |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-nvfp4 |  pp1024 (c1) | 2124.09 ± 23.48 | 2124.09 ± 23.48 |               |                  |    510.07 ± 2.18 |    443.15 ± 2.18 |    510.07 ± 2.18 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg1024 (c1) |    64.79 ± 0.06 |    64.79 ± 0.06 |  66.00 ± 0.00 |     66.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-omni-30b-nvfp4 |  pp1024 (c5) | 3858.98 ± 87.84 | 915.42 ± 183.65 |               |                  | 1106.45 ± 172.75 | 1039.52 ± 172.75 | 1106.45 ± 172.75 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg1024 (c5) |  137.26 ± 10.21 |    34.30 ± 4.73 | 169.00 ± 2.94 |     40.40 ± 9.25 |                  |                  |                  |
| nemotron-3-nano-omni-30b-nvfp4 | pp1024 (c10) | 5744.17 ± 43.07 | 747.73 ± 353.28 |               |                  | 1475.20 ± 298.83 | 1408.28 ± 298.83 | 1475.20 ± 298.83 |
| nemotron-3-nano-omni-30b-nvfp4 | tg1024 (c10) |   218.91 ± 1.61 |    23.94 ± 1.77 | 263.00 ± 4.97 |     27.63 ± 2.09 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-07 12:24:24 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
