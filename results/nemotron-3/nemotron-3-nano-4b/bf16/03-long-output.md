# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-06 06:02:58
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                   |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| nemotron-3-nano-4b-bf16 |   pp256 (c1) | 5829.02 ± 786.09 | 5829.02 ± 786.09 |               |                  |  103.05 ± 4.15 |   41.84 ± 4.15 |   103.05 ± 4.15 |
| nemotron-3-nano-4b-bf16 |  tg4096 (c1) |     24.81 ± 0.13 |     24.81 ± 0.13 |  26.00 ± 0.00 |     26.00 ± 0.00 |                |                |                 |
| nemotron-3-nano-4b-bf16 |   pp256 (c5) |  5401.50 ± 12.24 |  1518.91 ± 83.55 |               |                  |  214.23 ± 6.21 |  153.02 ± 6.21 |   214.23 ± 6.21 |
| nemotron-3-nano-4b-bf16 |  tg4096 (c5) |     74.44 ± 9.04 |     27.47 ± 0.48 | 140.00 ± 0.00 |     29.27 ± 0.77 |                |                |                 |
| nemotron-3-nano-4b-bf16 |  pp256 (c10) | 5907.06 ± 104.49 |  862.20 ± 216.63 |               |                  | 345.27 ± 52.42 | 284.06 ± 52.42 |  345.27 ± 52.42 |
| nemotron-3-nano-4b-bf16 | tg4096 (c10) |    158.45 ± 2.66 |     25.22 ± 0.52 | 262.67 ± 3.77 |     27.83 ± 1.42 |                |                |                 |

llama-benchy (0.4.0)
date: 2026-08-06 05:45:17 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
