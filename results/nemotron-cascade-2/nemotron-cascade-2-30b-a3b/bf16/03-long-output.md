# Test 03-long-output — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-08-09 11:34:22
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-cascade-2-30b-bf16 --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                       |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-cascade-2-30b-bf16 |   pp256 (c1) | 1850.28 ± 193.16 | 1850.28 ± 193.16 |               |                  |   295.35 ± 7.99 |   128.96 ± 7.99 |   295.35 ± 7.99 |
| nemotron-cascade-2-30b-bf16 |  tg4096 (c1) |     29.07 ± 0.02 |     29.07 ± 0.02 |  30.00 ± 0.00 |     30.00 ± 0.00 |                 |                 |                 |
| nemotron-cascade-2-30b-bf16 |   pp256 (c5) |  2815.81 ± 28.39 |   940.64 ± 54.01 |               |                  |   416.05 ± 7.26 |   249.66 ± 7.26 |   416.05 ± 7.26 |
| nemotron-cascade-2-30b-bf16 |  tg4096 (c5) |     53.46 ± 1.64 |     12.29 ± 1.28 |  68.67 ± 0.94 |     20.20 ± 5.76 |                 |                 |                 |
| nemotron-cascade-2-30b-bf16 |  pp256 (c10) |  2926.11 ± 50.84 |  562.15 ± 319.84 |               |                  | 673.17 ± 176.30 | 506.77 ± 176.30 | 673.17 ± 176.30 |
| nemotron-cascade-2-30b-bf16 | tg4096 (c10) |     67.88 ± 1.43 |      8.53 ± 0.99 | 100.00 ± 0.00 |     15.47 ± 6.58 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-09 10:51:10 | latency mode: generation

---

Volledige log in `03-long-output.log`. Server-config in `meta.json`.
