# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-06 11:44:06
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c1) | 2580.07 ± 646.89 |  2580.07 ± 646.89 |               |                  |   449.17 ± 99.53 |   374.67 ± 99.53 |   449.17 ± 99.53 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c1) |     29.90 ± 0.04 |      29.90 ± 0.04 |  30.67 ± 0.47 |     30.67 ± 0.47 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 |  pp1024 (c5) | 5392.52 ± 340.99 | 2345.93 ± 1840.60 |               |                  |  651.63 ± 235.34 |  577.13 ± 235.34 |  651.63 ± 235.34 |
| gemma-4-26b-a4b-nvfp4 |  tg1024 (c5) |    87.09 ± 11.01 |      24.97 ± 0.97 | 128.33 ± 2.36 |     28.93 ± 2.54 |                  |                  |                  |
| gemma-4-26b-a4b-nvfp4 | pp1024 (c10) |  6273.65 ± 39.43 | 1285.82 ± 1629.88 |               |                  | 1278.14 ± 396.30 | 1203.65 ± 396.30 | 1278.14 ± 396.30 |
| gemma-4-26b-a4b-nvfp4 | tg1024 (c10) |   140.63 ± 21.10 |      21.10 ± 1.12 | 223.33 ± 4.71 |     25.60 ± 3.62 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-06 11:38:19 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
