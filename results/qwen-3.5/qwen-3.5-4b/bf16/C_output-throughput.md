# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-07 21:11:40
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-4b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------|-------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-4b-bf16 |  pp1024 (c1) | 10235.87 ± 195.35 | 10235.87 ± 195.35 |               |                  |   150.22 ± 0.66 |    90.17 ± 0.66 |   150.22 ± 0.66 |
| qwen3.5-4b-bf16 |  tg1024 (c1) |      20.77 ± 0.01 |      20.77 ± 0.01 |  22.00 ± 0.00 |     22.00 ± 0.00 |                 |                 |                 |
| qwen3.5-4b-bf16 |  pp1024 (c5) |   6620.58 ± 25.76 | 2604.37 ± 1136.92 |               |                  | 491.70 ± 168.80 | 431.64 ± 168.80 | 491.70 ± 168.80 |
| qwen3.5-4b-bf16 |  tg1024 (c5) |     120.26 ± 0.12 |      24.20 ± 0.08 | 125.00 ± 0.00 |     25.00 ± 0.00 |                 |                 |                 |
| qwen3.5-4b-bf16 | pp1024 (c10) |   6645.32 ± 56.98 | 1817.52 ± 1847.12 |               |                  | 870.97 ± 398.84 | 810.92 ± 398.84 | 870.97 ± 398.84 |
| qwen3.5-4b-bf16 | tg1024 (c10) |     222.49 ± 0.56 |      22.60 ± 0.17 | 240.00 ± 0.00 |     24.00 ± 0.00 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-07 21:04:38 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
