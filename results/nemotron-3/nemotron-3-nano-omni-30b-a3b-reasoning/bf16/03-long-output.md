# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-06 00:53:07
**Profile:** bf16
**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-omni-30b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                         |         test |      t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------------------|-------------:|-----------------:|----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-omni-30b-bf16 |   pp256 (c1) |  1492.58 ± 74.09 | 1492.58 ± 74.09 |               |                  |  295.01 ± 10.47 |  159.03 ± 10.47 |  295.01 ± 10.47 |
| nemotron-3-nano-omni-30b-bf16 |  tg4096 (c1) |     29.32 ± 0.08 |    29.32 ± 0.08 |  30.00 ± 0.00 |     30.00 ± 0.00 |                 |                 |                 |
| nemotron-3-nano-omni-30b-bf16 |   pp256 (c5) | 2466.29 ± 518.68 | 754.76 ± 207.62 |               |                  |  470.10 ± 99.58 |  334.12 ± 99.58 |  470.10 ± 99.58 |
| nemotron-3-nano-omni-30b-bf16 |  tg4096 (c5) |     50.84 ± 4.52 |    15.20 ± 3.10 |  72.33 ± 2.05 |     20.00 ± 5.39 |                 |                 |                 |
| nemotron-3-nano-omni-30b-bf16 |  pp256 (c10) | 2934.24 ± 103.40 | 484.88 ± 236.22 |               |                  | 688.07 ± 167.17 | 552.09 ± 167.17 | 688.07 ± 167.17 |
| nemotron-3-nano-omni-30b-bf16 | tg4096 (c10) |     63.28 ± 5.06 |    10.24 ± 2.44 | 103.33 ± 4.71 |     15.80 ± 6.36 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-06 00:24:44 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
