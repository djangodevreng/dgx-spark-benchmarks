# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-16 15:56:20
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| gemma-4-26b-a4b-nvfp4 |   pp256 (c1) | 4356.41 ± 205.41 | 4356.41 ± 205.41 |               |                  |  118.51 ± 1.20 |   52.83 ± 1.20 |   118.51 ± 1.20 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c1) |     30.51 ± 0.14 |     30.51 ± 0.14 |  31.00 ± 0.00 |     31.00 ± 0.00 |                |                |                 |
| gemma-4-26b-a4b-nvfp4 |   pp256 (c5) |  5134.27 ± 69.73 |  1427.87 ± 52.30 |               |                  |  235.39 ± 2.46 |  169.70 ± 2.46 |   235.39 ± 2.46 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c5) |    105.91 ± 4.67 |     26.62 ± 0.72 | 135.00 ± 0.00 |     29.60 ± 1.93 |                |                |                 |
| gemma-4-26b-a4b-nvfp4 |  pp256 (c10) | 6091.78 ± 364.79 |  821.02 ± 131.40 |               |                  | 353.44 ± 35.46 | 287.75 ± 35.46 |  353.44 ± 35.46 |
| gemma-4-26b-a4b-nvfp4 | tg4096 (c10) |   169.07 ± 12.39 |     22.93 ± 0.68 | 243.33 ± 4.71 |     26.70 ± 2.72 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-16 15:52:39 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
