# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-08 12:12:13
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                |         test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------|-------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-bf16 |  pp8192 (c5) | 3524.53 ± 7.13 | 1485.85 ± 858.68 |               |                  |   6620.84 ± 2846.69 |   6512.49 ± 2846.69 |   6620.84 ± 2846.69 |
| qwen3.6-35b-a3b-bf16 |   tg512 (c5) |   52.96 ± 0.54 |     11.70 ± 0.71 |  70.00 ± 0.00 |     16.00 ± 2.28 |                     |                     |                     |
| qwen3.6-35b-a3b-bf16 | pp8192 (c10) | 3558.83 ± 4.69 |  970.51 ± 802.82 |               |                  |  11775.23 ± 5907.67 |  11666.87 ± 5907.67 |  11775.23 ± 5907.67 |
| qwen3.6-35b-a3b-bf16 |  tg512 (c10) |   68.44 ± 2.63 |      7.99 ± 0.74 | 101.33 ± 6.60 |     13.43 ± 3.20 |                     |                     |                     |
| qwen3.6-35b-a3b-bf16 | pp8192 (c20) | 3525.56 ± 5.02 |  604.51 ± 686.84 |               |                  | 22382.85 ± 12100.02 | 22274.50 ± 12100.02 | 22382.85 ± 12100.02 |
| qwen3.6-35b-a3b-bf16 |  tg512 (c20) |   90.90 ± 0.45 |      5.77 ± 0.66 | 160.00 ± 0.00 |     10.87 ± 3.24 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-08 11:55:57 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
