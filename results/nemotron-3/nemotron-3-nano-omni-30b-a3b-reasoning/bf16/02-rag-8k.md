# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-06 00:24:44
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                         |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| nemotron-3-nano-omni-30b-bf16 |  pp8192 (c5) | 6852.40 ± 13.20 | 3192.33 ± 2106.03 |               |                  |  3385.98 ± 1534.41 |  3249.81 ± 1534.41 |  3385.98 ± 1534.41 |
| nemotron-3-nano-omni-30b-bf16 |   tg512 (c5) |    52.85 ± 2.14 |      11.96 ± 1.23 |  69.33 ± 1.89 |     16.67 ± 2.09 |                    |                    |                    |
| nemotron-3-nano-omni-30b-bf16 | pp8192 (c10) |  6883.76 ± 9.78 | 2028.96 ± 1961.77 |               |                  |  6258.40 ± 3201.46 |  6122.23 ± 3201.46 |  6258.40 ± 3201.46 |
| nemotron-3-nano-omni-30b-bf16 |  tg512 (c10) |    67.37 ± 0.36 |       7.53 ± 0.46 |  92.00 ± 2.83 |     10.63 ± 1.60 |                    |                    |                    |
| nemotron-3-nano-omni-30b-bf16 | pp8192 (c20) |  6905.52 ± 5.36 | 1231.02 ± 1562.58 |               |                  | 11606.23 ± 6170.92 | 11470.06 ± 6170.92 | 11606.23 ± 6170.92 |
| nemotron-3-nano-omni-30b-bf16 |  tg512 (c20) |    93.87 ± 1.42 |       5.50 ± 0.38 | 153.33 ± 9.43 |      8.52 ± 1.28 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-06 00:09:45 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
