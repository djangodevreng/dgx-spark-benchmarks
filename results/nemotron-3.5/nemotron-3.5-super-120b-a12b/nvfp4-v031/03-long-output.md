# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-10-17 22:28:07
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3.5-super --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model              |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |    est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|-----------------:|----------------:|-----------------:|
| nemotron-3.5-super |   pp256 (c1) | 1001.73 ± 85.11 | 1001.73 ± 85.11 |               |                  |    411.88 ± 2.18 |   222.43 ± 2.18 |    411.98 ± 2.11 |
| nemotron-3.5-super |  tg4096 (c1) |    35.35 ± 0.27 |    35.35 ± 0.27 |  45.67 ± 2.62 |     45.67 ± 2.62 |                  |                 |                  |
| nemotron-3.5-super |   pp256 (c5) | 1732.97 ± 14.52 |  483.57 ± 19.87 |               |                  |    673.87 ± 8.50 |   484.42 ± 8.50 |    673.96 ± 8.53 |
| nemotron-3.5-super |  tg4096 (c5) |    62.36 ± 7.96 |    18.11 ± 2.36 | 116.33 ± 3.68 |     30.20 ± 7.12 |                  |                 |                  |
| nemotron-3.5-super |  pp256 (c10) | 1717.28 ± 74.46 |  267.21 ± 56.18 |               |                  | 1081.30 ± 168.40 | 891.85 ± 168.40 | 1081.31 ± 168.39 |
| nemotron-3.5-super | tg4096 (c10) |    81.64 ± 4.91 |    13.58 ± 1.61 | 182.67 ± 1.70 |     25.30 ± 7.50 |                  |                 |                  |

llama-benchy (0.4.0)
date: 2026-10-17 22:05:03 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
