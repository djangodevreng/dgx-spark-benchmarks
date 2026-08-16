# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-14 08:07:37
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|--------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| qwen3.6-35b-a3b-nvfp4 | pp25000 (c20) | 4657.34 ± 2.00 | 839.18 ± 986.62 |               |                  | 50718.92 ± 28110.84 | 50663.15 ± 28110.84 | 50720.94 ± 28110.71 |
| qwen3.6-35b-a3b-nvfp4 |   tg256 (c20) |   47.57 ± 0.05 |     5.91 ± 3.76 | 260.00 ± 0.00 |     20.20 ± 6.97 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-14 08:00:03 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
