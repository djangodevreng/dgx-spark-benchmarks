# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-07 19:43:32
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.5-9b-bf16 |  pp1024 (c1) | 1651.31 ± 293.96 |  1651.31 ± 293.96 |               |                  |   685.63 ± 87.27 |   569.24 ± 87.27 |   685.63 ± 87.27 |
| qwen3.5-9b-bf16 |  tg1024 (c1) |     12.42 ± 0.07 |      12.42 ± 0.07 |  15.33 ± 1.25 |     15.33 ± 1.25 |                  |                  |                  |
| qwen3.5-9b-bf16 |  pp1024 (c5) | 3198.25 ± 167.33 | 1421.47 ± 1059.49 |               |                  | 1022.04 ± 378.95 |  905.65 ± 378.95 | 1022.04 ± 378.95 |
| qwen3.5-9b-bf16 |  tg1024 (c5) |     64.89 ± 0.28 |      13.10 ± 0.07 |  71.67 ± 2.36 |     14.33 ± 0.47 |                  |                  |                  |
| qwen3.5-9b-bf16 | pp1024 (c10) | 3180.06 ± 426.10 |  986.50 ± 1129.68 |               |                  | 1823.15 ± 923.89 | 1706.76 ± 923.89 | 1823.15 ± 923.89 |
| qwen3.5-9b-bf16 | tg1024 (c10) |    122.57 ± 0.67 |      12.51 ± 0.13 | 140.00 ± 0.00 |     14.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-07 19:26:52 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
