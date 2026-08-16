# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-14 07:41:57
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|------------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-nvfp4 |  pp2048 @ d4 (c1) |  6516.09 ± 25.19 |   6516.09 ± 25.19 |               |                  |    345.70 ± 7.82 |    288.29 ± 7.82 |    345.70 ± 7.82 |
| qwen3.6-35b-a3b-nvfp4 |   tg512 @ d4 (c1) |     42.48 ± 0.42 |      42.48 ± 0.42 |  43.00 ± 0.00 |     43.00 ± 0.00 |                  |                  |                  |
| qwen3.6-35b-a3b-nvfp4 |  pp2048 @ d4 (c5) |  5595.87 ± 34.59 | 2183.04 ± 1202.46 |               |                  | 1133.67 ± 436.76 | 1076.26 ± 436.76 | 1133.67 ± 436.76 |
| qwen3.6-35b-a3b-nvfp4 |   tg512 @ d4 (c5) |    130.00 ± 0.36 |      26.99 ± 0.57 | 151.67 ± 2.36 |     30.33 ± 0.47 |                  |                  |                  |
| qwen3.6-35b-a3b-nvfp4 | pp2048 @ d4 (c10) | 5351.18 ± 351.23 |  1244.47 ± 975.12 |               |                  | 2208.08 ± 998.10 | 2150.68 ± 998.10 | 2208.08 ± 998.10 |
| qwen3.6-35b-a3b-nvfp4 |  tg512 @ d4 (c10) |    183.61 ± 0.90 |      19.58 ± 0.66 | 230.00 ± 0.00 |     23.03 ± 0.18 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-14 07:37:49 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
