# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-05 17:09:32
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                  |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-nano-4b-fp8 |  pp8192 (c5) | 10907.93 ± 70.91 | 4599.60 ± 2645.63 |               |                  |  2121.89 ± 909.66 |  2077.33 ± 909.66 |  2121.89 ± 909.66 |
| nemotron-3-nano-4b-fp8 |   tg512 (c5) |    160.19 ± 0.44 |      35.50 ± 1.95 | 195.00 ± 0.00 |     39.33 ± 0.47 |                   |                   |                   |
| nemotron-3-nano-4b-fp8 | pp8192 (c10) | 10779.74 ± 54.10 | 2925.02 ± 2372.20 |               |                  | 3855.19 ± 1918.20 | 3810.64 ± 1918.20 | 3855.19 ± 1918.20 |
| nemotron-3-nano-4b-fp8 |  tg512 (c10) |    234.34 ± 0.85 |      28.11 ± 2.56 | 330.00 ± 0.00 |     34.70 ± 1.73 |                   |                   |                   |
| nemotron-3-nano-4b-fp8 | pp8192 (c20) | 10510.49 ± 36.85 | 1785.41 ± 1942.95 |               |                  | 7401.67 ± 4022.21 | 7357.12 ± 4022.21 | 7401.67 ± 4022.21 |
| nemotron-3-nano-4b-fp8 |  tg512 (c20) |    295.81 ± 1.60 |      19.58 ± 2.68 | 486.33 ± 8.96 |     29.53 ± 4.25 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-05 17:05:48 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
