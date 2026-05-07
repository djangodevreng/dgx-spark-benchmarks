# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-06 01:29:14
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model       |          test |   t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:------------|--------------:|--------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| gemma-4-31b |  pp25000 (c5) | 715.30 ± 2.36 | 311.27 ± 195.36 |              |                  |   98820.17 ± 44899.22 |   98437.70 ± 44899.22 |   98821.81 ± 44899.59 |
| gemma-4-31b |    tg256 (c5) |   6.30 ± 0.02 |     2.10 ± 0.72 | 20.00 ± 0.00 |      4.00 ± 0.00 |                       |                       |                       |
| gemma-4-31b | pp25000 (c10) | 717.33 ± 1.00 | 201.61 ± 178.66 |              |                  |  177179.24 ± 89912.67 |  176796.77 ± 89912.67 |  177179.67 ± 89912.56 |
| gemma-4-31b |   tg256 (c10) |   6.94 ± 0.02 |     1.41 ± 0.69 | 38.33 ± 2.36 |      3.93 ± 0.25 |                       |                       |                       |
| gemma-4-31b | pp25000 (c20) | 713.94 ± 1.26 | 123.30 ± 144.99 |              |                  | 335975.22 ± 181584.10 | 335592.75 ± 181584.10 | 335975.79 ± 181584.23 |
| gemma-4-31b |   tg256 (c20) |   7.18 ± 0.12 |     0.86 ± 0.55 | 60.00 ± 0.00 |      3.43 ± 0.50 |                       |                       |                       |

llama-benchy (0.3.7)
date: 2026-05-06 00:20:26 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
