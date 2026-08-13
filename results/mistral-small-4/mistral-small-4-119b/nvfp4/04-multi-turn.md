# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-13 10:38:22
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model mistral-small-4-119b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                      |              test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------------|------------------:|----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| mistral-small-4-119b-nvfp4 |  pp2048 @ d4 (c1) | 3831.56 ± 32.21 |  3831.56 ± 32.21 |               |                  |    597.26 ± 7.96 |    482.51 ± 7.96 |    597.26 ± 7.96 |
| mistral-small-4-119b-nvfp4 |   tg512 @ d4 (c1) |    30.60 ± 0.01 |     30.60 ± 0.01 |  31.00 ± 0.00 |     31.00 ± 0.00 |                  |                  |                  |
| mistral-small-4-119b-nvfp4 |  pp2048 @ d4 (c5) | 4181.27 ± 38.98 | 1090.43 ± 356.00 |               |                  | 1957.66 ± 434.28 | 1842.91 ± 434.28 | 1957.66 ± 434.28 |
| mistral-small-4-119b-nvfp4 |   tg512 @ d4 (c5) |    67.81 ± 2.11 |     16.85 ± 1.35 |  79.33 ± 0.94 |     18.60 ± 1.54 |                  |                  |                  |
| mistral-small-4-119b-nvfp4 | pp2048 @ d4 (c10) | 4103.21 ± 11.61 |  656.83 ± 410.46 |               |                  | 3512.47 ± 979.25 | 3397.72 ± 979.25 | 3512.47 ± 979.25 |
| mistral-small-4-119b-nvfp4 |  tg512 @ d4 (c10) |    88.73 ± 1.12 |      9.96 ± 0.43 | 110.00 ± 0.00 |     11.97 ± 0.91 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-13 10:31:33 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
