# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-14 15:59:46
**Profile:** fp8
**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-fp8 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model               |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:--------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-fp8 | pp25000 (c20) | 3539.69 ± 3.20 | 630.86 ± 737.22 |               |                  | 66864.27 ± 36898.83 | 66796.05 ± 36898.83 | 66866.46 ± 36898.80 |
| qwen3.6-35b-a3b-fp8 |   tg256 (c20) |   36.69 ± 0.04 |     4.69 ± 3.18 | 222.67 ± 2.05 |     17.87 ± 7.39 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-14 15:49:59 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
