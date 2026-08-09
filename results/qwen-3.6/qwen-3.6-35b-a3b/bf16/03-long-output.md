# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-08 12:58:27
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |         test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:---------------------|-------------:|-----------------:|----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.6-35b-a3b-bf16 |   pp256 (c1) |  1688.29 ± 26.47 | 1688.29 ± 26.47 |               |                  |   247.31 ± 7.17 |   139.30 ± 7.17 |   247.31 ± 7.17 |
| qwen3.6-35b-a3b-bf16 |  tg4096 (c1) |     30.35 ± 0.02 |    30.35 ± 0.02 |  31.33 ± 0.47 |     31.33 ± 0.47 |                 |                 |                 |
| qwen3.6-35b-a3b-bf16 |   pp256 (c5) | 1774.95 ± 209.13 | 486.24 ± 158.43 |               |                  | 629.09 ± 125.58 | 521.08 ± 125.58 | 629.09 ± 125.58 |
| qwen3.6-35b-a3b-bf16 |  tg4096 (c5) |     61.35 ± 2.47 |    14.26 ± 1.44 |  80.00 ± 0.00 |     21.00 ± 4.44 |                 |                 |                 |
| qwen3.6-35b-a3b-bf16 |  pp256 (c10) | 2460.53 ± 104.06 |  339.63 ± 94.41 |               |                  | 843.99 ± 138.05 | 735.97 ± 138.05 | 843.99 ± 138.05 |
| qwen3.6-35b-a3b-bf16 | tg4096 (c10) |     79.15 ± 2.16 |     9.97 ± 1.19 | 123.33 ± 4.71 |     16.60 ± 4.81 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-08 12:12:14 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
