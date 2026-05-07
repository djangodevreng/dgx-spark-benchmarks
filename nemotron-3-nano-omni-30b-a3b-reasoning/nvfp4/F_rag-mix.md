# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-03 10:06:03
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                          |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-------------------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-nano-omni-30b-nvfp4 |  pp8192 (c5) | 9921.44 ± 1292.72 | 3789.99 ± 2322.63 |               |                  | 2588.57 ± 1054.22 | 2515.19 ± 1054.22 | 2588.57 ± 1054.22 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg512 (c5) |     122.05 ± 2.56 |      27.77 ± 2.44 | 151.67 ± 2.36 |     32.20 ± 3.51 |                   |                   |                   |
| nemotron-3-nano-omni-30b-nvfp4 | pp8192 (c10) |  11156.13 ± 31.34 | 2795.83 ± 2263.48 |               |                  | 4014.66 ± 1933.76 | 3941.29 ± 1933.76 | 4014.66 ± 1933.76 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg512 (c10) |     167.06 ± 3.87 |      19.65 ± 1.48 | 233.67 ± 3.86 |     25.10 ± 2.56 |                   |                   |                   |
| nemotron-3-nano-omni-30b-nvfp4 | pp8192 (c20) |  11251.61 ± 54.36 | 1749.47 ± 1878.43 |               |                  | 7311.72 ± 3751.74 | 7238.34 ± 3751.74 | 7311.72 ± 3751.74 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg512 (c20) |     229.11 ± 1.66 |      14.09 ± 1.52 | 360.00 ± 0.00 |     18.87 ± 1.32 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-03 10:01:16 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
