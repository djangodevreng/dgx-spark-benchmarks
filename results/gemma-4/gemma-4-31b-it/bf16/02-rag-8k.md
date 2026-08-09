# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-06 16:10:15
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model       |         test |   t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------|-------------:|--------------:|----------------:|-------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-31b |  pp8192 (c5) | 930.53 ± 3.93 | 424.39 ± 285.57 |              |                  | 24731.28 ± 11409.46 | 24341.51 ± 11409.46 | 24731.28 ± 11409.46 |
| gemma-4-31b |   tg512 (c5) |  12.75 ± 0.92 |     3.12 ± 0.24 | 20.00 ± 0.00 |      4.00 ± 0.00 |                     |                     |                     |
| gemma-4-31b | pp8192 (c10) | 938.64 ± 1.50 | 272.48 ± 261.24 |              |                  | 45869.11 ± 23877.38 | 45479.34 ± 23877.38 | 45869.11 ± 23877.38 |
| gemma-4-31b |  tg512 (c10) |  17.94 ± 1.17 |     2.61 ± 0.46 | 40.00 ± 0.00 |      4.00 ± 0.00 |                     |                     |                     |
| gemma-4-31b | pp8192 (c20) | 937.31 ± 0.48 | 166.30 ± 212.94 |              |                  | 86049.91 ± 46028.14 | 85660.14 ± 46028.14 | 86049.91 ± 46028.14 |
| gemma-4-31b |  tg512 (c20) |  26.85 ± 0.94 |     1.88 ± 0.37 | 60.00 ± 0.00 |      3.67 ± 0.47 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-06 15:18:29 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
