# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-08 11:12:32
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model             |          test |   t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:------------------|--------------:|--------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| gemma-4-31b-nvfp4 |  pp25000 (c5) | 858.78 ± 0.78 | 374.85 ± 237.45 |              |                  |   82132.38 ± 37393.72 |   81921.13 ± 37393.72 |   82132.79 ± 37393.80 |
| gemma-4-31b-nvfp4 |    tg256 (c5) |   8.54 ± 0.02 |     3.23 ± 1.40 | 30.00 ± 0.00 |      6.33 ± 0.47 |                       |                       |                       |
| gemma-4-31b-nvfp4 | pp25000 (c10) | 856.48 ± 1.70 | 241.41 ± 213.12 |              |                  |  147913.50 ± 75343.44 |  147702.25 ± 75343.44 |  147913.88 ± 75343.75 |
| gemma-4-31b-nvfp4 |   tg256 (c10) |   8.67 ± 0.13 |     1.95 ± 1.14 | 50.00 ± 0.00 |      5.83 ± 0.64 |                       |                       |                       |
| gemma-4-31b-nvfp4 | pp25000 (c20) | 853.89 ± 0.73 | 148.78 ± 176.62 |              |                  | 280767.87 ± 152272.10 | 280556.61 ± 152272.10 | 280768.30 ± 152272.23 |
| gemma-4-31b-nvfp4 |   tg256 (c20) |   8.92 ± 0.02 |     1.14 ± 0.82 | 80.00 ± 0.00 |      5.02 ± 0.97 |                       |                       |                       |

llama-benchy (0.3.7)
date: 2026-05-08 10:17:45 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
