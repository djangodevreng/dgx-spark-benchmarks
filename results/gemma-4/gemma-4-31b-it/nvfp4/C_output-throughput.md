# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-08 12:15:33
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |      t/s (total) |   t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |   est_ppt (ms) |     e2e_ttft (ms) |
|:------------------|-------------:|-----------------:|------------:|-------------:|-----------------:|------------------:|---------------:|------------------:|
| gemma-4-31b-nvfp4 |  tg1024 (c1) |      1.71 ± 0.24 | 1.71 ± 0.24 |  2.67 ± 0.47 |      2.67 ± 0.47 |                   |                |                   |
| gemma-4-31b-nvfp4 |  pp1024 (c5) |  1404.41 ± 11.34 |             |              |                  |   3330.33 ± 49.12 |    0.00 ± 0.00 |   3330.33 ± 49.12 |
| gemma-4-31b-nvfp4 |  tg1024 (c5) |      6.72 ± 0.70 | 2.01 ± 0.11 | 15.00 ± 0.00 |      3.07 ± 0.25 |                   |                |                   |
| gemma-4-31b-nvfp4 | pp1024 (c10) | 1245.51 ± 236.55 |             |              |                  | 6940.88 ± 1712.98 |    0.00 ± 0.00 | 6940.88 ± 1712.98 |
| gemma-4-31b-nvfp4 | tg1024 (c10) |     15.46 ± 0.74 | 2.21 ± 0.08 | 37.33 ± 3.77 |      3.93 ± 0.25 |                   |                |                   |

llama-benchy (0.3.7)
date: 2026-05-08 11:15:40 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
