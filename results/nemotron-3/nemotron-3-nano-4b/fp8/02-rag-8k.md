# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-08 09:37:18
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                  |         test |       t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:-----------------------|-------------:|------------------:|------------------:|--------------:|-----------------:|------------------:|------------------:|------------------:|
| nemotron-3-nano-4b-fp8 |  pp8192 (c5) | 10277.04 ± 421.14 | 4264.42 ± 2416.72 |               |                  |  2283.34 ± 960.53 |  2239.37 ± 960.53 |  2283.34 ± 960.53 |
| nemotron-3-nano-4b-fp8 |   tg512 (c5) |     155.87 ± 8.60 |      35.73 ± 2.49 | 201.67 ± 6.24 |     40.60 ± 1.08 |                   |                   |                   |
| nemotron-3-nano-4b-fp8 | pp8192 (c10) | 10546.43 ± 199.19 | 3019.53 ± 2560.06 |               |                  | 3853.31 ± 1967.23 | 3809.35 ± 1967.23 | 3853.31 ± 1967.23 |
| nemotron-3-nano-4b-fp8 |  tg512 (c10) |     225.13 ± 2.09 |      27.64 ± 2.60 | 330.00 ± 0.00 |     35.27 ± 1.79 |                   |                   |                   |
| nemotron-3-nano-4b-fp8 | pp8192 (c20) |  10255.20 ± 73.49 | 1832.37 ± 2138.04 |               |                  | 7439.99 ± 4067.81 | 7396.02 ± 4067.81 | 7439.99 ± 4067.81 |
| nemotron-3-nano-4b-fp8 |  tg512 (c20) |     286.73 ± 3.94 |      19.09 ± 2.86 | 480.00 ± 0.00 |     28.92 ± 4.30 |                   |                   |                   |

llama-benchy (0.4.0)
date: 2026-08-08 09:32:14 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
