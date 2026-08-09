# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-07 21:11:12
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------|------------------:|------------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.5-9b-bf16 |  pp2048 @ d4 (c1) | 3744.49 ± 1173.55 | 3744.49 ± 1173.55 |               |                  |   673.77 ± 244.01 |   579.03 ± 244.01 |   673.77 ± 244.01 |
| qwen3.5-9b-bf16 |   tg512 @ d4 (c1) |      12.48 ± 0.02 |      12.48 ± 0.02 |  13.00 ± 0.00 |     13.00 ± 0.00 |                   |                   |                   |
| qwen3.5-9b-bf16 |  pp2048 @ d4 (c5) |   3783.90 ± 23.57 | 1876.64 ± 1337.68 |               |                  |  1555.29 ± 711.62 |  1460.55 ± 711.62 |  1555.29 ± 711.62 |
| qwen3.5-9b-bf16 |   tg512 @ d4 (c5) |      62.46 ± 0.21 |      12.88 ± 0.19 |  70.00 ± 0.00 |     14.00 ± 0.00 |                   |                   |                   |
| qwen3.5-9b-bf16 | pp2048 @ d4 (c10) |  3582.87 ± 222.57 | 1009.33 ± 1017.94 |               |                  | 3131.34 ± 1539.25 | 3036.60 ± 1539.25 | 3131.34 ± 1539.25 |
| qwen3.5-9b-bf16 |  tg512 @ d4 (c10) |     113.14 ± 0.10 |      12.07 ± 0.36 | 133.33 ± 4.71 |     13.57 ± 0.50 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-07 21:02:27 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
