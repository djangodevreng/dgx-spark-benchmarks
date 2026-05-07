# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-03 11:30:43
**Profile:** fp8
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-omni-30b-fp8 |  pp1024 (c1) | 6333.19 ± 432.13 | 6333.19 ± 432.13 |               |                  |   226.40 ± 3.46 |   144.68 ± 3.46 |   226.40 ± 3.46 |
| nemotron-3-nano-omni-30b-fp8 |  tg1024 (c1) |     49.85 ± 0.27 |     49.85 ± 0.27 |  51.00 ± 0.00 |     51.00 ± 0.00 |                 |                 |                 |
| nemotron-3-nano-omni-30b-fp8 |  pp1024 (c5) |  6740.78 ± 64.24 | 2191.75 ± 784.03 |               |                  | 555.81 ± 154.04 | 474.09 ± 154.04 | 555.81 ± 154.04 |
| nemotron-3-nano-omni-30b-fp8 |  tg1024 (c5) |    102.07 ± 3.11 |     21.32 ± 2.13 | 117.00 ± 2.16 |     24.93 ± 2.49 |                 |                 |                 |
| nemotron-3-nano-omni-30b-fp8 | pp1024 (c10) |  8213.69 ± 41.53 | 1180.13 ± 518.25 |               |                  | 964.67 ± 228.85 | 882.95 ± 228.85 | 964.67 ± 228.85 |
| nemotron-3-nano-omni-30b-fp8 | tg1024 (c10) |    138.12 ± 3.79 |     15.26 ± 0.74 | 180.00 ± 0.00 |     20.13 ± 1.15 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-03 11:24:08 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
