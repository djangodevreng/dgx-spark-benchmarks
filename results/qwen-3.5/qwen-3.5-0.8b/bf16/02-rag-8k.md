# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-07 09:26:16
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model             |         test |      t/s (total) |          t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:------------------|-------------:|-----------------:|-------------------:|---------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.5-0.8b-bf16 |  pp8192 (c5) | 25792.81 ± 81.80 | 11271.48 ± 6841.12 |                |                  |   901.33 ± 391.76 |   878.06 ± 391.76 |   901.33 ± 391.76 |
| qwen3.5-0.8b-bf16 |   tg512 (c5) |   397.99 ± 20.38 |       96.15 ± 6.13 | 533.33 ± 11.79 |    108.67 ± 3.30 |                   |                   |                   |
| qwen3.5-0.8b-bf16 | pp8192 (c10) | 25630.23 ± 67.65 |  7218.51 ± 6176.76 |                |                  |  1630.45 ± 820.91 |  1607.18 ± 820.91 |  1630.45 ± 820.91 |
| qwen3.5-0.8b-bf16 |  tg512 (c10) |   585.46 ± 14.38 |       73.74 ± 9.22 |  870.00 ± 0.00 |     91.77 ± 2.73 |                   |                   |                   |
| qwen3.5-0.8b-bf16 | pp8192 (c20) | 24872.50 ± 82.36 |  4368.49 ± 4927.92 |                |                  | 3134.95 ± 1716.67 | 3111.68 ± 1716.67 | 3134.95 ± 1716.67 |
| qwen3.5-0.8b-bf16 |  tg512 (c20) |   694.12 ± 14.65 |      49.31 ± 10.17 | 1228.67 ± 5.19 |     74.02 ± 8.85 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-07 09:24:20 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
