# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-07 12:36:59
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                          |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:-------------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-3-nano-omni-30b-nvfp4 |  pp8192 (c5) |   6954.26 ± 4.56 | 2776.00 ± 1534.43 |               |                  |  3431.28 ± 1435.57 |  3377.03 ± 1435.57 |  3431.28 ± 1435.57 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg512 (c5) |    125.95 ± 0.31 |      28.35 ± 2.19 | 161.67 ± 2.36 |     33.73 ± 2.32 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 | pp8192 (c10) | 7383.21 ± 110.01 | 1872.54 ± 1490.98 |               |                  |  5973.59 ± 2919.50 |  5919.34 ± 2919.50 |  5973.59 ± 2919.50 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg512 (c10) |    152.90 ± 4.75 |      19.73 ± 3.20 | 240.00 ± 0.00 |     28.00 ± 3.66 |                    |                    |                    |
| nemotron-3-nano-omni-30b-nvfp4 | pp8192 (c20) |  7604.01 ± 38.26 | 1193.43 ± 1289.55 |               |                  | 10670.77 ± 5525.52 | 10616.53 ± 5525.52 | 10670.77 ± 5525.52 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg512 (c20) |    203.15 ± 4.96 |      13.76 ± 2.88 | 379.33 ± 0.94 |     21.38 ± 2.09 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-07 12:30:16 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
