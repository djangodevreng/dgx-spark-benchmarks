# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-13 10:27:07
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model mistral-small-4-119b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                      |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:---------------------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| mistral-small-4-119b-nvfp4 |  pp8192 (c5) |  4139.00 ± 3.34 | 1591.26 ± 934.00 |               |                  |   6085.03 ± 2411.57 |   5971.06 ± 2411.57 |   6085.03 ± 2411.57 |
| mistral-small-4-119b-nvfp4 |   tg512 (c5) |    57.39 ± 1.35 |     14.61 ± 2.34 |  77.33 ± 1.89 |     19.40 ± 3.72 |                     |                     |                     |
| mistral-small-4-119b-nvfp4 | pp8192 (c10) |  4085.73 ± 3.78 | 1024.31 ± 869.51 |               |                  |  11124.68 ± 5335.28 |  11010.70 ± 5335.28 |  11124.68 ± 5335.28 |
| mistral-small-4-119b-nvfp4 |  tg512 (c10) |    60.50 ± 3.84 |      8.99 ± 2.26 | 100.00 ± 0.00 |     13.83 ± 2.98 |                     |                     |                     |
| mistral-small-4-119b-nvfp4 | pp8192 (c20) | 4034.93 ± 86.72 |  636.49 ± 727.88 |               |                  | 20558.26 ± 10618.67 | 20444.28 ± 10618.67 | 20558.26 ± 10618.67 |
| mistral-small-4-119b-nvfp4 |  tg512 (c20) |    75.45 ± 0.82 |      5.33 ± 1.42 | 138.67 ± 1.89 |      9.50 ± 2.37 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-13 10:13:22 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
