# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-08 00:48:19
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-fp8 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-30b-fp8 |   pp256 (c1) | 1700.85 ± 695.80 | 1700.85 ± 695.80 |               |                  |  242.64 ± 49.42 |  158.18 ± 49.42 |  242.64 ± 49.42 |
| nemotron-3-nano-30b-fp8 |  tg4096 (c1) |     47.07 ± 0.06 |     47.07 ± 0.06 |  49.00 ± 0.00 |     49.00 ± 0.00 |                 |                 |                 |
| nemotron-3-nano-30b-fp8 |   pp256 (c5) | 2431.51 ± 450.86 |  680.14 ± 271.98 |               |                  | 467.94 ± 115.56 | 383.48 ± 115.56 | 467.94 ± 115.56 |
| nemotron-3-nano-30b-fp8 |  tg4096 (c5) |     89.93 ± 5.13 |     21.66 ± 2.31 | 114.00 ± 2.83 |     32.73 ± 8.75 |                 |                 |                 |
| nemotron-3-nano-30b-fp8 |  pp256 (c10) | 3254.79 ± 885.58 |  411.50 ± 220.35 |               |                  | 732.79 ± 178.74 | 648.33 ± 178.74 | 732.79 ± 178.74 |
| nemotron-3-nano-30b-fp8 | tg4096 (c10) |    116.83 ± 4.59 |     15.69 ± 2.28 | 166.67 ± 4.71 |     25.07 ± 9.81 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-08 00:28:09 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
