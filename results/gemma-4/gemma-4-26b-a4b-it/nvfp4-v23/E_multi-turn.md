# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-06-23 02:26:24
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c1) | 6679.97 ± 194.56 | 6679.97 ± 194.56 |               |                  |   348.21 ± 17.22 |   283.34 ± 17.22 |   348.21 ± 17.22 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c1) |     30.55 ± 0.01 |     30.55 ± 0.01 |  31.00 ± 0.00 |     31.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp2048 @ d4 (c5) |  6423.83 ± 20.30 | 1880.23 ± 696.60 |               |                  | 1161.57 ± 302.25 | 1096.69 ± 302.25 | 1161.57 ± 302.25 |
| gemma-4-26b-a4b-nvfp4 |   tg512 @ d4 (c5) |    115.65 ± 1.62 |     24.55 ± 0.50 | 130.00 ± 0.00 |     26.93 ± 1.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp2048 @ d4 (c10) |   6575.72 ± 8.39 | 1211.53 ± 614.11 |               |                  | 1966.10 ± 735.30 | 1901.23 ± 735.30 | 1966.10 ± 735.30 |
| gemma-4-26b-a4b-nvfp4 |  tg512 @ d4 (c10) |    182.90 ± 6.67 |     20.01 ± 0.80 | 220.00 ± 0.00 |     23.47 ± 1.96 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-23 02:22:01 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
