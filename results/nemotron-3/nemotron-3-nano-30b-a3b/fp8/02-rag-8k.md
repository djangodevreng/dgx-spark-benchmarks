# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-08 00:28:09
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                   |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-nano-30b-fp8 |  pp8192 (c5) |  8040.96 ± 74.04 | 3303.60 ± 1999.67 |               |                  | 3013.03 ± 1233.45 | 2912.25 ± 1233.45 | 3013.03 ± 1233.45 |
| nemotron-3-nano-30b-fp8 |   tg512 (c5) |     86.12 ± 0.64 |      18.52 ± 0.77 | 108.67 ± 2.87 |     23.27 ± 3.04 |                   |                   |                   |
| nemotron-3-nano-30b-fp8 | pp8192 (c10) |  8309.07 ± 29.44 | 2197.47 ± 1797.05 |               |                  | 5223.64 ± 2583.77 | 5122.87 ± 2583.77 | 5223.64 ± 2583.77 |
| nemotron-3-nano-30b-fp8 |  tg512 (c10) |    111.14 ± 1.72 |      12.76 ± 0.87 | 150.67 ± 0.94 |     16.67 ± 1.96 |                   |                   |                   |
| nemotron-3-nano-30b-fp8 | pp8192 (c20) | 8443.33 ± 166.03 | 1321.40 ± 1432.86 |               |                  | 9603.43 ± 4926.93 | 9502.65 ± 4926.93 | 9603.43 ± 4926.93 |
| nemotron-3-nano-30b-fp8 |  tg512 (c20) |    155.89 ± 0.72 |       9.07 ± 0.74 | 233.33 ± 9.43 |     12.77 ± 1.54 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-08 00:18:30 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
