# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-10-18 14:54:23
**Profile:** nvfp4-b12x
**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.8-flash-next --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model              |         test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------|-------------:|-----------------:|----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.8-flash-next |   pp256 (c1) |  1221.04 ± 90.03 | 1221.04 ± 90.03 |               |                  |    367.25 ± 3.48 |    185.24 ± 3.48 |    367.25 ± 3.48 |
| qwen3.8-flash-next |  tg4096 (c1) |     34.57 ± 1.72 |    34.57 ± 1.72 |  64.67 ± 1.25 |     64.67 ± 1.25 |                  |                  |                  |
| qwen3.8-flash-next |   pp256 (c5) | 1245.01 ± 133.85 |  327.99 ± 53.35 |               |                  |  866.23 ± 101.10 |  684.22 ± 101.10 |  866.28 ± 101.08 |
| qwen3.8-flash-next |  tg4096 (c5) |     69.60 ± 1.35 |    17.80 ± 1.84 | 122.67 ± 4.99 |     36.60 ± 4.94 |                  |                  |                  |
| qwen3.8-flash-next |  pp256 (c10) | 1654.79 ± 179.05 |  200.32 ± 25.79 |               |                  | 1304.54 ± 127.57 | 1122.53 ± 127.57 | 1304.61 ± 127.58 |
| qwen3.8-flash-next | tg4096 (c10) |     98.21 ± 4.93 |    12.74 ± 0.95 | 172.33 ± 4.64 |     27.80 ± 5.68 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-10-18 14:09:59 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
