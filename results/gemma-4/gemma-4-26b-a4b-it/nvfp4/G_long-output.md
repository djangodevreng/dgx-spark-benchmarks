# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-05-06 11:05:08
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |     ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|--------------:|---------------:|----------------:|
| gemma-4-26b-a4b-nvfp4 |   pp256 (c1) | 5411.54 ± 553.44 | 5411.54 ± 553.44 |               |                  | 114.77 ± 4.28 |   45.95 ± 4.28 |   114.77 ± 4.28 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c1) |     29.59 ± 0.41 |     29.59 ± 0.41 |  31.00 ± 0.00 |     31.00 ± 0.00 |               |                |                 |
| gemma-4-26b-a4b-nvfp4 |   pp256 (c5) | 5136.96 ± 104.98 |  1483.83 ± 85.99 |               |                  | 225.03 ± 0.96 |  156.21 ± 0.96 |   225.03 ± 0.96 |
| gemma-4-26b-a4b-nvfp4 |  tg4096 (c5) |     94.35 ± 8.90 |     25.79 ± 0.85 | 131.67 ± 2.36 |     29.07 ± 2.14 |               |                |                 |
| gemma-4-26b-a4b-nvfp4 |  pp256 (c10) |  6357.02 ± 57.93 |   782.56 ± 39.74 |               |                  | 372.59 ± 1.91 |  303.76 ± 1.91 |   372.59 ± 1.91 |
| gemma-4-26b-a4b-nvfp4 | tg4096 (c10) |   143.28 ± 29.90 |     22.54 ± 0.92 | 231.33 ± 1.89 |     26.03 ± 2.83 |               |                |                 |

llama-benchy (0.3.7)
date: 2026-05-06 11:02:26 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
