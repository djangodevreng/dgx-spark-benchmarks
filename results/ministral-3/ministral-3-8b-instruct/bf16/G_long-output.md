# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-07 18:11:51
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| ministral-3-8b-instruct-bf16 |   pp256 (c1) |  1289.24 ± 83.54 |  1289.24 ± 83.54 |               |                  | 241.68 ± 20.89 | 175.79 ± 20.89 |  241.68 ± 20.89 |
| ministral-3-8b-instruct-bf16 |  tg4096 (c1) |     22.01 ± 0.02 |     22.01 ± 0.02 |  23.00 ± 0.00 |     23.00 ± 0.00 |                |                |                 |
| ministral-3-8b-instruct-bf16 |   pp256 (c5) | 5602.40 ± 201.88 | 1760.17 ± 481.21 |               |                  | 204.49 ± 20.16 | 138.60 ± 20.16 |  204.49 ± 20.16 |
| ministral-3-8b-instruct-bf16 |  tg4096 (c5) |    69.94 ± 22.17 |     23.77 ± 0.69 | 125.00 ± 0.00 |     25.00 ± 0.00 |                |                |                 |
| ministral-3-8b-instruct-bf16 |  pp256 (c10) | 7310.82 ± 106.91 |   922.52 ± 55.94 |               |                  |  321.06 ± 1.44 |  255.18 ± 1.44 |   321.06 ± 1.44 |
| ministral-3-8b-instruct-bf16 | tg4096 (c10) |    72.72 ± 12.75 |     23.55 ± 0.50 | 250.00 ± 0.00 |     25.00 ± 0.00 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-07 17:57:36 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
