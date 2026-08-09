# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-07 21:02:26
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-9b-bf16 |   pp256 (c1) | 7066.45 ± 541.99 |  7066.45 ± 541.99 |               |                  |   127.43 ± 2.58 |    34.07 ± 2.58 |   127.43 ± 2.58 |
| qwen3.5-9b-bf16 |  tg4096 (c1) |     12.47 ± 0.01 |      12.47 ± 0.01 |  13.00 ± 0.00 |     13.00 ± 0.00 |                 |                 |                 |
| qwen3.5-9b-bf16 |   pp256 (c5) |  2856.08 ± 82.14 | 1794.75 ± 2118.18 |               |                  | 364.59 ± 115.77 | 271.22 ± 115.77 | 364.59 ± 115.77 |
| qwen3.5-9b-bf16 |  tg4096 (c5) |     63.48 ± 3.04 |      13.14 ± 0.01 |  70.00 ± 0.00 |     14.27 ± 0.44 |                 |                 |                 |
| qwen3.5-9b-bf16 |  pp256 (c10) |  3016.74 ± 41.64 |  894.29 ± 1503.89 |               |                  | 636.81 ± 169.15 | 543.45 ± 169.15 | 636.81 ± 169.15 |
| qwen3.5-9b-bf16 | tg4096 (c10) |    123.09 ± 1.77 |      12.55 ± 0.02 | 146.67 ± 4.71 |     14.67 ± 0.47 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 19:57:46 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
