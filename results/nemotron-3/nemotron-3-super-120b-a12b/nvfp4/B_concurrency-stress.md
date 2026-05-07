# Run B — 25k context, c=5/10/20

**Generated:** 2026-05-05 03:02:35
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-super --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model            |          test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:-----------------|--------------:|---------------:|----------------:|-------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| nemotron-3-super |  pp25000 (c5) | 1590.65 ± 1.14 | 685.96 ± 407.62 |              |                  |  43798.97 ± 19674.83 |  43598.13 ± 19674.83 |  43799.96 ± 19674.36 |
| nemotron-3-super |    tg256 (c5) |   16.88 ± 0.22 |     6.88 ± 3.16 | 69.33 ± 4.19 |     19.47 ± 3.34 |                      |                      |                      |
| nemotron-3-super | pp25000 (c10) | 1570.71 ± 0.97 | 433.78 ± 357.98 |              |                  |  79994.17 ± 40711.52 |  79793.34 ± 40711.52 |  79994.43 ± 40711.55 |
| nemotron-3-super |   tg256 (c10) |   17.07 ± 0.13 |     4.47 ± 2.87 | 87.00 ± 2.16 |     16.30 ± 5.76 |                      |                      |                      |
| nemotron-3-super | pp25000 (c20) | 1541.47 ± 4.11 | 268.19 ± 302.77 |              |                  | 153193.77 ± 84135.90 | 152992.93 ± 84135.90 | 153194.27 ± 84135.92 |
| nemotron-3-super |   tg256 (c20) |   16.20 ± 0.30 |     2.90 ± 2.21 | 79.00 ± 8.29 |      8.92 ± 5.92 |                      |                      |                      |

llama-benchy (0.3.7)
date: 2026-05-05 02:33:50 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
