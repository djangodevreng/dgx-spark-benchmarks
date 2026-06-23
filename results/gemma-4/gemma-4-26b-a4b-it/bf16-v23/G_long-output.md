# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-06-23 00:44:22
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |     ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|--------------:|---------------:|----------------:|
| gemma-4-26b-a4b |   pp256 (c1) | 1968.24 ± 100.05 | 1968.24 ± 100.05 |               |                  | 230.56 ± 5.96 |  120.02 ± 5.96 |   230.56 ± 5.96 |
| gemma-4-26b-a4b |  tg4096 (c1) |     25.30 ± 0.04 |     25.30 ± 0.04 |  26.00 ± 0.00 |     26.00 ± 0.00 |               |                |                 |
| gemma-4-26b-a4b |   pp256 (c5) |  3406.91 ± 52.06 |  1006.66 ± 66.00 |               |                  | 343.51 ± 2.52 |  232.96 ± 2.52 |   343.51 ± 2.52 |
| gemma-4-26b-a4b |  tg4096 (c5) |    43.19 ± 10.38 |     15.72 ± 2.59 |  80.00 ± 0.00 |     19.20 ± 4.12 |               |                |                 |
| gemma-4-26b-a4b |  pp256 (c10) |  4822.82 ± 53.15 |   623.68 ± 24.60 |               |                  | 490.95 ± 4.88 |  380.40 ± 4.88 |   490.95 ± 4.88 |
| gemma-4-26b-a4b | tg4096 (c10) |     87.16 ± 3.88 |     12.47 ± 0.94 | 127.67 ± 3.30 |     16.31 ± 3.85 |               |                |                 |

llama-benchy (0.3.8)
date: 2026-06-23 00:36:01 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
