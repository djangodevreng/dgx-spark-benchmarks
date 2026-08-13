# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-09 10:51:09
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-cascade-2-30b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                       |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-cascade-2-30b-bf16 |  pp8192 (c5) |  6868.28 ± 5.68 | 3305.37 ± 2262.97 |               |                  |  3343.37 ± 1522.96 |  3168.82 ± 1522.96 |  3343.37 ± 1522.96 |
| nemotron-cascade-2-30b-bf16 |   tg512 (c5) |    51.35 ± 0.45 |      10.78 ± 0.34 |  63.33 ± 2.36 |     12.87 ± 0.50 |                    |                    |                    |
| nemotron-cascade-2-30b-bf16 | pp8192 (c10) | 6915.74 ± 11.56 | 2088.04 ± 2031.70 |               |                  |  6215.01 ± 3194.80 |  6040.46 ± 3194.80 |  6215.01 ± 3194.80 |
| nemotron-cascade-2-30b-bf16 |  tg512 (c10) |    67.24 ± 0.44 |       7.25 ± 0.31 |  90.00 ± 0.00 |      9.70 ± 1.00 |                    |                    |                    |
| nemotron-cascade-2-30b-bf16 | pp8192 (c20) |  6982.30 ± 5.29 | 1263.60 ± 1649.68 |               |                  | 11528.14 ± 6117.91 | 11353.59 ± 6117.91 | 11528.14 ± 6117.91 |
| nemotron-cascade-2-30b-bf16 |  tg512 (c20) |    98.48 ± 0.47 |       5.54 ± 0.33 | 140.33 ± 0.47 |      8.17 ± 1.47 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-09 10:35:32 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
