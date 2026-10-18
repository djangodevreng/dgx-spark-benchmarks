# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-10-17 22:05:02
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3.5-super --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model              |         test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-------------------|-------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3.5-super |  pp8192 (c5) | 2348.37 ± 2.77 | 978.84 ± 573.83 |               |                  |  10066.35 ± 4243.26 |   9874.25 ± 4243.26 |  10066.57 ± 4243.24 |
| nemotron-3.5-super |   tg512 (c5) |   59.35 ± 1.27 |    14.56 ± 1.70 | 104.67 ± 7.93 |     24.27 ± 2.91 |                     |                     |                     |
| nemotron-3.5-super | pp8192 (c10) | 2344.94 ± 4.58 | 634.25 ± 526.06 |               |                  |  17903.23 ± 8865.66 |  17711.13 ± 8865.66 |  17903.72 ± 8865.65 |
| nemotron-3.5-super |  tg512 (c10) |   74.46 ± 0.22 |    10.21 ± 1.45 | 154.00 ± 3.27 |     19.40 ± 3.06 |                     |                     |                     |
| nemotron-3.5-super | pp8192 (c20) | 2300.18 ± 0.42 | 393.63 ± 437.51 |               |                  | 33702.71 ± 18341.26 | 33510.61 ± 18341.26 | 33703.52 ± 18341.24 |
| nemotron-3.5-super |  tg512 (c20) |   91.58 ± 1.11 |     7.25 ± 1.46 | 222.33 ± 4.19 |     15.97 ± 4.50 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-10-17 21:49:27 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
