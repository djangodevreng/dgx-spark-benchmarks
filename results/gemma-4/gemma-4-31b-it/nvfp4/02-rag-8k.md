# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-16 19:19:05
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-31b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model             |         test |   t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:------------------|-------------:|--------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| gemma-4-31b-nvfp4 |  pp8192 (c5) | 779.65 ± 6.92 | 282.99 ± 145.60 |               |                  |  32434.25 ± 12385.78 |  32235.63 ± 12385.78 |  32434.25 ± 12385.78 |
| gemma-4-31b-nvfp4 |   tg512 (c5) |  21.28 ± 0.29 |     5.37 ± 0.69 |  35.00 ± 0.00 |      7.00 ± 0.00 |                      |                      |                      |
| gemma-4-31b-nvfp4 | pp8192 (c10) | 787.08 ± 0.71 | 187.21 ± 146.65 |               |                  |  57922.16 ± 27473.97 |  57723.54 ± 27473.97 |  57922.16 ± 27473.97 |
| gemma-4-31b-nvfp4 |  tg512 (c10) |  25.65 ± 1.68 |     4.12 ± 1.09 |  60.00 ± 0.00 |      6.60 ± 0.49 |                      |                      |                      |
| gemma-4-31b-nvfp4 | pp8192 (c20) | 786.23 ± 0.13 | 118.34 ± 124.91 |               |                  | 105836.23 ± 54288.25 | 105637.61 ± 54288.25 | 105836.23 ± 54288.25 |
| gemma-4-31b-nvfp4 |  tg512 (c20) |  30.46 ± 0.40 |     2.63 ± 0.92 | 100.00 ± 0.00 |      5.87 ± 0.83 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-08-16 18:38:17 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
