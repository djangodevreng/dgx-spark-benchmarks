# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-06 10:41:05
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c1) | 7282.94 ± 448.83 | 7282.94 ± 448.83 |               |                  |   194.34 ± 12.66 |   127.97 ± 12.66 |   194.34 ± 12.66 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c1) |     29.45 ± 0.08 |     29.45 ± 0.08 |  30.00 ± 0.00 |     30.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c5) |  6801.70 ± 34.14 |  1508.87 ± 53.25 |               |                  |    681.32 ± 7.44 |    614.96 ± 7.44 |    681.32 ± 7.44 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c5) |    94.40 ± 12.33 |     24.69 ± 0.85 | 130.00 ± 0.00 |     28.47 ± 2.28 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp1024 (c10) |  7014.21 ± 30.74 | 1082.26 ± 703.88 |               |                  | 1098.61 ± 307.66 | 1032.25 ± 307.66 | 1098.61 ± 307.66 |
| gemma-4-26b-a4b-nvfp4 | tg1024 (c10) |   146.33 ± 16.88 |     20.88 ± 1.10 | 220.00 ± 8.16 |     25.03 ± 2.97 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-06 10:37:04 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
