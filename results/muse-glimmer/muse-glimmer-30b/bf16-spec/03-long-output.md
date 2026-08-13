# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-12 16:10:24
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16-spec --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                      |         test |    t/s (total) |       t/s (req) |       peak t/s |   peak t/s (req) |        ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:---------------------------|-------------:|---------------:|----------------:|---------------:|-----------------:|-----------------:|----------------:|----------------:|
| muse-glimmer-30b-bf16-spec |   pp256 (c1) | 693.58 ± 46.29 |  693.58 ± 46.29 |                |                  |    600.68 ± 3.67 |   314.98 ± 3.67 |   858.96 ± 4.33 |
| muse-glimmer-30b-bf16-spec |  tg4096 (c1) |   13.12 ± 1.80 |    13.12 ± 1.80 |   60.67 ± 0.47 |     60.67 ± 0.47 |                  |                 |                 |
| muse-glimmer-30b-bf16-spec |   pp256 (c5) | 801.53 ± 23.97 | 461.42 ± 714.95 |                |                  | 1055.06 ± 185.34 | 769.36 ± 185.34 | 1369.09 ± 68.61 |
| muse-glimmer-30b-bf16-spec |  tg4096 (c5) |   48.45 ± 3.73 |    13.29 ± 2.44 | 269.00 ± 10.20 |     57.00 ± 4.27 |                  |                 |                 |
| muse-glimmer-30b-bf16-spec |  pp256 (c10) | 966.87 ± 36.43 |  132.72 ± 10.22 |                |                  |  1895.74 ± 15.34 | 1610.04 ± 15.34 | 2208.79 ± 15.72 |
| muse-glimmer-30b-bf16-spec | tg4096 (c10) |   89.62 ± 4.78 |    12.07 ± 1.42 | 517.33 ± 31.08 |     53.80 ± 5.44 |                  |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-12 15:05:04 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
