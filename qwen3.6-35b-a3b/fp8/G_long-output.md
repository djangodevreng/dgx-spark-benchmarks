# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-04 22:05:22
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.6-35b-a3b-fp8 |   pp256 (c1) | 2670.76 ± 724.70 | 2670.76 ± 724.70 |               |                  | 160.26 ± 25.15 |  96.01 ± 25.15 |  160.26 ± 25.15 |
| qwen3.6-35b-a3b-fp8 |  tg4096 (c1) |     52.01 ± 0.08 |     52.01 ± 0.08 |  53.33 ± 0.47 |     53.33 ± 0.47 |                |                |                 |
| qwen3.6-35b-a3b-fp8 |   pp256 (c5) |  2733.88 ± 92.47 |   692.55 ± 99.79 |               |                  | 406.64 ± 44.70 | 342.39 ± 44.70 |  406.64 ± 44.70 |
| qwen3.6-35b-a3b-fp8 |  tg4096 (c5) |     95.94 ± 2.55 |     23.18 ± 2.62 | 126.67 ± 2.36 |     36.40 ± 9.84 |                |                |                 |
| qwen3.6-35b-a3b-fp8 |  pp256 (c10) | 3927.76 ± 276.45 |  533.43 ± 151.89 |               |                  | 534.25 ± 85.81 | 470.00 ± 85.81 |  534.25 ± 85.81 |
| qwen3.6-35b-a3b-fp8 | tg4096 (c10) |    127.93 ± 1.37 |     16.83 ± 1.97 | 196.67 ± 4.71 |     24.40 ± 5.09 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-04 21:43:45 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
