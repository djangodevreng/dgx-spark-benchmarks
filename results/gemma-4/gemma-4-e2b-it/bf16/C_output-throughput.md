# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-06 12:18:59
**Profile:** bf16
**Model:** google/gemma-4-E2B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-e2b-it-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-e2b-it-bf16 |  pp1024 (c1) | 15385.40 ± 813.63 | 15385.40 ± 813.63 |               |                  |   103.03 ± 3.36 |    62.15 ± 3.36 |   103.03 ± 3.36 |
| gemma-4-e2b-it-bf16 |  tg1024 (c1) |      37.55 ± 0.41 |      37.55 ± 0.41 |  39.00 ± 0.00 |     39.00 ± 0.00 |                 |                 |                 |
| gemma-4-e2b-it-bf16 |  pp1024 (c5) | 12576.15 ± 218.06 | 3418.86 ± 1486.55 |               |                  |  343.67 ± 69.58 |  302.80 ± 69.58 |  343.67 ± 69.58 |
| gemma-4-e2b-it-bf16 |  tg1024 (c5) |    156.59 ± 14.12 |      41.64 ± 0.51 | 215.00 ± 0.00 |     43.53 ± 0.50 |                 |                 |                 |
| gemma-4-e2b-it-bf16 | pp1024 (c10) | 13889.31 ± 185.76 | 2928.89 ± 4103.74 |               |                  | 583.15 ± 178.07 | 542.27 ± 178.07 | 583.15 ± 178.07 |
| gemma-4-e2b-it-bf16 | tg1024 (c10) |    249.74 ± 33.14 |      41.85 ± 0.64 | 440.00 ± 0.00 |     44.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-06 12:16:15 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
