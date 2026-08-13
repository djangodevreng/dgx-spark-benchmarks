# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-12 04:33:56
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|----------------:|-------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| muse-glimmer-30b-bf16 |  pp8192 (c5) | 1473.03 ± 13.41 | 709.74 ± 484.85 |              |                  |  15089.91 ± 7134.62 |  14826.76 ± 7134.62 |  23637.79 ± 2521.51 |
| muse-glimmer-30b-bf16 |   tg512 (c5) |    19.51 ± 0.32 |     4.06 ± 0.07 | 25.00 ± 0.00 |      5.00 ± 0.00 |                     |                     |                     |
| muse-glimmer-30b-bf16 | pp8192 (c10) |  1475.69 ± 7.45 | 441.39 ± 431.77 |              |                  | 28816.08 ± 15050.28 | 28552.93 ± 15050.28 | 40956.04 ± 10543.32 |
| muse-glimmer-30b-bf16 |  tg512 (c10) |    31.98 ± 0.79 |     3.71 ± 0.26 | 50.00 ± 0.00 |      5.00 ± 0.00 |                     |                     |                     |
| muse-glimmer-30b-bf16 | pp8192 (c20) | 1468.82 ± 11.90 | 268.45 ± 359.46 |              |                  | 54169.70 ± 29105.65 | 53906.55 ± 29105.65 | 68636.27 ± 26065.41 |
| muse-glimmer-30b-bf16 |  tg512 (c20) |    43.97 ± 0.67 |     2.90 ± 0.40 | 80.00 ± 0.00 |      4.38 ± 0.49 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-12 03:55:25 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
