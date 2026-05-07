# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-05 20:53:00
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b-bf16 |  pp25000 (c5) | 3559.17 ± 6.72 | 1557.53 ± 983.46 |               |                  |  19859.37 ± 8996.55 |  19740.39 ± 8996.55 |  19859.52 ± 8996.75 |
| gemma-4-26b-a4b-bf16 |    tg256 (c5) |   27.88 ± 0.05 |      8.51 ± 2.40 |  65.00 ± 0.00 |     13.60 ± 0.80 |                     |                     |                     |
| gemma-4-26b-a4b-bf16 | pp25000 (c10) | 3569.77 ± 2.99 | 1000.28 ± 873.70 |               |                  | 35441.37 ± 17952.77 | 35322.39 ± 17952.77 | 35442.23 ± 17952.74 |
| gemma-4-26b-a4b-bf16 |   tg256 (c10) |   30.68 ± 0.09 |      5.37 ± 1.99 | 100.00 ± 0.00 |     11.73 ± 1.61 |                     |                     |                     |
| gemma-4-26b-a4b-bf16 | pp25000 (c20) | 3563.64 ± 8.78 |  615.12 ± 718.51 |               |                  | 67367.91 ± 36441.67 | 67248.93 ± 36441.67 | 67368.20 ± 36441.84 |
| gemma-4-26b-a4b-bf16 |   tg256 (c20) |   32.26 ± 0.10 |      3.16 ± 1.41 | 140.00 ± 0.00 |      9.77 ± 2.38 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-05 20:37:35 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
