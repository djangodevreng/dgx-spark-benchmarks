# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-07 21:04:36
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model           |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.5-4b-bf16 |  pp25000 (c5) | 5798.52 ± 1.59 | 2553.16 ± 1540.80 |               |                  |  11908.02 ± 5414.04 |  11847.51 ± 5414.04 |  11908.14 ± 5414.21 |
| qwen3.5-4b-bf16 |    tg256 (c5) |   46.22 ± 0.11 |      14.41 ± 3.83 | 105.00 ± 0.00 |     22.27 ± 0.77 |                     |                     |                     |
| qwen3.5-4b-bf16 | pp25000 (c10) | 5631.47 ± 3.89 | 1600.31 ± 1347.29 |               |                  | 22125.97 ± 11433.54 | 22065.46 ± 11433.54 | 22126.98 ± 11433.61 |
| qwen3.5-4b-bf16 |   tg256 (c10) |   51.18 ± 0.09 |       9.77 ± 3.85 | 180.00 ± 0.00 |     20.60 ± 2.15 |                     |                     |                     |
| qwen3.5-4b-bf16 | pp25000 (c20) | 5365.04 ± 5.97 |  987.98 ± 1143.96 |               |                  | 43183.89 ± 24332.21 | 43123.38 ± 24332.21 | 43184.99 ± 24332.36 |
| qwen3.5-4b-bf16 |   tg256 (c20) |   52.87 ± 0.02 |       6.09 ± 3.33 | 260.00 ± 0.00 |     17.37 ± 3.45 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-07 20:55:08 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
