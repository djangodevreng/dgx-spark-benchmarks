# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-06-23 04:31:14
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-mtp --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-mtp |  pp2048 @ d4 (c1) | 4902.56 ± 414.44 | 4902.56 ± 414.44 |               |                  |   544.76 ± 43.30 |   396.24 ± 43.30 |   544.76 ± 43.30 |
| gemma-4-26b-a4b-mtp |   tg512 @ d4 (c1) |     33.64 ± 2.79 |     33.64 ± 2.79 |  44.33 ± 4.50 |     44.33 ± 4.50 |                  |                  |                  |
| gemma-4-26b-a4b-mtp |  pp2048 @ d4 (c5) |  5218.09 ± 37.15 | 1570.83 ± 599.59 |               |                  | 1466.30 ± 321.58 | 1317.78 ± 321.58 | 1466.30 ± 321.58 |
| gemma-4-26b-a4b-mtp |   tg512 @ d4 (c5) |     88.89 ± 2.09 |     20.87 ± 2.47 | 129.33 ± 3.77 |     34.27 ± 3.53 |                  |                  |                  |
| gemma-4-26b-a4b-mtp | pp2048 @ d4 (c10) |  5557.31 ± 34.00 |  979.27 ± 394.74 |               |                  | 2368.00 ± 789.47 | 2219.47 ± 789.47 | 2368.00 ± 789.47 |
| gemma-4-26b-a4b-mtp |  tg512 @ d4 (c10) |    143.47 ± 4.67 |     16.57 ± 1.32 | 201.33 ± 0.47 |     28.23 ± 3.41 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-23 04:25:59 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
