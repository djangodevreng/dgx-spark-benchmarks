# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-06 12:36:58
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| gemma-4-26b-a4b-nvfp4 | pp25000 (c20) | 3251.76 ± 5.20 | 567.91 ± 675.63 |               |                  | 73574.78 ± 39896.53 | 73506.89 ± 39896.53 | 73575.71 ± 39896.74 |
| gemma-4-26b-a4b-nvfp4 |   tg256 (c20) |   33.16 ± 0.03 |     3.99 ± 2.60 | 240.00 ± 0.00 |     15.87 ± 3.52 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-06 12:26:12 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
