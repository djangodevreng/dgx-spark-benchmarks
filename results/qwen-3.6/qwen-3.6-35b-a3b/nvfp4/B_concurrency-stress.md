# Run B — 25k context, c=5/10/20

**Generated:** 2026-06-26 07:05:38
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-nvfp4 |  pp25000 (c5) |  5549.77 ± 2.90 | 2449.59 ± 1458.54 |               |                  |  12409.13 ± 5672.74 |  12345.76 ± 5672.74 |  12411.37 ± 5673.13 |
| qwen3.6-35b-a3b-nvfp4 |    tg256 (c5) |    46.03 ± 0.15 |      14.50 ± 4.30 | 110.00 ± 0.00 |     26.80 ± 4.07 |                     |                     |                     |
| qwen3.6-35b-a3b-nvfp4 | pp25000 (c10) | 5021.90 ± 14.12 | 1518.31 ± 1295.79 |               |                  | 23927.28 ± 12915.48 | 23863.91 ± 12915.48 | 23928.72 ± 12916.20 |
| qwen3.6-35b-a3b-nvfp4 |   tg256 (c10) |    45.60 ± 0.13 |       8.43 ± 3.50 | 150.67 ± 0.94 |     21.83 ± 5.81 |                     |                     |                     |
| qwen3.6-35b-a3b-nvfp4 | pp25000 (c20) | 4106.53 ± 14.42 |  921.17 ± 1128.80 |               |                  | 51568.02 ± 32124.43 | 51504.66 ± 32124.43 | 51568.87 ± 32124.75 |
| qwen3.6-35b-a3b-nvfp4 |   tg256 (c20) |    41.20 ± 0.12 |       4.61 ± 2.95 | 219.67 ± 0.47 |     17.15 ± 6.37 |                     |                     |                     |

llama-benchy (0.3.8)
date: 2026-06-26 06:50:48 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
