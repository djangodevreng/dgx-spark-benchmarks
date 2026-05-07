# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-06 12:33:52
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-e2b-it-bf16 |   pp256 (c1) | 12012.27 ± 7257.98 | 12012.27 ± 7257.98 |               |                  |  85.14 ± 40.52 |  43.84 ± 40.52 |   85.14 ± 40.52 |
| gemma-4-e2b-it-bf16 |  tg4096 (c1) |       38.70 ± 0.01 |       38.70 ± 0.01 |  39.33 ± 0.47 |     39.33 ± 0.47 |                |                |                 |
| gemma-4-e2b-it-bf16 |   pp256 (c5) |   9700.61 ± 528.78 |   2993.60 ± 257.92 |               |                  |  118.77 ± 2.93 |   77.47 ± 2.93 |   118.77 ± 2.93 |
| gemma-4-e2b-it-bf16 |  tg4096 (c5) |      118.10 ± 6.92 |       42.16 ± 0.64 | 209.33 ± 8.01 |     43.81 ± 0.66 |                |                |                 |
| gemma-4-e2b-it-bf16 |  pp256 (c10) |  12397.47 ± 126.88 |  3038.70 ± 2805.70 |               |                  | 161.55 ± 49.00 | 120.25 ± 49.00 |  161.55 ± 49.00 |
| gemma-4-e2b-it-bf16 | tg4096 (c10) |     297.96 ± 36.65 |       42.73 ± 0.24 | 440.00 ± 0.00 |     44.03 ± 0.18 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-06 12:31:37 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
