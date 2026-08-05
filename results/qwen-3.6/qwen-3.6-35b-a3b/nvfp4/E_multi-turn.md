# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-06-26 07:30:32
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|------------------:|----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-nvfp4 |  pp2048 @ d4 (c1) | 7674.62 ± 56.66 |   7674.62 ± 56.66 |               |                  |    315.29 ± 7.09 |    251.21 ± 7.09 |    315.29 ± 7.09 |
| qwen3.6-35b-a3b-nvfp4 |   tg512 @ d4 (c1) |    40.48 ± 0.14 |      40.48 ± 0.14 |  41.00 ± 0.00 |     41.00 ± 0.00 |                  |                  |                  |
| qwen3.6-35b-a3b-nvfp4 |  pp2048 @ d4 (c5) | 6418.53 ± 38.77 | 2313.64 ± 1148.41 |               |                  | 1025.62 ± 352.33 |  961.53 ± 352.33 | 1025.62 ± 352.33 |
| qwen3.6-35b-a3b-nvfp4 |   tg512 @ d4 (c5) |   121.05 ± 0.23 |      24.92 ± 0.38 | 136.33 ± 1.89 |     27.33 ± 0.47 |                  |                  |                  |
| qwen3.6-35b-a3b-nvfp4 | pp2048 @ d4 (c10) | 6270.72 ± 25.01 | 1492.94 ± 1090.79 |               |                  | 1852.20 ± 832.82 | 1788.12 ± 832.82 | 1852.20 ± 832.82 |
| qwen3.6-35b-a3b-nvfp4 |  tg512 @ d4 (c10) |   174.88 ± 1.05 |      18.44 ± 0.50 | 210.00 ± 0.00 |     21.17 ± 0.37 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-26 07:26:11 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
