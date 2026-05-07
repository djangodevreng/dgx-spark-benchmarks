# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-05 11:42:36
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                |          test |    t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------|--------------:|---------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-bf16 |  pp25000 (c5) | 3309.79 ± 5.65 | 1456.60 ± 874.46 |               |                  |  20850.43 ± 9488.43 |  20737.68 ± 9488.43 |  20850.76 ± 9488.09 |
| qwen3.6-35b-a3b-bf16 |    tg256 (c5) |   26.74 ± 0.14 |      8.25 ± 2.35 |  66.33 ± 0.94 |     18.07 ± 4.51 |                     |                     |                     |
| qwen3.6-35b-a3b-bf16 | pp25000 (c10) | 3117.23 ± 1.66 |  919.25 ± 786.03 |               |                  | 39309.36 ± 20819.74 | 39196.61 ± 20819.74 | 39309.97 ± 20819.88 |
| qwen3.6-35b-a3b-bf16 |   tg256 (c10) |   27.29 ± 0.13 |      4.90 ± 1.86 |  97.00 ± 0.00 |     14.30 ± 5.09 |                     |                     |                     |
| qwen3.6-35b-a3b-bf16 | pp25000 (c20) | 2739.36 ± 4.40 |  567.36 ± 693.95 |               |                  | 80378.90 ± 47870.56 | 80266.15 ± 47870.56 | 80379.98 ± 47870.77 |
| qwen3.6-35b-a3b-bf16 |   tg256 (c20) |   26.83 ± 0.10 |      2.94 ± 1.65 | 130.00 ± 0.00 |     10.75 ± 5.23 |                     |                     |                     |

llama-benchy (0.3.7)
date: 2026-05-05 11:24:48 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
