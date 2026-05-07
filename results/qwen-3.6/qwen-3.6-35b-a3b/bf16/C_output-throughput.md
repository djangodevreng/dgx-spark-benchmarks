# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-05 11:54:43
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-bf16 |  pp1024 (c1) | 3579.07 ± 78.02 |  3579.07 ± 78.02 |               |                  |    367.39 ± 7.78 |    255.08 ± 7.78 |    367.39 ± 7.78 |
| qwen3.6-35b-a3b-bf16 |  tg1024 (c1) |    30.38 ± 0.02 |     30.38 ± 0.02 |  31.00 ± 0.00 |     31.00 ± 0.00 |                  |                  |                  |
| qwen3.6-35b-a3b-bf16 |  pp1024 (c5) | 3287.62 ± 20.60 | 1071.95 ± 388.93 |               |                  | 1082.46 ± 286.18 |  970.15 ± 286.18 | 1082.46 ± 286.18 |
| qwen3.6-35b-a3b-bf16 |  tg1024 (c5) |    62.02 ± 0.98 |     12.57 ± 0.41 |  75.33 ± 0.47 |     16.07 ± 1.77 |                  |                  |                  |
| qwen3.6-35b-a3b-bf16 | pp1024 (c10) | 3500.18 ± 18.09 |  706.20 ± 398.91 |               |                  | 1784.57 ± 687.73 | 1672.26 ± 687.73 | 1784.57 ± 687.73 |
| qwen3.6-35b-a3b-bf16 | tg1024 (c10) |    82.80 ± 0.56 |      8.36 ± 0.07 | 110.00 ± 0.00 |     11.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-05 11:42:36 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
