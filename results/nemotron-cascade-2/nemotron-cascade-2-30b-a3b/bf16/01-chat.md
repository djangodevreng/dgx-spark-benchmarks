# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-09 10:35:31
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-cascade-2-30b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                       |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-cascade-2-30b-bf16 |  pp1024 (c1) | 2396.11 ± 245.10 |  2396.11 ± 245.10 |               |                  |   552.41 ± 38.45 |   369.73 ± 38.45 |   552.41 ± 38.45 |
| nemotron-cascade-2-30b-bf16 |  tg1024 (c1) |     29.06 ± 0.05 |      29.06 ± 0.05 |  30.67 ± 0.47 |     30.67 ± 0.47 |                  |                  |                  |
| nemotron-cascade-2-30b-bf16 |  pp1024 (c5) |  4107.90 ± 31.61 | 1510.18 ± 1073.75 |               |                  |  996.98 ± 277.21 |  814.30 ± 277.21 |  996.98 ± 277.21 |
| nemotron-cascade-2-30b-bf16 |  tg1024 (c5) |     54.70 ± 0.43 |      11.01 ± 0.09 |  66.67 ± 2.36 |     13.33 ± 0.47 |                  |                  |                  |
| nemotron-cascade-2-30b-bf16 | pp1024 (c10) |  5113.97 ± 12.10 |  1024.81 ± 940.96 |               |                  | 1496.52 ± 504.87 | 1313.84 ± 504.87 | 1496.52 ± 504.87 |
| nemotron-cascade-2-30b-bf16 | tg1024 (c10) |     75.25 ± 0.39 |       7.59 ± 0.05 | 100.00 ± 0.00 |     10.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-09 10:17:40 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
