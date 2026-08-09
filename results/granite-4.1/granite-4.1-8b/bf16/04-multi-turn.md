# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-09 07:16:40
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model granite-4-1-8b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:--------------------|------------------:|----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| granite-4-1-8b-bf16 |  pp2048 @ d4 (c1) | 4608.98 ± 57.91 |   4608.98 ± 57.91 |               |                  |    509.04 ± 11.44 |    396.91 ± 11.44 |    509.04 ± 11.44 |
| granite-4-1-8b-bf16 |   tg512 @ d4 (c1) |    12.52 ± 0.00 |      12.52 ± 0.00 |  13.00 ± 0.00 |     13.00 ± 0.00 |                   |                   |                   |
| granite-4-1-8b-bf16 |  pp2048 @ d4 (c5) | 4145.10 ± 16.67 | 1583.71 ± 1418.19 |               |                  |  1857.88 ± 668.66 |  1745.76 ± 668.66 |  1857.88 ± 668.66 |
| granite-4-1-8b-bf16 |   tg512 @ d4 (c5) |    52.06 ± 0.70 |      12.61 ± 0.23 |  65.00 ± 0.00 |     13.00 ± 0.00 |                   |                   |                   |
| granite-4-1-8b-bf16 | pp2048 @ d4 (c10) | 4236.98 ± 81.26 |  980.42 ± 1157.94 |               |                  | 3157.98 ± 1245.43 | 3045.85 ± 1245.43 | 3157.98 ± 1245.43 |
| granite-4-1-8b-bf16 |  tg512 @ d4 (c10) |    99.94 ± 3.96 |      11.86 ± 0.34 | 130.00 ± 0.00 |     13.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-09 07:07:58 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
