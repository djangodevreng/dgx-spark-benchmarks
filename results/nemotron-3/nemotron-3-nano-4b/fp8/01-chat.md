# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-08 09:32:14
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-4b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                  |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:-----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|----------------:|----------------:|----------------:|
| nemotron-3-nano-4b-fp8 |  pp1024 (c1) |  1643.61 ± 75.68 |  1643.61 ± 75.68 |               |                  |  594.96 ± 21.93 |  544.33 ± 21.93 |  594.96 ± 21.93 |
| nemotron-3-nano-4b-fp8 |  tg1024 (c1) |     42.06 ± 0.40 |     42.06 ± 0.40 |  44.67 ± 0.47 |     44.67 ± 0.47 |                 |                 |                 |
| nemotron-3-nano-4b-fp8 |  pp1024 (c5) | 4616.51 ± 372.49 | 1210.33 ± 344.67 |               |                  | 867.86 ± 191.60 | 817.22 ± 191.60 | 867.86 ± 191.60 |
| nemotron-3-nano-4b-fp8 |  tg1024 (c5) |   178.26 ± 20.47 |     40.69 ± 0.71 | 210.00 ± 0.00 |     43.33 ± 1.25 |                 |                 |                 |
| nemotron-3-nano-4b-fp8 | pp1024 (c10) |  7495.97 ± 71.00 | 1169.00 ± 396.53 |               |                  | 930.50 ± 251.62 | 879.86 ± 251.62 | 930.50 ± 251.62 |
| nemotron-3-nano-4b-fp8 | tg1024 (c10) |    308.16 ± 9.01 |     34.89 ± 0.91 | 357.00 ± 3.56 |     38.40 ± 1.38 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-08 09:26:46 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
