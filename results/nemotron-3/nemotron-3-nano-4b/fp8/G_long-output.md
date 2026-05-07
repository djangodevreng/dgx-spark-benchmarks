# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-05 18:12:10
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                  |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-4b-fp8 |   pp256 (c1) | 8600.75 ± 4453.34 | 8600.75 ± 4453.34 |               |                  |  81.98 ± 16.26 |  36.00 ± 16.26 |   81.98 ± 16.26 |
| nemotron-3-nano-4b-fp8 |  tg4096 (c1) |      42.78 ± 0.04 |      42.78 ± 0.04 |  43.67 ± 0.47 |     43.67 ± 0.47 |                |                |                 |
| nemotron-3-nano-4b-fp8 |   pp256 (c5) |  6544.61 ± 786.40 |  1966.30 ± 545.91 |               |                  | 173.76 ± 34.22 | 127.78 ± 34.22 |  173.76 ± 34.22 |
| nemotron-3-nano-4b-fp8 |  tg4096 (c5) |    124.10 ± 28.28 |      41.11 ± 1.04 | 205.00 ± 0.00 |     43.47 ± 1.75 |                |                |                 |
| nemotron-3-nano-4b-fp8 |  pp256 (c10) |  8267.79 ± 675.23 |  1217.32 ± 547.41 |               |                  | 255.25 ± 50.83 | 209.28 ± 50.83 |  255.25 ± 50.83 |
| nemotron-3-nano-4b-fp8 | tg4096 (c10) |    214.49 ± 31.85 |      36.72 ± 1.21 | 360.00 ± 0.00 |     40.20 ± 3.16 |                |                |                 |

llama-benchy (0.3.7)
date: 2026-05-05 18:04:49 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
