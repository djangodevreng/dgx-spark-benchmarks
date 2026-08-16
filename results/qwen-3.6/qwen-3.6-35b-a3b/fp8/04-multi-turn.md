# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-14 15:27:22
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:--------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-35b-a3b-fp8 |  pp2048 @ d4 (c1) |  4534.32 ± 80.60 |  4534.32 ± 80.60 |               |                  |    492.96 ± 15.82 |    428.97 ± 15.82 |    492.96 ± 15.82 |
| qwen3.6-35b-a3b-fp8 |   tg512 @ d4 (c1) |     52.01 ± 0.49 |     52.01 ± 0.49 |  53.00 ± 0.00 |     53.00 ± 0.00 |                   |                   |                   |
| qwen3.6-35b-a3b-fp8 |  pp2048 @ d4 (c5) |   4064.93 ± 7.82 | 1573.67 ± 861.87 |               |                  |  1578.57 ± 613.56 |  1514.58 ± 613.56 |  1578.57 ± 613.56 |
| qwen3.6-35b-a3b-fp8 |   tg512 @ d4 (c5) |    105.94 ± 1.62 |     22.10 ± 0.65 | 126.67 ± 2.36 |     25.33 ± 0.47 |                   |                   |                   |
| qwen3.6-35b-a3b-fp8 | pp2048 @ d4 (c10) | 3860.95 ± 140.66 |  938.38 ± 750.29 |               |                  | 2995.44 ± 1388.08 | 2931.45 ± 1388.08 | 2995.44 ± 1388.08 |
| qwen3.6-35b-a3b-fp8 |  tg512 @ d4 (c10) |    140.72 ± 2.10 |     15.09 ± 0.60 | 180.00 ± 0.00 |     18.30 ± 0.59 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-14 15:22:30 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
