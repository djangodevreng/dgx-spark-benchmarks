# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-06 03:36:36
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model       |         test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------|-------------:|---------------:|----------------:|-------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-31b |  pp8192 (c5) | 1003.40 ± 6.21 | 441.46 ± 287.30 |              |                  | 23470.71 ± 10553.09 | 23075.15 ± 10553.09 | 23470.71 ± 10553.09 |
| gemma-4-31b |   tg512 (c5) |   11.54 ± 0.12 |     3.12 ± 0.24 | 20.00 ± 0.00 |      4.00 ± 0.00 |                     |                     |                     |
| gemma-4-31b | pp8192 (c10) |  991.49 ± 8.58 | 271.51 ± 250.20 |              |                  | 44193.68 ± 22441.81 | 43798.12 ± 22441.81 | 44193.68 ± 22441.81 |
| gemma-4-31b |  tg512 (c10) |   19.44 ± 1.51 |     2.68 ± 0.47 | 40.00 ± 0.00 |      4.00 ± 0.00 |                     |                     |                     |
| gemma-4-31b | pp8192 (c20) |  995.38 ± 1.79 | 170.37 ± 205.01 |              |                  | 81249.95 ± 43309.60 | 80854.39 ± 43309.60 | 81249.95 ± 43309.60 |
| gemma-4-31b |  tg512 (c20) |   27.30 ± 1.28 |     2.04 ± 0.50 | 63.00 ± 1.41 |      3.78 ± 0.41 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-06 02:59:40 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
