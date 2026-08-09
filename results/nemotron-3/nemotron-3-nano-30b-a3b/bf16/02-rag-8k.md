# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-09 03:07:06
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                    |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:-------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-3-nano-30b-bf16 |  pp8192 (c5) | 6761.39 ± 27.73 | 3171.96 ± 2181.66 |               |                  |  3396.83 ± 1547.30 |  3272.38 ± 1547.30 |  3396.83 ± 1547.30 |
| nemotron-3-nano-30b-bf16 |   tg512 (c5) |    51.20 ± 0.02 |      10.76 ± 0.33 |  62.00 ± 2.16 |     12.87 ± 0.72 |                    |                    |                    |
| nemotron-3-nano-30b-bf16 | pp8192 (c10) | 6828.50 ± 12.59 | 2003.67 ± 1914.09 |               |                  |  6283.43 ± 3228.69 |  6158.98 ± 3228.69 |  6283.43 ± 3228.69 |
| nemotron-3-nano-30b-bf16 |  tg512 (c10) |    67.50 ± 0.21 |       7.29 ± 0.31 |  90.00 ± 0.00 |      9.70 ± 1.00 |                    |                    |                    |
| nemotron-3-nano-30b-bf16 | pp8192 (c20) | 6897.33 ± 11.02 | 1222.60 ± 1551.42 |               |                  | 11628.84 ± 6178.98 | 11504.38 ± 6178.98 | 11628.84 ± 6178.98 |
| nemotron-3-nano-30b-bf16 |  tg512 (c20) |    96.02 ± 1.51 |       5.43 ± 0.32 | 140.00 ± 0.00 |      8.17 ± 1.49 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-09 02:51:20 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
