# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-12 07:39:09
**Profile:** bf16
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |       t/s (total) |         t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|------------------:|------------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| muse-glimmer-30b-bf16 |   pp256 (c1) | 1689.92 ± 1253.09 | 1689.92 ± 1253.09 |              |                  |   461.88 ± 97.97 |   196.52 ± 97.97 |  1150.76 ± 98.05 |
| muse-glimmer-30b-bf16 |  tg4096 (c1) |       4.28 ± 0.03 |       4.28 ± 0.03 |  5.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| muse-glimmer-30b-bf16 |   pp256 (c5) |    631.08 ± 51.97 | 1101.22 ± 1617.30 |              |                  |  866.02 ± 274.37 |  600.67 ± 274.37 | 1682.35 ± 102.29 |
| muse-glimmer-30b-bf16 |  tg4096 (c5) |      17.71 ± 2.11 |       4.21 ± 0.03 | 25.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |
| muse-glimmer-30b-bf16 |  pp256 (c10) |    881.37 ± 42.81 |  488.66 ± 1029.15 |              |                  | 1598.22 ± 423.97 | 1332.86 ± 423.97 |  2423.38 ± 83.18 |
| muse-glimmer-30b-bf16 | tg4096 (c10) |      34.49 ± 3.58 |       4.09 ± 0.03 | 50.00 ± 0.00 |      5.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-12 04:33:59 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
