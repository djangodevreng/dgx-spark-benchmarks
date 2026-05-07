# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-05-03 14:00:54
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                         |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-3-nano-omni-30b-bf16 |  pp8192 (c5) | 6762.68 ± 14.59 | 2992.82 ± 1918.27 |               |                  |  3506.42 ± 1523.85 |  3359.38 ± 1523.85 |  3506.42 ± 1523.85 |
| nemotron-3-nano-omni-30b-bf16 |   tg512 (c5) |    52.73 ± 4.11 |      12.50 ± 1.77 |  69.33 ± 1.89 |     17.53 ± 3.76 |                    |                    |                    |
| nemotron-3-nano-omni-30b-bf16 | pp8192 (c10) | 6794.13 ± 32.28 | 1902.53 ± 1725.99 |               |                  |  6428.66 ± 3228.24 |  6281.63 ± 3228.24 |  6428.66 ± 3228.24 |
| nemotron-3-nano-omni-30b-bf16 |  tg512 (c10) |    69.02 ± 0.26 |       8.11 ± 0.64 |  96.00 ± 0.00 |     11.63 ± 1.43 |                    |                    |                    |
| nemotron-3-nano-omni-30b-bf16 | pp8192 (c20) | 6802.19 ± 28.06 | 1157.91 ± 1399.05 |               |                  | 11823.70 ± 6222.51 | 11676.66 ± 6222.51 | 11823.70 ± 6222.51 |
| nemotron-3-nano-omni-30b-bf16 |  tg512 (c20) |    95.36 ± 0.76 |       5.51 ± 0.36 | 140.00 ± 0.00 |      8.30 ± 1.42 |                    |                    |                    |

llama-benchy (0.3.7)
date: 2026-05-03 13:50:05 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
