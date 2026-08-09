# Test 06-concurrency-stress — 25k context, c=20 (c=5/10 zit in 05-big-context)

**Generated:** 2026-08-07 13:08:51
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                          |          test |    t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:-------------------------------|--------------:|---------------:|------------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| nemotron-3-nano-omni-30b-nvfp4 | pp25000 (c20) | 7326.03 ± 9.61 | 1248.65 ± 1443.11 |               |                  | 32651.44 ± 17602.25 | 32595.93 ± 17602.25 | 32653.54 ± 17602.66 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg256 (c20) |   67.62 ± 1.52 |       7.21 ± 3.80 | 346.67 ± 9.43 |     21.85 ± 4.58 |                     |                     |                     |

llama-benchy (0.4.0)
date: 2026-08-07 13:03:46 | latency mode: generation

---

Volledige log in `06-concurrency-stress.log`. Server-config in `meta.json`.
