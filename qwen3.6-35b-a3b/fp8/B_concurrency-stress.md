# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-04 21:25:02
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-fp8 |  pp25000 (c5) |  4748.62 ± 7.86 | 2072.06 ± 1238.95 |               |                  |  14612.85 ± 6610.16 |  14545.55 ± 6610.16 |  14614.41 ± 6610.08 |
| qwen3.6-35b-a3b-fp8 |    tg256 (c5) |    40.96 ± 0.05 |      13.22 ± 4.22 | 104.33 ± 0.47 |     27.47 ± 5.90 |                     |                     |                     |
| qwen3.6-35b-a3b-fp8 | pp25000 (c10) | 4564.93 ± 88.26 | 1276.63 ± 1073.46 |               |                  | 27568.60 ± 14105.28 | 27501.31 ± 14105.28 | 27569.72 ± 14105.46 |
| qwen3.6-35b-a3b-fp8 |   tg256 (c10) |    42.29 ± 0.88 |       8.09 ± 3.37 | 147.67 ± 3.30 |     21.60 ± 6.87 |                     |                     |                     |
| qwen3.6-35b-a3b-fp8 | pp25000 (c20) |  4451.78 ± 6.48 |   806.35 ± 929.31 |               |                  | 52327.65 ± 29245.60 | 52260.35 ± 29245.60 | 52327.79 ± 29245.65 |
| qwen3.6-35b-a3b-fp8 |   tg256 (c20) |    44.44 ± 0.07 |       5.16 ± 2.95 | 213.00 ± 5.10 |     16.77 ± 6.98 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-04 21:13:51 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
