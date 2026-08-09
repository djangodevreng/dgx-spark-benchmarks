# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-07 09:24:20
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.5-0.8b-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model             |         test |           t/s (total) |             t/s (req) |       peak t/s |   peak t/s (req) |       ttfr (ms) |    est_ppt (ms) |   e2e_ttft (ms) |
|:------------------|-------------:|----------------------:|----------------------:|---------------:|-----------------:|----------------:|----------------:|----------------:|
| qwen3.5-0.8b-bf16 |  pp1024 (c1) | 275039.94 ± 158383.33 | 275039.94 ± 158383.33 |                |                  |    52.11 ± 7.23 |     7.55 ± 7.23 |    52.11 ± 7.23 |
| qwen3.5-0.8b-bf16 |  tg1024 (c1) |         116.03 ± 0.18 |         116.03 ± 0.18 |  117.00 ± 0.00 |    117.00 ± 0.00 |                 |                 |                 |
| qwen3.5-0.8b-bf16 |  pp1024 (c5) |      25360.95 ± 19.76 |   35314.59 ± 52660.15 |                |                  |  132.57 ± 48.13 |   88.01 ± 48.13 |  132.57 ± 48.13 |
| qwen3.5-0.8b-bf16 |  tg1024 (c5) |        406.37 ± 27.15 |         115.73 ± 1.75 |  575.00 ± 0.00 |    120.27 ± 3.68 |                 |                 |                 |
| qwen3.5-0.8b-bf16 | pp1024 (c10) |      25275.46 ± 92.37 |   12196.84 ± 20219.48 |                |                  | 233.62 ± 100.49 | 189.06 ± 100.49 | 233.62 ± 100.49 |
| qwen3.5-0.8b-bf16 | tg1024 (c10) |        563.69 ± 95.41 |        102.13 ± 11.34 | 985.00 ± 29.06 |   109.75 ± 13.23 |                 |                 |                 |

llama-benchy (0.4.0)
date: 2026-08-07 09:22:47 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
