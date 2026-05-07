# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-05 21:22:22
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-bf16 |  pp2048 @ d4 (c1) | 4716.21 ± 542.88 |  4716.21 ± 542.88 |               |                  |   527.32 ± 59.88 |   404.74 ± 59.88 |   527.32 ± 59.88 |
| gemma-4-26b-a4b-bf16 |   tg512 @ d4 (c1) |     23.97 ± 0.10 |      23.97 ± 0.10 |  25.00 ± 0.00 |     25.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 |  pp2048 @ d4 (c5) | 5693.39 ± 128.08 | 1883.80 ± 1125.59 |               |                  | 1320.45 ± 387.41 | 1197.86 ± 387.41 | 1320.45 ± 387.41 |
| gemma-4-26b-a4b-bf16 |   tg512 @ d4 (c5) |     59.48 ± 2.26 |      13.07 ± 0.16 |  73.33 ± 2.36 |     14.87 ± 0.50 |                  |                  |                  |
| gemma-4-26b-a4b-bf16 | pp2048 @ d4 (c10) |  6096.81 ± 56.92 | 1348.78 ± 1225.13 |               |                  | 2126.73 ± 826.47 | 2004.14 ± 826.47 | 2126.73 ± 826.47 |
| gemma-4-26b-a4b-bf16 |  tg512 @ d4 (c10) |     92.42 ± 3.33 |      10.43 ± 0.35 | 116.67 ± 4.71 |     13.10 ± 0.87 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-05 21:16:53 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
