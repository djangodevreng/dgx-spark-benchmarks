# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-04 21:32:11
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-fp8 |  pp1024 (c1) | 5647.20 ± 195.14 | 5647.20 ± 195.14 |               |                  |    226.44 ± 8.60 |    155.95 ± 8.60 |    226.44 ± 8.60 |
| qwen3.6-35b-a3b-fp8 |  tg1024 (c1) |     52.22 ± 0.13 |     52.22 ± 0.13 |  53.00 ± 0.00 |     53.00 ± 0.00 |                  |                  |                  |
| qwen3.6-35b-a3b-fp8 |  pp1024 (c5) |  5094.32 ± 40.83 | 1555.17 ± 405.37 |               |                  |  705.51 ± 155.26 |  635.02 ± 155.26 |  705.51 ± 155.26 |
| qwen3.6-35b-a3b-fp8 |  tg1024 (c5) |    100.36 ± 0.77 |     20.15 ± 0.16 | 115.00 ± 4.08 |     23.00 ± 0.82 |                  |                  |                  |
| qwen3.6-35b-a3b-fp8 | pp1024 (c10) |  5306.93 ± 17.75 |  997.44 ± 506.50 |               |                  | 1210.21 ± 440.01 | 1139.72 ± 440.01 | 1210.21 ± 440.01 |
| qwen3.6-35b-a3b-fp8 | tg1024 (c10) |    147.62 ± 0.96 |     14.92 ± 0.13 | 186.67 ± 4.71 |     18.67 ± 0.47 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-04 21:25:04 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
