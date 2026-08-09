# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-09 06:40:28
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model granite-4-1-8b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| granite-4-1-8b-bf16 |  pp1024 (c1) | 2942.64 ± 802.37 |  2942.64 ± 802.37 |               |                  |  492.78 ± 102.07 |  338.31 ± 102.07 |  492.78 ± 102.07 |
| granite-4-1-8b-bf16 |  tg1024 (c1) |     12.26 ± 0.10 |      12.26 ± 0.10 |  13.00 ± 0.00 |     13.00 ± 0.00 |                  |                  |                  |
| granite-4-1-8b-bf16 |  pp1024 (c5) |  3351.07 ± 57.36 | 1506.12 ± 1345.33 |               |                  | 1080.69 ± 391.11 |  926.22 ± 391.11 | 1080.69 ± 391.11 |
| granite-4-1-8b-bf16 |  tg1024 (c5) |     39.69 ± 4.79 |      12.52 ± 0.25 |  70.00 ± 0.00 |     14.00 ± 0.00 |                  |                  |                  |
| granite-4-1-8b-bf16 | pp1024 (c10) | 3576.91 ± 216.58 |  861.14 ± 1108.02 |               |                  | 1886.73 ± 689.10 | 1732.26 ± 689.10 | 1886.73 ± 689.10 |
| granite-4-1-8b-bf16 | tg1024 (c10) |     60.09 ± 7.00 |      11.99 ± 0.50 | 136.67 ± 4.71 |     13.73 ± 0.44 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-09 06:26:41 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
