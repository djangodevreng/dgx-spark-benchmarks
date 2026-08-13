# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-09 11:43:29
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-cascade-2-30b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                       |              test |     t/s (total) |         t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------------|------------------:|----------------:|------------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-cascade-2-30b-bf16 |  pp2048 @ d4 (c1) | 5807.76 ± 89.69 |   5807.76 ± 89.69 |              |                  |    480.90 ± 7.60 |    311.78 ± 7.60 |    480.90 ± 7.60 |
| nemotron-cascade-2-30b-bf16 |   tg512 @ d4 (c1) |    29.08 ± 0.01 |      29.08 ± 0.01 | 30.00 ± 0.00 |     30.00 ± 0.00 |                  |                  |                  |
| nemotron-cascade-2-30b-bf16 |  pp2048 @ d4 (c5) | 6060.15 ± 63.84 | 2173.80 ± 1639.38 |              |                  | 1348.01 ± 414.00 | 1178.89 ± 414.00 | 1348.01 ± 414.00 |
| nemotron-cascade-2-30b-bf16 |   tg512 @ d4 (c5) |    54.19 ± 0.44 |      11.03 ± 0.13 | 66.67 ± 2.36 |     13.33 ± 0.47 |                  |                  |                  |
| nemotron-cascade-2-30b-bf16 | pp2048 @ d4 (c10) | 6099.16 ± 12.68 | 1383.24 ± 1328.65 |              |                  | 2126.90 ± 777.37 | 1957.78 ± 777.37 | 2126.90 ± 777.37 |
| nemotron-cascade-2-30b-bf16 |  tg512 @ d4 (c10) |    73.92 ± 1.25 |       7.58 ± 0.15 | 96.67 ± 4.71 |      9.67 ± 0.47 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-09 11:34:23 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
