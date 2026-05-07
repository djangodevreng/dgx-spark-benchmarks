# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-06 12:31:36
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model               |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:--------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| gemma-4-e2b-it-bf16 |  pp8192 (c5) |  11011.40 ± 39.54 | 4666.95 ± 2864.41 |               |                  |  2146.86 ± 932.21 |  2106.24 ± 932.21 |  2146.86 ± 932.21 |
| gemma-4-e2b-it-bf16 |   tg512 (c5) |     163.50 ± 1.71 |      36.10 ± 2.31 | 205.00 ± 0.00 |     41.00 ± 0.00 |                   |                   |                   |
| gemma-4-e2b-it-bf16 | pp8192 (c10) | 10891.43 ± 230.93 | 2851.38 ± 2393.32 |               |                  | 4041.36 ± 2016.00 | 4000.73 ± 2016.00 | 4041.36 ± 2016.00 |
| gemma-4-e2b-it-bf16 |  tg512 (c10) |     260.35 ± 3.70 |      32.52 ± 4.03 | 400.00 ± 0.00 |     40.27 ± 0.44 |                   |                   |                   |
| gemma-4-e2b-it-bf16 | pp8192 (c20) |  11101.48 ± 49.64 | 1741.04 ± 1888.72 |               |                  | 7382.63 ± 3828.99 | 7342.01 ± 3828.99 | 7382.63 ± 3828.99 |
| gemma-4-e2b-it-bf16 |  tg512 (c20) |     339.83 ± 7.31 |      23.82 ± 4.60 | 660.00 ± 0.00 |     33.97 ± 1.02 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-06 12:28:17 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
