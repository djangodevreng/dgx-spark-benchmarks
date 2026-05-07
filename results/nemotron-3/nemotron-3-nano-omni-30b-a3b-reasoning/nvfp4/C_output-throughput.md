# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-03 09:58:35
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                          |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-------------------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-omni-30b-nvfp4 |  pp1024 (c1) | 2525.29 ± 1913.86 | 2525.29 ± 1913.86 |               |                  | 710.80 ± 360.67 | 624.93 ± 360.67 | 710.80 ± 360.67 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg1024 (c1) |      55.55 ± 0.06 |      55.55 ± 0.06 |  57.00 ± 0.00 |     57.00 ± 0.00 |                 |                 |                 |
| nemotron-3-nano-omni-30b-nvfp4 |  pp1024 (c5) |  5812.31 ± 550.91 |  1691.44 ± 956.01 |               |                  | 712.33 ± 160.99 | 626.46 ± 160.99 | 712.33 ± 160.99 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg1024 (c5) |    135.15 ± 11.80 |      30.97 ± 1.78 | 160.00 ± 4.08 |     36.47 ± 2.58 |                 |                 |                 |
| nemotron-3-nano-omni-30b-nvfp4 | pp1024 (c10) |  8675.28 ± 680.97 |  1242.39 ± 627.72 |               |                  | 949.70 ± 262.00 | 863.84 ± 262.00 | 949.70 ± 262.00 |
| nemotron-3-nano-omni-30b-nvfp4 | tg1024 (c10) |     201.92 ± 7.08 |      22.90 ± 1.67 | 252.67 ± 8.96 |     28.20 ± 1.80 |                 |                 |                 |

llama-benchy (0.3.7)
date: 2026-05-03 09:53:40 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
