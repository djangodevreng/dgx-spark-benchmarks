# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-06 14:23:40
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-e4b-it-bf16 |  pp8192 (c5) | 6144.73 ± 250.32 | 2604.20 ± 1604.00 |               |                  |  3868.21 ± 1693.66 |  3795.94 ± 1693.66 |  3868.21 ± 1693.66 |
| gemma-4-e4b-it-bf16 |   tg512 (c5) |     79.49 ± 3.35 |      18.93 ± 1.32 | 110.00 ± 0.00 |     22.00 ± 0.00 |                    |                    |                    |
| gemma-4-e4b-it-bf16 | pp8192 (c10) |  6371.07 ± 52.03 | 1752.75 ± 1596.15 |               |                  |  6846.60 ± 3482.50 |  6774.34 ± 3482.50 |  6846.60 ± 3482.50 |
| gemma-4-e4b-it-bf16 |  tg512 (c10) |    129.14 ± 1.31 |      16.55 ± 2.90 | 210.00 ± 0.00 |     21.00 ± 0.00 |                    |                    |                    |
| gemma-4-e4b-it-bf16 | pp8192 (c20) |  6488.86 ± 12.62 | 1078.34 ± 1275.42 |               |                  | 12531.30 ± 6598.96 | 12459.04 ± 6598.96 | 12531.30 ± 6598.96 |
| gemma-4-e4b-it-bf16 |  tg512 (c20) |    179.72 ± 9.21 |      12.50 ± 3.28 | 358.33 ± 2.36 |     18.75 ± 0.94 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-06 14:17:37 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
