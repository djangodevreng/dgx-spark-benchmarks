# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-04 23:06:27
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model             |          test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------|--------------:|------------------:|------------------:|---------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.5-0.8b-bf16 |  pp25000 (c5) |  20894.44 ± 31.58 | 8940.71 ± 5149.15 |                |                  |  3338.06 ± 1479.24 |  3315.60 ± 1479.24 |  3339.13 ± 1478.90 |
| qwen3.5-0.8b-bf16 |    tg256 (c5) |     176.77 ± 4.03 |     57.54 ± 17.37 |  431.67 ± 2.36 |     88.80 ± 2.64 |                    |                    |                    |
| qwen3.5-0.8b-bf16 | pp25000 (c10) |  20164.33 ± 51.34 | 5328.84 ± 4019.07 |                |                  |  6258.45 ± 3117.15 |  6235.99 ± 3117.15 |  6259.41 ± 3117.05 |
| qwen3.5-0.8b-bf16 |   tg256 (c10) |     186.34 ± 1.95 |     36.15 ± 15.19 |  643.33 ± 4.71 |     73.13 ± 7.50 |                    |                    |                    |
| qwen3.5-0.8b-bf16 | pp25000 (c20) | 18970.06 ± 280.60 | 3203.19 ± 3425.97 |                |                  | 12321.98 ± 6762.45 | 12299.52 ± 6762.45 | 12323.21 ± 6762.46 |
| qwen3.5-0.8b-bf16 |   tg256 (c20) |     176.35 ± 6.62 |     20.88 ± 12.57 | 777.33 ± 11.09 |    57.30 ± 19.41 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-04 23:03:51 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
