# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-05 04:05:43
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-super |  pp8192 (c5) | 1612.55 ± 8.86 | 619.93 ± 324.02 |               |                  |  14975.25 ± 5947.44 |  14770.57 ± 5947.44 |  14975.25 ± 5947.44 |
| nemotron-3-super |   tg512 (c5) |   40.38 ± 0.19 |    10.01 ± 1.03 |  69.67 ± 2.05 |     19.40 ± 4.13 |                     |                     |                     |
| nemotron-3-super | pp8192 (c10) | 1600.64 ± 1.45 | 406.24 ± 304.50 |               |                  | 26514.56 ± 12832.83 | 26309.87 ± 12832.83 | 26514.56 ± 12832.83 |
| nemotron-3-super |  tg512 (c10) |   49.66 ± 1.24 |     6.94 ± 1.14 | 103.67 ± 1.25 |     15.33 ± 2.90 |                     |                     |                     |
| nemotron-3-super | pp8192 (c20) | 1562.81 ± 1.13 | 256.53 ± 269.66 |               |                  | 50402.63 ± 27228.10 | 50197.95 ± 27228.10 | 50402.63 ± 27228.10 |
| nemotron-3-super |  tg512 (c20) |   59.74 ± 1.12 |     4.71 ± 1.01 | 148.33 ± 3.77 |     12.18 ± 2.91 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-05 03:48:27 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
