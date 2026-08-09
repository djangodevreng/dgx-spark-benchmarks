# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-07 14:36:58
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-2b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------|-------------:|------------------:|------------------:|---------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.5-2b-bf16 |  pp8192 (c5) | 14726.19 ± 445.66 | 6100.50 ± 3479.20 |                |                  |  1592.75 ± 665.85 |  1557.21 ± 665.85 |  1592.75 ± 665.85 |
| qwen3.5-2b-bf16 |   tg512 (c5) |     159.36 ± 9.17 |      44.03 ± 8.67 |  255.67 ± 3.68 |     52.60 ± 2.47 |                   |                   |                   |
| qwen3.5-2b-bf16 | pp8192 (c10) |  15252.82 ± 30.56 | 4247.26 ± 3584.34 |                |                  | 2738.39 ± 1373.18 | 2702.85 ± 1373.18 | 2738.39 ± 1373.18 |
| qwen3.5-2b-bf16 |  tg512 (c10) |    285.94 ± 11.29 |      38.29 ± 9.37 | 448.00 ± 15.58 |     47.27 ± 9.48 |                   |                   |                   |
| qwen3.5-2b-bf16 | pp8192 (c20) |  15007.92 ± 28.19 | 2634.58 ± 3037.47 |                |                  | 5228.98 ± 2847.75 | 5193.45 ± 2847.75 | 5228.98 ± 2847.75 |
| qwen3.5-2b-bf16 |  tg512 (c20) |    364.33 ± 40.85 |      27.93 ± 6.81 | 701.33 ± 14.73 |     42.63 ± 6.91 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-07 14:33:35 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
