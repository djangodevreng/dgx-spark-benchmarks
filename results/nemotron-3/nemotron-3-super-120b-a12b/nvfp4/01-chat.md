# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-15 04:41:55
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |      t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|---------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-super |  pp1024 (c1) | 944.74 ± 65.53 | 944.74 ± 65.53 |               |                  |   1229.62 ± 83.99 |   1011.97 ± 83.99 |   1229.62 ± 83.99 |
| nemotron-3-super |  tg1024 (c1) |   21.47 ± 1.37 |   21.47 ± 1.37 |  32.00 ± 2.16 |     32.00 ± 2.16 |                   |                   |                   |
| nemotron-3-super |  pp1024 (c5) | 1112.58 ± 6.71 | 272.08 ± 58.69 |               |                  |  3745.06 ± 615.01 |  3527.41 ± 615.01 |  3745.06 ± 615.01 |
| nemotron-3-super |  tg1024 (c5) |   50.86 ± 1.62 |   10.68 ± 0.46 |  75.00 ± 0.82 |     19.73 ± 2.95 |                   |                   |                   |
| nemotron-3-super | pp1024 (c10) | 1129.65 ± 1.40 | 181.38 ± 81.56 |               |                  | 6114.84 ± 1891.57 | 5897.19 ± 1891.57 | 6114.84 ± 1891.57 |
| nemotron-3-super | tg1024 (c10) |   72.58 ± 1.10 |    8.10 ± 0.39 | 115.67 ± 3.40 |     15.17 ± 2.84 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-15 04:22:52 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
