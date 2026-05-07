# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-03 13:30:52
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                         |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:------------------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-omni-30b-bf16 |  pp25000 (c5) |  6463.44 ± 9.11 | 2766.29 ± 1700.03 |               |                  |  11008.59 ± 4839.64 |  10860.70 ± 4839.64 |  11009.45 ± 4839.51 |
| nemotron-3-nano-omni-30b-bf16 |    tg256 (c5) |    34.40 ± 0.11 |       9.06 ± 1.80 |  62.67 ± 3.77 |     14.67 ± 2.52 |                     |                     |                     |
| nemotron-3-nano-omni-30b-bf16 | pp25000 (c10) | 6435.99 ± 11.71 | 1786.12 ± 1537.76 |               |                  |  19749.55 ± 9908.51 |  19601.66 ± 9908.51 |  19749.92 ± 9908.51 |
| nemotron-3-nano-omni-30b-bf16 |   tg256 (c10) |    38.32 ± 0.21 |       5.65 ± 1.34 |  85.67 ± 4.03 |     11.67 ± 3.01 |                     |                     |                     |
| nemotron-3-nano-omni-30b-bf16 | pp25000 (c20) | 6236.93 ± 15.19 | 1080.26 ± 1231.39 |               |                  | 37884.18 ± 20624.64 | 37736.29 ± 20624.64 | 37885.03 ± 20624.79 |
| nemotron-3-nano-omni-30b-bf16 |   tg256 (c20) |    44.20 ± 0.90 |       3.70 ± 1.17 | 140.00 ± 0.00 |      9.23 ± 2.68 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-03 13:19:53 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
