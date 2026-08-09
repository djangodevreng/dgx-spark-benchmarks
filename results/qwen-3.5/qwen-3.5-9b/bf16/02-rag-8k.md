# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-07 19:57:45
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.5-9b-bf16 |  pp8192 (c5) |  3686.62 ± 3.92 | 1605.99 ± 982.82 |               |                  |   6242.84 ± 2753.10 |   6146.51 ± 2753.10 |   6242.84 ± 2753.10 |
| qwen3.5-9b-bf16 |   tg512 (c5) |    53.29 ± 0.44 |     11.81 ± 0.65 |  70.00 ± 0.00 |     14.00 ± 0.00 |                     |                     |                     |
| qwen3.5-9b-bf16 | pp8192 (c10) | 3679.23 ± 19.80 | 1015.87 ± 858.01 |               |                  |  11334.42 ± 5693.29 |  11238.09 ± 5693.29 |  11334.42 ± 5693.29 |
| qwen3.5-9b-bf16 |  tg512 (c10) |    84.20 ± 0.57 |     10.25 ± 1.00 | 130.00 ± 0.00 |     13.20 ± 0.40 |                     |                     |                     |
| qwen3.5-9b-bf16 | pp8192 (c20) |  3572.40 ± 4.12 |  639.17 ± 766.17 |               |                  | 21910.42 ± 12024.68 | 21814.09 ± 12024.68 | 21910.42 ± 12024.68 |
| qwen3.5-9b-bf16 |  tg512 (c20) |   108.43 ± 0.22 |      7.28 ± 1.06 | 200.00 ± 0.00 |     12.05 ± 1.33 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-07 19:43:33 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
