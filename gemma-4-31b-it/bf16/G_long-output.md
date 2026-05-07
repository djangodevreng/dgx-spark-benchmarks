# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-06 03:54:18
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model       |         test |         t/s (total) |           t/s (req) |     peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------|-------------:|--------------------:|--------------------:|-------------:|-----------------:|----------------:|----------------:|----------------:|
| gemma-4-31b |   pp256 (c1) | 39535.46 ± 54556.04 | 39535.46 ± 54556.04 |              |                  | 559.11 ± 120.54 | 172.21 ± 120.54 | 559.11 ± 120.54 |
| gemma-4-31b |  tg4096 (c1) |         3.74 ± 0.00 |         3.74 ± 0.00 |  4.00 ± 0.00 |      4.00 ± 0.00 |                 |                 |                 |
| gemma-4-31b |   pp256 (c5) |       988.98 ± 9.62 |      293.84 ± 16.79 |              |                  | 1186.84 ± 29.81 |  799.94 ± 29.81 | 1186.84 ± 29.81 |
| gemma-4-31b |  tg4096 (c5) |         9.55 ± 2.68 |         3.54 ± 0.24 | 20.00 ± 0.00 |      4.05 ± 0.21 |                 |                 |                 |
| gemma-4-31b |  pp256 (c10) |      1117.44 ± 6.51 |       137.29 ± 5.82 |              |                  | 2085.02 ± 31.28 | 1698.12 ± 31.28 | 2085.02 ± 31.28 |
| gemma-4-31b | tg4096 (c10) |        19.18 ± 2.87 |         3.55 ± 0.08 | 40.00 ± 0.00 |      4.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-06 03:36:38 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
