# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-06-26 08:03:53
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| qwen3.6-35b-a3b-nvfp4 |   pp256 (c1) | 4181.03 ± 212.06 | 4181.03 ± 212.06 |               |                  |  118.31 ± 2.02 |   54.87 ± 2.02 |   118.31 ± 2.02 |
| qwen3.6-35b-a3b-nvfp4 |  tg4096 (c1) |     40.56 ± 0.09 |     40.56 ± 0.09 |  42.00 ± 0.00 |     42.00 ± 0.00 |                |                |                 |
| qwen3.6-35b-a3b-nvfp4 |   pp256 (c5) | 4283.71 ± 356.34 | 1377.90 ± 415.26 |               |                  | 249.23 ± 42.90 | 185.79 ± 42.90 |  249.23 ± 42.90 |
| qwen3.6-35b-a3b-nvfp4 |  tg4096 (c5) |    101.10 ± 9.67 |     28.54 ± 2.67 | 145.00 ± 4.08 |     34.53 ± 4.10 |                |                |                 |
| qwen3.6-35b-a3b-nvfp4 |  pp256 (c10) | 5045.48 ± 320.75 |  713.21 ± 170.16 |               |                  | 404.21 ± 66.78 | 340.77 ± 66.78 |  404.21 ± 66.78 |
| qwen3.6-35b-a3b-nvfp4 | tg4096 (c10) |    156.48 ± 7.15 |     21.47 ± 2.03 | 240.00 ± 8.16 |     28.77 ± 5.09 |                |                |                 |

llama-benchy (0.3.8)
date: 2026-06-26 07:39:31 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
