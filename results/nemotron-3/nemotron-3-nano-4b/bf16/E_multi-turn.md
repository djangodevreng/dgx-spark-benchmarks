# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-05-05 15:23:22
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |              test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------|------------------:|------------------:|------------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-4b-bf16 |  pp2048 @ d4 (c1) | 11199.69 ± 191.89 | 11199.69 ± 191.89 |               |                  |    231.18 ± 2.31 |    168.22 ± 2.31 |    231.18 ± 2.31 |
| nemotron-3-nano-4b-bf16 |   tg512 @ d4 (c1) |      25.75 ± 0.00 |      25.75 ± 0.00 |  26.00 ± 0.00 |     26.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-4b-bf16 |  pp2048 @ d4 (c5) |   8250.95 ± 28.73 | 3891.20 ± 2564.26 |               |                  |  731.80 ± 311.26 |  668.84 ± 311.26 |  731.80 ± 311.26 |
| nemotron-3-nano-4b-bf16 |   tg512 @ d4 (c5) |     129.90 ± 1.16 |      26.88 ± 0.37 | 140.00 ± 0.00 |     28.27 ± 0.44 |                  |                  |                  |
| nemotron-3-nano-4b-bf16 | pp2048 @ d4 (c10) |   8134.12 ± 59.22 | 2253.75 ± 1950.88 |               |                  | 1370.15 ± 666.19 | 1307.20 ± 666.19 | 1370.15 ± 666.19 |
| nemotron-3-nano-4b-bf16 |  tg512 @ d4 (c10) |     221.30 ± 3.83 |      23.72 ± 0.67 | 250.00 ± 0.00 |     25.50 ± 0.50 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-05 15:20:09 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
