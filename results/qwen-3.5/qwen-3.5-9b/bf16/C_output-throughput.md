# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-09 14:48:24
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.5-9b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |     t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|-------------:|----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.5-9b-bf16 |  pp1024 (c1) | 6383.08 ± 57.64 |  6383.08 ± 57.64 |               |                  |    245.00 ± 7.77 |    147.07 ± 7.77 |    245.00 ± 7.77 |
| qwen3.5-9b-bf16 |  tg1024 (c1) |    12.65 ± 0.00 |     12.65 ± 0.00 |  13.00 ± 0.00 |     13.00 ± 0.00 |                  |                  |                  |
| qwen3.5-9b-bf16 |  pp1024 (c5) | 3988.12 ± 16.19 | 1553.28 ± 704.63 |               |                  |  820.00 ± 281.07 |  722.06 ± 281.07 |  820.00 ± 281.07 |
| qwen3.5-9b-bf16 |  tg1024 (c5) |    66.21 ± 0.01 |     13.31 ± 0.04 |  70.00 ± 0.00 |     14.00 ± 0.00 |                  |                  |                  |
| qwen3.5-9b-bf16 | pp1024 (c10) | 4001.58 ± 20.00 |  977.04 ± 701.85 |               |                  | 1470.43 ± 659.09 | 1372.50 ± 659.09 | 1470.43 ± 659.09 |
| qwen3.5-9b-bf16 | tg1024 (c10) |   125.55 ± 0.13 |     12.73 ± 0.09 | 136.67 ± 4.71 |     13.67 ± 0.47 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-09 14:36:12 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
