# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-14 15:22:30
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.6-35b-a3b-fp8 |   pp256 (c1) | 2947.48 ± 238.05 | 2947.48 ± 238.05 |               |                  |   148.32 ± 7.79 |    79.23 ± 7.79 |   148.32 ± 7.79 |
| qwen3.6-35b-a3b-fp8 |  tg4096 (c1) |     51.93 ± 0.04 |     51.93 ± 0.04 |  53.67 ± 0.47 |     53.67 ± 0.47 |                 |                 |                 |
| qwen3.6-35b-a3b-fp8 |   pp256 (c5) | 2692.41 ± 211.03 |  743.12 ± 235.04 |               |                  |  415.31 ± 72.49 |  346.22 ± 72.49 |  415.31 ± 72.49 |
| qwen3.6-35b-a3b-fp8 |  tg4096 (c5) |    107.55 ± 2.99 |     24.24 ± 1.80 | 134.00 ± 1.41 |     34.73 ± 7.28 |                 |                 |                 |
| qwen3.6-35b-a3b-fp8 |  pp256 (c10) |  3108.55 ± 48.48 |  513.32 ± 462.02 |               |                  | 653.64 ± 145.64 | 584.55 ± 145.64 | 653.64 ± 145.64 |
| qwen3.6-35b-a3b-fp8 | tg4096 (c10) |    136.47 ± 2.78 |     17.89 ± 2.12 | 193.33 ± 4.71 |     26.13 ± 5.29 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-14 14:54:38 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
