# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-12 14:36:31
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16-spec --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                      |         test |      t/s (total) |        t/s (req) |       peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:---------------------------|-------------:|-----------------:|-----------------:|---------------:|-----------------:|------------------:|------------------:|------------------:|
| muse-glimmer-30b-bf16-spec |  pp1024 (c1) | 2153.41 ± 177.48 | 2153.41 ± 177.48 |                |                  |   1057.83 ± 37.47 |    447.96 ± 37.47 |   1284.61 ± 22.90 |
| muse-glimmer-30b-bf16-spec |  tg1024 (c1) |    20.72 ± 12.54 |    20.72 ± 12.54 |  52.33 ± 10.84 |    52.33 ± 10.84 |                   |                   |                   |
| muse-glimmer-30b-bf16-spec |  pp1024 (c5) |  1136.95 ± 34.47 |  529.42 ± 330.04 |                |                  |  2936.96 ± 989.97 |  2327.09 ± 989.97 |  3329.04 ± 900.80 |
| muse-glimmer-30b-bf16-spec |  tg1024 (c5) |    55.92 ± 13.20 |     17.80 ± 9.82 | 230.33 ± 26.20 |     53.67 ± 3.09 |                   |                   |                   |
| muse-glimmer-30b-bf16-spec | pp1024 (c10) |  1349.33 ± 16.50 | 369.90 ± 1028.90 |                |                  | 5666.74 ± 1016.93 | 5056.87 ± 1016.93 | 6467.47 ± 1016.12 |
| muse-glimmer-30b-bf16-spec | tg1024 (c10) |     86.23 ± 5.37 |     13.30 ± 6.78 |  393.33 ± 3.86 |     48.37 ± 5.81 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-12 14:17:00 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
