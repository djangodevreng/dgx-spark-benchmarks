# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-15 05:08:43
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model            |         test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------|-------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-super |  pp8192 (c5) | 1239.50 ± 6.34 | 469.42 ± 243.41 |               |                  |  19561.59 ± 7721.09 |  19357.14 ± 7721.09 |  19561.59 ± 7721.09 |
| nemotron-3-super |   tg512 (c5) |   37.29 ± 0.41 |     9.38 ± 1.11 |  73.00 ± 4.24 |     19.20 ± 3.80 |                     |                     |                     |
| nemotron-3-super | pp8192 (c10) | 1225.89 ± 0.75 | 311.08 ± 234.85 |               |                  | 34651.71 ± 16837.67 | 34447.27 ± 16837.67 | 34651.71 ± 16837.67 |
| nemotron-3-super |  tg512 (c10) |   43.95 ± 0.79 |     6.35 ± 1.15 | 105.33 ± 4.64 |     15.20 ± 2.79 |                     |                     |                     |
| nemotron-3-super | pp8192 (c20) | 1200.35 ± 0.33 | 196.22 ± 206.88 |               |                  | 65732.75 ± 35379.21 | 65528.30 ± 35379.21 | 65732.75 ± 35379.21 |
| nemotron-3-super |  tg512 (c20) |   50.46 ± 1.33 |     4.16 ± 1.11 | 138.33 ± 3.86 |     12.07 ± 3.55 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-15 04:41:55 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
