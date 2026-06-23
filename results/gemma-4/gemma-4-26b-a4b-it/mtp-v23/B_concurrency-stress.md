# Run B — 25k context, c=5/10/20

**Generated:** 2026-06-23 04:20:04
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-mtp --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b-mtp |  pp25000 (c5) | 2786.99 ± 2.62 | 1230.43 ± 777.08 |               |                  | 25039.77 ± 11378.31 | 24887.57 ± 11378.31 | 25040.92 ± 11378.26 |
| gemma-4-26b-a4b-mtp |    tg256 (c5) |   27.27 ± 0.32 |     10.53 ± 4.78 | 113.33 ± 5.19 |     28.07 ± 2.62 |                     |                     |                     |
| gemma-4-26b-a4b-mtp | pp25000 (c10) | 2776.34 ± 4.51 |  791.10 ± 701.65 |               |                  | 45450.80 ± 23256.44 | 45298.60 ± 23256.44 | 45451.00 ± 23256.54 |
| gemma-4-26b-a4b-mtp |   tg256 (c10) |   26.42 ± 1.02 |      6.01 ± 3.58 | 152.33 ± 6.55 |     23.20 ± 3.45 |                     |                     |                     |
| gemma-4-26b-a4b-mtp | pp25000 (c20) | 2755.96 ± 4.60 |  489.28 ± 584.78 |               |                  | 86327.15 ± 47236.74 | 86174.95 ± 47236.74 | 86327.76 ± 47236.88 |
| gemma-4-26b-a4b-mtp |   tg256 (c20) |   28.16 ± 0.25 |      3.63 ± 2.50 | 223.67 ± 7.36 |     18.28 ± 2.43 |                     |                     |                     |

llama-benchy (0.3.8)
date: 2026-06-23 03:56:58 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
