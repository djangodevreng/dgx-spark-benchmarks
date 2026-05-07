# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-03 13:43:29
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                         |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-omni-30b-bf16 |  pp1024 (c1) |  4344.93 ± 39.22 |  4344.93 ± 39.22 |               |                  |    357.09 ± 7.12 |    211.22 ± 7.12 |    357.09 ± 7.12 |
| nemotron-3-nano-omni-30b-bf16 |  tg1024 (c1) |     28.65 ± 0.01 |     28.65 ± 0.01 |  29.00 ± 0.00 |     29.00 ± 0.00 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 |  pp1024 (c5) |  4558.59 ± 45.03 | 1640.44 ± 555.76 |               |                  |  776.51 ± 207.11 |  630.63 ± 207.11 |  776.51 ± 207.11 |
| nemotron-3-nano-omni-30b-bf16 |  tg1024 (c5) |     57.84 ± 1.19 |     12.19 ± 1.21 |  69.33 ± 0.94 |     15.80 ± 3.76 |                  |                  |                  |
| nemotron-3-nano-omni-30b-bf16 | pp1024 (c10) | 5814.75 ± 364.75 | 1032.17 ± 773.20 |               |                  | 1333.92 ± 402.84 | 1188.05 ± 402.84 | 1333.92 ± 402.84 |
| nemotron-3-nano-omni-30b-bf16 | tg1024 (c10) |     75.62 ± 1.39 |      7.84 ± 0.22 | 106.67 ± 4.71 |     10.67 ± 0.47 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-03 13:30:53 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
