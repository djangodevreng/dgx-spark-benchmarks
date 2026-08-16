# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-14 12:23:03
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |              test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |     e2e_ttft (ms) |
|:------------------|------------------:|------------------:|------------------:|---------------:|-----------------:|-----------------:|-----------------:|------------------:|
| gpt-oss-20b-mxfp4 |  pp2048 @ d4 (c1) |   9732.52 ± 88.42 |   9732.52 ± 88.42 |                |                  |    266.01 ± 4.25 |    192.60 ± 4.25 |     329.85 ± 4.23 |
| gpt-oss-20b-mxfp4 |   tg512 @ d4 (c1) |      46.07 ± 0.27 |      46.07 ± 0.27 |   47.00 ± 0.00 |     47.00 ± 0.00 |                  |                  |                   |
| gpt-oss-20b-mxfp4 |  pp2048 @ d4 (c5) | 3052.82 ± 3248.57 | 3341.56 ± 2298.12 |                |                  |  913.89 ± 312.10 |  771.69 ± 342.05 | 3719.33 ± 5179.09 |
| gpt-oss-20b-mxfp4 |   tg512 @ d4 (c5) |     86.15 ± 42.78 |      32.58 ± 4.73 | 104.33 ± 36.28 |    31.80 ± 11.59 |                  |                  |                   |
| gpt-oss-20b-mxfp4 | pp2048 @ d4 (c10) | 3222.05 ± 3332.08 | 2020.40 ± 2157.82 |                |                  | 1636.61 ± 659.67 | 1496.61 ± 670.12 | 7666.79 ± 8676.82 |
| gpt-oss-20b-mxfp4 |  tg512 @ d4 (c10) |    140.97 ± 52.06 |      24.98 ± 1.26 | 152.67 ± 57.60 |    19.14 ± 12.16 |                  |                  |                   |

llama-benchy (0.4.0)
date: 2026-08-14 12:19:41 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
