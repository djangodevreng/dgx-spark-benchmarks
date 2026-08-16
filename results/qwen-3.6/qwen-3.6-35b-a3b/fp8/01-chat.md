# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-14 14:43:30
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-fp8 |  pp1024 (c1) | 4453.68 ± 91.47 |  4453.68 ± 91.47 |               |                  |    291.26 ± 4.55 |    221.01 ± 4.55 |    291.26 ± 4.55 |
| qwen3.6-35b-a3b-fp8 |  tg1024 (c1) |    51.86 ± 0.18 |     51.86 ± 0.18 |  53.67 ± 0.94 |     53.67 ± 0.94 |                  |                  |                  |
| qwen3.6-35b-a3b-fp8 |  pp1024 (c5) | 3682.23 ± 48.40 | 1107.38 ± 451.38 |               |                  | 1027.97 ± 274.16 |  957.72 ± 274.16 | 1027.97 ± 274.16 |
| qwen3.6-35b-a3b-fp8 |  tg1024 (c5) |   109.52 ± 0.76 |     22.15 ± 0.19 | 133.33 ± 2.36 |     26.67 ± 0.47 |                  |                  |                  |
| qwen3.6-35b-a3b-fp8 | pp1024 (c10) |  3849.13 ± 9.63 |  772.31 ± 524.37 |               |                  | 1652.46 ± 621.05 | 1582.22 ± 621.05 | 1652.46 ± 621.05 |
| qwen3.6-35b-a3b-fp8 | tg1024 (c10) |   150.15 ± 1.23 |     15.29 ± 0.18 | 193.33 ± 4.71 |     19.33 ± 0.47 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-14 14:34:20 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
