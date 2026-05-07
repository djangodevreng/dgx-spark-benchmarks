# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-06 02:59:39
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model       |              test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------|------------------:|-----------------:|-----------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-31b |  pp2048 @ d4 (c1) | 1161.36 ± 178.97 | 1161.36 ± 178.97 |              |                  |   2006.34 ± 304.90 |   1612.97 ± 304.90 |   2006.34 ± 304.90 |
| gemma-4-31b |   tg512 @ d4 (c1) |      3.69 ± 0.04 |      3.69 ± 0.04 |  4.00 ± 0.00 |      4.00 ± 0.00 |                    |                    |                    |
| gemma-4-31b |  pp2048 @ d4 (c5) |  1133.83 ± 24.56 |  418.63 ± 366.62 |              |                  |  6801.06 ± 2381.49 |  6407.68 ± 2381.49 |  6801.06 ± 2381.49 |
| gemma-4-31b |   tg512 @ d4 (c5) |     13.06 ± 0.42 |      3.42 ± 0.27 | 20.00 ± 0.00 |      4.00 ± 0.00 |                    |                    |                    |
| gemma-4-31b | pp2048 @ d4 (c10) |   1141.30 ± 8.36 |  257.89 ± 324.19 |              |                  | 11764.72 ± 4478.80 | 11371.35 ± 4478.80 | 11764.72 ± 4478.80 |
| gemma-4-31b |  tg512 @ d4 (c10) |     22.06 ± 1.31 |      3.23 ± 0.22 | 40.00 ± 0.00 |      4.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-06 02:39:19 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
