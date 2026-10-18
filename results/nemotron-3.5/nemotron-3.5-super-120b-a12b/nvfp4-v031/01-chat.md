# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-10-17 21:49:27
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3.5-super --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model              |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3.5-super |  pp1024 (c1) | 1634.77 ± 64.07 | 1634.77 ± 64.07 |               |                  |    775.56 ± 45.84 |    581.28 ± 45.84 |    775.56 ± 45.84 |
| nemotron-3.5-super |  tg1024 (c1) |    34.29 ± 0.76 |    34.29 ± 0.76 |  45.67 ± 0.94 |     45.67 ± 0.94 |                   |                   |                   |
| nemotron-3.5-super |  pp1024 (c5) | 2121.05 ± 42.60 | 644.16 ± 257.97 |               |                  |  1816.22 ± 436.36 |  1621.95 ± 436.36 |  1816.26 ± 436.30 |
| nemotron-3.5-super |  tg1024 (c5) |    70.43 ± 2.15 |    16.31 ± 0.59 | 102.33 ± 4.78 |     26.80 ± 4.92 |                   |                   |                   |
| nemotron-3.5-super | pp1024 (c10) | 2196.76 ± 60.48 | 421.29 ± 241.01 |               |                  | 2932.25 ± 1051.37 | 2737.98 ± 1051.37 | 2932.32 ± 1051.36 |
| nemotron-3.5-super | tg1024 (c10) |   104.14 ± 1.53 |    12.27 ± 0.42 | 167.33 ± 6.13 |     21.77 ± 5.82 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-10-17 21:37:20 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
