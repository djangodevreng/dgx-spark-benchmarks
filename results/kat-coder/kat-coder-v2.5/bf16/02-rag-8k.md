# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-13 16:44:18
**Profile:** bf16
**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model kat-coder-v2-5-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:--------------------|-------------:|---------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| kat-coder-v2-5-bf16 |  pp8192 (c5) | 4976.63 ± 5.86 | 1872.79 ± 1022.33 |               |                  |  5103.39 ± 1972.29 |  4988.90 ± 1972.29 |  5103.39 ± 1972.29 |
| kat-coder-v2-5-bf16 |   tg512 (c5) |   54.31 ± 0.83 |      13.59 ± 1.93 |  80.00 ± 0.00 |     20.80 ± 4.65 |                    |                    |                    |
| kat-coder-v2-5-bf16 | pp8192 (c10) | 4884.36 ± 7.83 |  1173.15 ± 933.22 |               |                  |  9445.08 ± 4405.40 |  9330.60 ± 4405.40 |  9445.08 ± 4405.40 |
| kat-coder-v2-5-bf16 |  tg512 (c10) |   65.52 ± 2.84 |       8.36 ± 0.88 | 103.67 ± 4.50 |     13.90 ± 4.04 |                    |                    |                    |
| kat-coder-v2-5-bf16 | pp8192 (c20) | 4949.73 ± 3.07 |   760.60 ± 826.83 |               |                  | 16940.99 ± 8657.00 | 16826.51 ± 8657.00 | 16940.99 ± 8657.00 |
| kat-coder-v2-5-bf16 |  tg512 (c20) |   86.58 ± 2.44 |       6.11 ± 0.95 | 160.00 ± 0.00 |     10.62 ± 2.27 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-13 16:30:42 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
