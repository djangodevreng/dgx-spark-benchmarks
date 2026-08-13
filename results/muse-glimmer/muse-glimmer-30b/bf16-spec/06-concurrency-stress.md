# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-12 17:51:20
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model muse-glimmer-30b-bf16-spec --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                      |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |            ttfr (ms) |         est_ppt (ms) |        e2e_ttft (ms) |
|:---------------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|---------------------:|---------------------:|---------------------:|
| muse-glimmer-30b-bf16-spec | pp25000 (c20) | 1372.42 ± 2.15 | 243.60 ± 288.30 |               |                  | 171624.08 ± 94349.91 | 171335.72 ± 94349.91 | 177317.07 ± 94061.14 |
| muse-glimmer-30b-bf16-spec |   tg256 (c20) |   14.13 ± 0.05 |     1.82 ± 1.23 | 131.67 ± 5.56 |     15.45 ± 4.71 |                      |                      |                      |

llama-benchy (0.4.0)
date: 2026-08-12 17:25:53 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
