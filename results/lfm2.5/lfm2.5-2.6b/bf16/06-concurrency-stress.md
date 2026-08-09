# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-08 16:49:22
**Profile:** bf16
**Model:** LiquidAI/LFM2.5-2.6B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model lfm2-5-2-6b-bf16 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model            |          test |      t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-----------------|--------------:|-----------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| lfm2-5-2-6b-bf16 | pp25000 (c20) | 11436.62 ± 22.89 | 2011.13 ± 2392.13 |               |                  | 21230.41 ± 11585.22 | 21185.68 ± 11585.22 | 21230.72 ± 11585.44 |
| lfm2-5-2-6b-bf16 |   tg256 (c20) |    102.14 ± 0.91 |      10.06 ± 4.54 | 440.00 ± 0.00 |     26.33 ± 3.77 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-08 16:45:51 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
