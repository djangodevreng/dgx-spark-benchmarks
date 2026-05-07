# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-05 03:16:00
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|-------------:|----------------:|----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-super |  pp1024 (c1) | 1441.68 ± 11.97 | 1441.68 ± 11.97 |               |                  |    861.61 ± 27.36 |    663.82 ± 27.36 |    861.61 ± 27.36 |
| nemotron-3-super |  tg1024 (c1) |    23.54 ± 1.35 |    23.54 ± 1.35 |  33.33 ± 1.25 |     33.33 ± 1.25 |                   |                   |                   |
| nemotron-3-super |  pp1024 (c5) | 1385.08 ± 28.71 |  343.24 ± 43.21 |               |                  |  2885.33 ± 341.39 |  2687.53 ± 341.39 |  2885.33 ± 341.39 |
| nemotron-3-super |  tg1024 (c5) |    50.56 ± 0.82 |    11.77 ± 0.53 |  73.00 ± 1.41 |     20.93 ± 3.17 |                   |                   |                   |
| nemotron-3-super | pp1024 (c10) |  1518.93 ± 6.80 |  237.80 ± 95.41 |               |                  | 4602.79 ± 1344.37 | 4404.99 ± 1344.37 | 4602.79 ± 1344.37 |
| nemotron-3-super | tg1024 (c10) |    74.55 ± 1.91 |     8.18 ± 0.34 | 116.00 ± 4.97 |     15.53 ± 2.91 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-05 03:02:36 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
