# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-07 03:08:25
**Profile:** bf16
**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model ministral-3-8b-instruct-bf16 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                        |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:-----------------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| ministral-3-8b-instruct-bf16 |  pp1024 (c1) | 2040.29 ± 772.56 | 2040.29 ± 772.56 |               |                  |  626.29 ± 285.89 |  551.59 ± 285.89 |  626.29 ± 285.89 |
| ministral-3-8b-instruct-bf16 |  tg1024 (c1) |     25.10 ± 0.17 |     25.10 ± 0.17 |  26.00 ± 0.00 |     26.00 ± 0.00 |                  |                  |                  |
| ministral-3-8b-instruct-bf16 |  pp1024 (c5) |  4448.88 ± 64.82 | 1106.47 ± 288.48 |               |                  |  941.00 ± 142.93 |  866.29 ± 142.93 |  941.00 ± 142.93 |
| ministral-3-8b-instruct-bf16 |  tg1024 (c5) |    105.40 ± 8.13 |     25.20 ± 0.19 | 130.00 ± 0.00 |     26.27 ± 0.44 |                  |                  |                  |
| ministral-3-8b-instruct-bf16 | pp1024 (c10) | 6678.61 ± 168.80 |  967.55 ± 699.18 |               |                  | 1247.63 ± 286.04 | 1172.93 ± 286.04 | 1247.63 ± 286.04 |
| ministral-3-8b-instruct-bf16 | tg1024 (c10) |    183.89 ± 2.62 |     24.00 ± 0.29 | 250.00 ± 0.00 |     25.40 ± 0.49 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-07 03:00:00 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
