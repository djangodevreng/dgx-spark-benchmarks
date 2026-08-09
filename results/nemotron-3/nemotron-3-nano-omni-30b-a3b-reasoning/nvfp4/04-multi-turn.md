# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-07 12:50:33
**Profile:** nvfp4
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-nvfp4 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                          |              test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------------------|------------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-nvfp4 |  pp2048 @ d4 (c1) | 3333.86 ± 152.35 | 3333.86 ± 152.35 |               |                  |   617.18 ± 15.85 |   562.23 ± 15.85 |   617.18 ± 15.85 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg512 @ d4 (c1) |     64.20 ± 0.15 |     64.20 ± 0.15 |  65.00 ± 0.00 |     65.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-omni-30b-nvfp4 |  pp2048 @ d4 (c5) | 5516.40 ± 304.72 | 1448.66 ± 691.19 |               |                  | 1516.27 ± 378.69 | 1461.33 ± 378.69 | 1516.27 ± 378.69 |
| nemotron-3-nano-omni-30b-nvfp4 |   tg512 @ d4 (c5) |    146.13 ± 6.39 |     33.24 ± 2.31 | 172.33 ± 2.05 |     38.33 ± 4.38 |                  |                  |                  |
| nemotron-3-nano-omni-30b-nvfp4 | pp2048 @ d4 (c10) | 6571.29 ± 243.06 | 1098.97 ± 669.26 |               |                  | 2142.62 ± 714.33 | 2087.67 ± 714.33 | 2142.62 ± 714.33 |
| nemotron-3-nano-omni-30b-nvfp4 |  tg512 @ d4 (c10) |    206.65 ± 4.36 |     23.60 ± 1.43 | 260.00 ± 0.00 |     29.87 ± 2.14 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-07 12:47:19 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
