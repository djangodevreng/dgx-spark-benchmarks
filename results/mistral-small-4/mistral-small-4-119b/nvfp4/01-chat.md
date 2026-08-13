# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-13 10:13:22
**Profile:** nvfp4
**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model mistral-small-4-119b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                      |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:---------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| mistral-small-4-119b-nvfp4 |  pp1024 (c1) | 2322.26 ± 168.66 | 2322.26 ± 168.66 |               |                  |   518.76 ± 36.72 |   401.51 ± 36.72 |   518.76 ± 36.72 |
| mistral-small-4-119b-nvfp4 |  tg1024 (c1) |     31.07 ± 0.04 |     31.07 ± 0.04 |  32.00 ± 0.00 |     32.00 ± 0.00 |                  |                  |                  |
| mistral-small-4-119b-nvfp4 |  pp1024 (c5) | 3433.68 ± 102.59 |  897.47 ± 294.57 |               |                  | 1233.50 ± 242.76 | 1116.25 ± 242.76 | 1233.50 ± 242.76 |
| mistral-small-4-119b-nvfp4 |  tg1024 (c5) |     60.79 ± 1.61 |     17.47 ± 2.51 |  80.00 ± 0.00 |     22.67 ± 5.70 |                  |                  |                  |
| mistral-small-4-119b-nvfp4 | pp1024 (c10) |  3718.61 ± 63.32 |  501.42 ± 214.91 |               |                  | 2135.63 ± 400.64 | 2018.38 ± 400.64 | 2135.63 ± 400.64 |
| mistral-small-4-119b-nvfp4 | tg1024 (c10) |     80.21 ± 2.56 |     11.62 ± 1.35 | 113.33 ± 4.71 |     17.07 ± 5.97 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-13 10:05:28 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
