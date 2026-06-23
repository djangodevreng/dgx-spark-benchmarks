# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-06-23 02:22:01
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c1) | 6472.41 ± 131.23 |  6472.41 ± 131.23 |               |                  |    213.68 ± 5.64 |    146.46 ± 5.64 |    213.68 ± 5.64 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c1) |     30.67 ± 0.02 |      30.67 ± 0.02 |  31.00 ± 0.00 |     31.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c5) |  6715.60 ± 85.78 |   1490.06 ± 42.68 |               |                  |   690.13 ± 13.58 |   622.91 ± 13.58 |   690.13 ± 13.58 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c5) |    107.97 ± 7.12 |      25.59 ± 0.54 | 133.33 ± 2.36 |     29.27 ± 2.11 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp1024 (c10) |  6829.17 ± 60.73 | 1262.02 ± 1325.33 |               |                  | 1138.26 ± 385.15 | 1071.04 ± 385.15 | 1138.26 ± 385.15 |
| gemma-4-26b-a4b-nvfp4 | tg1024 (c10) |   151.22 ± 15.96 |      21.59 ± 0.98 | 226.67 ± 4.71 |     25.93 ± 3.39 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-23 02:16:52 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
