# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-10-18 13:52:43
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-flash-next --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model              |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.8-flash-next |  pp1024 (c1) | 2089.84 ± 92.98 | 2089.84 ± 92.98 |               |                  |   622.57 ± 29.24 |   435.61 ± 29.24 |   622.64 ± 29.22 |
| qwen3.8-flash-next |  tg1024 (c1) |    37.07 ± 5.74 |    37.07 ± 5.74 |  57.00 ± 9.90 |     57.00 ± 9.90 |                  |                  |                  |
| qwen3.8-flash-next |  pp1024 (c5) | 2039.50 ± 13.70 |  470.60 ± 32.97 |               |                  | 2167.09 ± 129.58 | 1980.13 ± 129.58 | 2167.23 ± 129.61 |
| qwen3.8-flash-next |  tg1024 (c5) |    80.26 ± 4.79 |    16.91 ± 1.16 | 115.33 ± 4.50 |     32.20 ± 3.92 |                  |                  |                  |
| qwen3.8-flash-next | pp1024 (c10) | 2104.26 ± 38.83 |  275.07 ± 77.63 |               |                  | 3805.48 ± 697.41 | 3618.52 ± 697.41 | 3805.48 ± 697.41 |
| qwen3.8-flash-next | tg1024 (c10) |   118.62 ± 1.05 |    13.04 ± 1.06 | 167.67 ± 9.10 |     25.03 ± 5.82 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-10-18 13:40:23 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
