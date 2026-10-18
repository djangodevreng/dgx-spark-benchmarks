# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-10-17 22:35:01
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3.5-super --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model              |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3.5-super |  pp2048 @ d4 (c1) | 3095.10 ± 176.84 | 3095.10 ± 176.84 |               |                  |    781.63 ± 32.03 |    585.80 ± 32.03 |    782.07 ± 32.35 |
| nemotron-3.5-super |   tg512 @ d4 (c1) |     34.90 ± 2.34 |     34.90 ± 2.34 |  44.33 ± 2.05 |     44.33 ± 2.05 |                   |                   |                   |
| nemotron-3.5-super |  pp2048 @ d4 (c5) |  2326.05 ± 16.87 |  878.21 ± 464.53 |               |                  | 2816.23 ± 1003.71 | 2620.40 ± 1003.71 | 2816.43 ± 1003.58 |
| nemotron-3.5-super |   tg512 @ d4 (c5) |     72.76 ± 0.31 |     15.87 ± 0.55 | 105.67 ± 1.25 |     25.20 ± 3.51 |                   |                   |                   |
| nemotron-3.5-super | pp2048 @ d4 (c10) |   2316.12 ± 7.90 |  575.41 ± 453.56 |               |                  | 4972.42 ± 2284.71 | 4776.59 ± 2284.71 | 4972.71 ± 2284.53 |
| nemotron-3.5-super |  tg512 @ d4 (c10) |    102.46 ± 1.31 |     11.71 ± 0.63 | 165.67 ± 2.05 |     19.03 ± 1.99 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-10-17 22:28:07 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
