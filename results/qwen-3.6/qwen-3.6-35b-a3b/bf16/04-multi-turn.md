# Test 04-multi-turn — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-08-08 13:06:45
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                |              test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:---------------------|------------------:|----------------:|-----------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-35b-a3b-bf16 |  pp2048 @ d4 (c1) | 4124.80 ± 14.67 |  4124.80 ± 14.67 |               |                  |    549.66 ± 12.39 |    442.33 ± 12.39 |    549.66 ± 12.39 |
| qwen3.6-35b-a3b-bf16 |   tg512 @ d4 (c1) |    30.34 ± 0.07 |     30.34 ± 0.07 |  31.00 ± 0.00 |     31.00 ± 0.00 |                   |                   |                   |
| qwen3.6-35b-a3b-bf16 |  pp2048 @ d4 (c5) | 3518.57 ± 59.25 | 1410.98 ± 801.68 |               |                  |  1818.65 ± 703.38 |  1711.32 ± 703.38 |  1818.65 ± 703.38 |
| qwen3.6-35b-a3b-bf16 |   tg512 @ d4 (c5) |    61.09 ± 0.71 |     12.56 ± 0.25 |  75.00 ± 0.00 |     15.00 ± 0.00 |                   |                   |                   |
| qwen3.6-35b-a3b-bf16 | pp2048 @ d4 (c10) | 3546.42 ± 16.79 |  912.47 ± 737.58 |               |                  | 3177.59 ± 1506.29 | 3070.27 ± 1506.29 | 3177.59 ± 1506.29 |
| qwen3.6-35b-a3b-bf16 |  tg512 @ d4 (c10) |    82.36 ± 1.34 |      8.61 ± 0.24 | 106.67 ± 4.71 |     11.20 ± 0.87 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-08 12:58:28 | latency mode: generation

---

Volledige log in `04-multi-turn.log`. Server-config in `meta.json`.
