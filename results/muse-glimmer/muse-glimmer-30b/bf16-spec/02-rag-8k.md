# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-12 15:05:03
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16-spec --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                      |         test |    t/s (total) |       t/s (req) |       peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------------|-------------:|---------------:|----------------:|---------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| muse-glimmer-30b-bf16-spec |  pp8192 (c5) | 1443.45 ± 9.44 | 650.80 ± 426.67 |                |                  |  15999.75 ± 7174.08 |  15622.31 ± 7174.08 |  19688.66 ± 6329.44 |
| muse-glimmer-30b-bf16-spec |   tg512 (c5) |   29.92 ± 1.02 |     8.63 ± 2.15 |  89.00 ± 10.42 |     29.40 ± 9.88 |                     |                     |                     |
| muse-glimmer-30b-bf16-spec | pp8192 (c10) | 1458.94 ± 7.50 | 418.23 ± 396.86 |                |                  | 29449.59 ± 14994.36 | 29072.15 ± 14994.36 | 33973.61 ± 13827.00 |
| muse-glimmer-30b-bf16-spec |  tg512 (c10) |   43.99 ± 1.32 |     6.63 ± 1.42 | 130.33 ± 14.38 |     27.03 ± 8.16 |                     |                     |                     |
| muse-glimmer-30b-bf16-spec | pp8192 (c20) | 1440.07 ± 0.38 | 257.93 ± 329.56 |                |                  | 55047.25 ± 29181.21 | 54669.81 ± 29181.21 | 60616.11 ± 28679.91 |
| muse-glimmer-30b-bf16-spec |  tg512 (c20) |   52.06 ± 0.50 |     4.12 ± 0.95 |  160.00 ± 2.94 |     22.45 ± 6.33 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-12 14:36:32 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
