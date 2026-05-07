# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-06 14:03:04
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e4b-it-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |        t/s (total) |          t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|-------------:|-------------------:|-------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-e4b-it-bf16 |  pp1024 (c1) | 10124.36 ± 2740.76 | 10124.36 ± 2740.76 |               |                  |   182.20 ± 21.54 |    99.69 ± 21.54 |   182.20 ± 21.54 |
| gemma-4-e4b-it-bf16 |  tg1024 (c1) |       18.88 ± 0.06 |       18.88 ± 0.06 |  20.00 ± 0.00 |     20.00 ± 0.00 |                  |                  |                  |
| gemma-4-e4b-it-bf16 |  pp1024 (c5) |    7211.04 ± 56.04 |    1656.37 ± 50.33 |               |                  |    643.49 ± 7.57 |    560.98 ± 7.57 |    643.49 ± 7.57 |
| gemma-4-e4b-it-bf16 |  tg1024 (c5) |       69.47 ± 8.05 |       21.58 ± 0.41 | 108.67 ± 1.89 |     22.66 ± 0.47 |                  |                  |                  |
| gemma-4-e4b-it-bf16 | pp1024 (c10) |   7533.56 ± 176.17 |  1283.11 ± 2200.11 |               |                  | 1104.36 ± 191.61 | 1021.85 ± 191.61 | 1104.36 ± 191.61 |
| gemma-4-e4b-it-bf16 | tg1024 (c10) |      120.68 ± 3.05 |       21.40 ± 0.19 | 220.00 ± 0.00 |     22.80 ± 0.40 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-06 13:57:46 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
