# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-16 12:25:36
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:---------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-26b-a4b-bf16 |  pp8192 (c5) | 4819.34 ± 16.22 | 2255.77 ± 1496.39 |               |                  |  4707.04 ± 2188.96 |  4587.64 ± 2188.96 |  4707.04 ± 2188.96 |
| gemma-4-26b-a4b-bf16 |   tg512 (c5) |    53.53 ± 2.11 |      12.12 ± 0.65 |  70.00 ± 0.00 |     15.93 ± 1.06 |                    |                    |                    |
| gemma-4-26b-a4b-bf16 | pp8192 (c10) |  4836.86 ± 9.88 | 1422.35 ± 1358.34 |               |                  |  8805.78 ± 4590.36 |  8686.38 ± 4590.36 |  8805.78 ± 4590.36 |
| gemma-4-26b-a4b-bf16 |  tg512 (c10) |    74.55 ± 1.22 |       8.91 ± 0.79 | 108.00 ± 2.83 |     12.57 ± 1.48 |                    |                    |                    |
| gemma-4-26b-a4b-bf16 | pp8192 (c20) | 4818.87 ± 33.91 |  858.63 ± 1093.06 |               |                  | 16719.75 ± 8921.96 | 16600.35 ± 8921.96 | 16719.75 ± 8921.96 |
| gemma-4-26b-a4b-bf16 |  tg512 (c20) |    94.06 ± 1.60 |       5.81 ± 0.64 | 152.67 ± 6.13 |      9.48 ± 1.65 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-16 12:11:05 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
