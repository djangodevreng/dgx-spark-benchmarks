# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-06 16:59:55
**Profile:** bf16
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model       |              test |     t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------|------------------:|----------------:|----------------:|-------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gemma-4-31b |  pp2048 @ d4 (c1) |  1086.33 ± 4.08 |  1086.33 ± 4.08 |              |                  |     2110.71 ± 0.35 |     1733.97 ± 0.35 |     2110.71 ± 0.35 |
| gemma-4-31b |   tg512 @ d4 (c1) |     3.71 ± 0.00 |     3.71 ± 0.00 |  4.00 ± 0.00 |      4.00 ± 0.00 |                    |                    |                    |
| gemma-4-31b |  pp2048 @ d4 (c5) | 1054.02 ± 28.77 | 306.53 ± 250.02 |              |                  |  7720.84 ± 1644.92 |  7344.09 ± 1644.92 |  7720.84 ± 1644.92 |
| gemma-4-31b |   tg512 @ d4 (c5) |    12.19 ± 0.40 |     3.47 ± 0.06 | 20.00 ± 0.00 |      4.00 ± 0.00 |                    |                    |                    |
| gemma-4-31b | pp2048 @ d4 (c10) |  1066.72 ± 6.22 | 270.49 ± 331.11 |              |                  | 12126.50 ± 5058.30 | 11749.76 ± 5058.30 | 12126.50 ± 5058.30 |
| gemma-4-31b |  tg512 @ d4 (c10) |    21.74 ± 2.48 |     3.21 ± 0.19 | 40.00 ± 0.00 |      4.00 ± 0.00 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-06 16:31:18 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
