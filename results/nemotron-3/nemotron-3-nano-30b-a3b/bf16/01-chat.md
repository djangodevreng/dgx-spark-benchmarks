# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-09 02:51:19
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model nemotron-3-nano-30b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                    |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| nemotron-3-nano-30b-bf16 |  pp1024 (c1) | 2388.16 ± 372.88 | 2388.16 ± 372.88 |               |                  |   544.19 ± 77.91 |   398.46 ± 77.91 |   544.19 ± 77.91 |
| nemotron-3-nano-30b-bf16 |  tg1024 (c1) |     29.27 ± 0.03 |     29.27 ± 0.03 |  31.00 ± 0.82 |     31.00 ± 0.82 |                  |                  |                  |
| nemotron-3-nano-30b-bf16 |  pp1024 (c5) | 4101.50 ± 117.09 | 1408.48 ± 952.67 |               |                  |  995.66 ± 280.25 |  849.93 ± 280.25 |  995.66 ± 280.25 |
| nemotron-3-nano-30b-bf16 |  tg1024 (c5) |     54.60 ± 0.05 |     10.99 ± 0.04 |  66.67 ± 2.36 |     13.33 ± 0.47 |                  |                  |                  |
| nemotron-3-nano-30b-bf16 | pp1024 (c10) |  5096.37 ± 42.71 |  966.21 ± 914.84 |               |                  | 1505.80 ± 463.15 | 1360.07 ± 463.15 | 1505.80 ± 463.15 |
| nemotron-3-nano-30b-bf16 | tg1024 (c10) |     72.26 ± 0.68 |      7.64 ± 0.07 | 100.00 ± 0.00 |     10.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-09 02:33:35 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
