# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-05 03:48:26
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |              test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|------------------:|----------------:|----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-super |  pp2048 @ d4 (c1) | 1721.64 ± 21.43 | 1721.64 ± 21.43 |               |                  |    1304.67 ± 8.24 |    1097.70 ± 8.24 |    1304.67 ± 8.24 |
| nemotron-3-super |   tg512 @ d4 (c1) |    22.10 ± 0.38 |    22.10 ± 0.38 |  30.67 ± 0.94 |     30.67 ± 0.94 |                   |                   |                   |
| nemotron-3-super |  pp2048 @ d4 (c5) | 1550.11 ± 14.75 | 479.99 ± 185.09 |               |                  | 4577.66 ± 1326.73 | 4370.69 ± 1326.73 | 4577.66 ± 1326.73 |
| nemotron-3-super |   tg512 @ d4 (c5) |    48.29 ± 1.42 |    11.23 ± 0.56 |  76.67 ± 6.34 |     20.00 ± 3.01 |                   |                   |                   |
| nemotron-3-super | pp2048 @ d4 (c10) | 1566.37 ± 12.78 | 323.15 ± 207.77 |               |                  | 7781.63 ± 3219.41 | 7574.67 ± 3219.41 | 7781.63 ± 3219.41 |
| nemotron-3-super |  tg512 @ d4 (c10) |    69.24 ± 0.60 |     7.81 ± 0.37 | 108.33 ± 4.03 |     14.60 ± 1.58 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-05 03:40:47 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
