# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-06-23 04:46:08
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-mtp --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-26b-a4b-mtp |   pp256 (c1) | 1849.45 ± 111.56 | 1849.45 ± 111.56 |               |                  |  282.74 ± 2.94 |  132.04 ± 2.94 |   282.74 ± 2.94 |
| gemma-4-26b-a4b-mtp |  tg4096 (c1) |     34.38 ± 1.38 |     34.38 ± 1.38 |  50.33 ± 4.50 |     50.33 ± 4.50 |                |                |                 |
| gemma-4-26b-a4b-mtp |   pp256 (c5) |  2886.51 ± 61.01 |   916.75 ± 55.83 |               |                  |  408.45 ± 7.68 |  257.75 ± 7.68 |   408.45 ± 7.68 |
| gemma-4-26b-a4b-mtp |  tg4096 (c5) |     76.27 ± 3.41 |     21.52 ± 2.63 | 120.67 ± 7.41 |     32.73 ± 6.88 |                |                |                 |
| gemma-4-26b-a4b-mtp |  pp256 (c10) |  4211.49 ± 49.68 |   575.82 ± 32.72 |               |                  | 564.16 ± 14.86 | 413.46 ± 14.86 |  564.16 ± 14.86 |
| gemma-4-26b-a4b-mtp | tg4096 (c10) |    127.52 ± 9.05 |     17.67 ± 1.92 | 204.33 ± 9.88 |     28.97 ± 4.13 |                |                |                 |

llama-benchy (0.3.8)
date: 2026-06-23 04:42:08 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
