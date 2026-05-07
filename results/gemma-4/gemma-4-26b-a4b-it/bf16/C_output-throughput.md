# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-05 20:59:32
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-bf16 |  pp1024 (c1) | 4627.12 ± 374.91 |  4627.12 ± 374.91 |               |                  |   309.12 ± 19.38 |   193.21 ± 19.38 |   309.12 ± 19.38 |
| gemma-4-26b-a4b-bf16 |  tg1024 (c1) |     23.86 ± 0.03 |      23.86 ± 0.03 |  25.00 ± 0.00 |     25.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 |  pp1024 (c5) | 5701.55 ± 561.36 |  1515.14 ± 284.33 |               |                  |  757.87 ± 109.96 |  641.96 ± 109.96 |  757.87 ± 109.96 |
| gemma-4-26b-a4b-bf16 |  tg1024 (c5) |     54.67 ± 4.90 |      13.59 ± 1.05 |  73.33 ± 2.36 |     17.13 ± 3.79 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 | pp1024 (c10) |  6346.87 ± 64.52 | 1147.76 ± 1040.37 |               |                  | 1259.44 ± 403.83 | 1143.53 ± 403.83 | 1259.44 ± 403.83 |
| gemma-4-26b-a4b-bf16 | tg1024 (c10) |     86.46 ± 1.74 |      10.92 ± 0.73 | 126.67 ± 9.43 |     15.00 ± 3.80 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-05 20:53:01 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
