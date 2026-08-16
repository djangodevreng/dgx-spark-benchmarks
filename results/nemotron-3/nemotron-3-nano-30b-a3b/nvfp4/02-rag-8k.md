# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-13 13:57:17
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                     |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:--------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-3-nano-30b-nvfp4 |  pp8192 (c5) | 6583.59 ± 15.43 | 2960.32 ± 1950.84 |               |                  |  3507.88 ± 1608.99 |  3453.42 ± 1608.99 |  3507.88 ± 1608.99 |
| nemotron-3-nano-30b-nvfp4 |   tg512 (c5) |   121.17 ± 0.70 |      28.45 ± 4.62 | 162.67 ± 3.77 |     34.73 ± 4.39 |                    |                    |                    |
| nemotron-3-nano-30b-nvfp4 | pp8192 (c10) |  6603.33 ± 8.26 | 1866.92 ± 1738.87 |               |                  |  6580.08 ± 3381.79 |  6525.61 ± 3381.79 |  6580.08 ± 3381.79 |
| nemotron-3-nano-30b-nvfp4 |  tg512 (c10) |   150.78 ± 2.29 |      19.18 ± 2.88 | 236.67 ± 4.71 |     25.70 ± 2.77 |                    |                    |                    |
| nemotron-3-nano-30b-nvfp4 | pp8192 (c20) |  6618.54 ± 3.41 | 1136.13 ± 1403.57 |               |                  | 12241.51 ± 6493.00 | 12187.05 ± 6493.00 | 12241.51 ± 6493.00 |
| nemotron-3-nano-30b-nvfp4 |  tg512 (c20) |   192.82 ± 2.49 |      12.76 ± 2.10 | 360.00 ± 0.00 |     19.02 ± 1.60 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-13 13:50:01 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
