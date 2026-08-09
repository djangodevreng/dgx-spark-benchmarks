# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-06 11:59:14
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |     ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|--------------:|---------------:|----------------:|
| gemma-4-26b-a4b-nvfp4 |   pp256 (c1) | 4651.15 ± 82.28 | 4651.15 ± 82.28 |               |                  | 119.18 ± 0.17 |   52.46 ± 0.17 |   119.18 ± 0.17 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c1) |    30.01 ± 0.19 |    30.01 ± 0.19 |  31.00 ± 0.00 |     31.00 ± 0.00 |               |                |                 |
| gemma-4-26b-a4b-nvfp4 |   pp256 (c5) | 5010.01 ± 79.40 | 1398.24 ± 91.23 |               |                  | 237.49 ± 6.22 |  170.77 ± 6.22 |   237.49 ± 6.22 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c5) |    96.54 ± 8.75 |    26.18 ± 1.01 | 131.67 ± 2.36 |     29.47 ± 2.70 |               |                |                 |
| gemma-4-26b-a4b-nvfp4 |  pp256 (c10) | 6088.59 ± 36.66 |  738.70 ± 41.84 |               |                  | 382.41 ± 4.92 |  315.69 ± 4.92 |   382.41 ± 4.92 |
| gemma-4-26b-a4b-nvfp4 | tg4096 (c10) |   161.48 ± 0.99 |    22.94 ± 0.76 | 236.67 ± 4.71 |     26.67 ± 3.08 |               |                |                 |

llama-benchy (0.4.0)
date: 2026-08-06 11:53:09 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
