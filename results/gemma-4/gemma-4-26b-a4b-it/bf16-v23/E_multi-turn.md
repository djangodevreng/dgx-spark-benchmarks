# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-06-23 00:22:16
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b |  pp2048 @ d4 (c1) | 5368.20 ± 107.68 | 5368.20 ± 107.68 |               |                  |   454.20 ± 13.26 |   344.32 ± 13.26 |   454.20 ± 13.26 |
| gemma-4-26b-a4b |   tg512 @ d4 (c1) |     25.02 ± 0.01 |     25.02 ± 0.01 |  26.00 ± 0.00 |     26.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b |  pp2048 @ d4 (c5) |  5745.57 ± 24.74 | 1755.24 ± 636.59 |               |                  | 1289.06 ± 333.45 | 1179.19 ± 333.45 | 1289.06 ± 333.45 |
| gemma-4-26b-a4b |   tg512 @ d4 (c5) |     66.03 ± 1.57 |     13.64 ± 0.16 |  75.00 ± 0.00 |     15.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b | pp2048 @ d4 (c10) |  6100.81 ± 28.38 | 1257.43 ± 908.63 |               |                  | 2154.60 ± 858.63 | 2044.72 ± 858.63 | 2154.60 ± 858.63 |
| gemma-4-26b-a4b |  tg512 @ d4 (c10) |     98.35 ± 3.95 |     10.69 ± 0.25 | 123.33 ± 4.71 |     13.20 ± 0.91 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-23 00:15:04 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
