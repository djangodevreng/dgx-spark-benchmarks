# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-03 10:01:14
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                          |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------------------|------------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-nvfp4 |  pp2048 @ d4 (c1) |  3666.20 ± 590.37 |  3666.20 ± 590.37 |               |                  |  595.67 ± 107.28 |  523.61 ± 107.28 |  595.67 ± 107.28 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg512 @ d4 (c1) |      56.18 ± 0.29 |      56.18 ± 0.29 |  62.33 ± 2.62 |     62.33 ± 2.62 |                  |                  |                  |
| nemotron-3-nano-omni-30b-nvfp4 |  pp2048 @ d4 (c5) |  8341.79 ± 781.53 | 2261.26 ± 1030.67 |               |                  | 1031.74 ± 264.02 |  959.69 ± 264.02 | 1031.74 ± 264.02 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg512 @ d4 (c5) |     128.86 ± 8.39 |      30.55 ± 2.00 | 168.33 ± 8.50 |     36.67 ± 4.53 |                  |                  |                  |
| nemotron-3-nano-omni-30b-nvfp4 | pp2048 @ d4 (c10) | 10129.85 ± 204.98 | 1886.17 ± 1331.85 |               |                  | 1358.61 ± 484.84 | 1286.55 ± 484.84 | 1358.61 ± 484.84 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg512 @ d4 (c10) |     193.48 ± 2.75 |      21.58 ± 0.81 | 246.33 ± 8.96 |     27.80 ± 1.70 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-03 09:58:37 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
