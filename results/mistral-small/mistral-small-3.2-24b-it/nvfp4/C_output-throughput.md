# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-06-23 11:41:55
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model mistral-small-3.2-24b --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| mistral-small-3.2-24b |  pp1024 (c1) | 1146.32 ± 90.38 | 1146.32 ± 90.38 |               |                  |   929.64 ± 28.59 |   342.47 ± 28.59 |   929.64 ± 28.59 |
| mistral-small-3.2-24b |  tg1024 (c1) |    15.39 ± 0.00 |    15.39 ± 0.00 |  16.00 ± 0.00 |     16.00 ± 0.00 |                  |                  |                  |
| mistral-small-3.2-24b |  pp1024 (c5) |   463.91 ± 4.10 |   107.86 ± 1.11 |               |                  |  4203.20 ± 37.16 |  3616.04 ± 37.16 |  4203.20 ± 37.16 |
| mistral-small-3.2-24b |  tg1024 (c5) |    34.63 ± 6.35 |    15.45 ± 0.08 |  80.00 ± 0.00 |     16.00 ± 0.00 |                  |                  |                  |
| mistral-small-3.2-24b | pp1024 (c10) |   474.93 ± 1.95 |    61.18 ± 5.01 |               |                  | 7011.14 ± 600.18 | 6423.97 ± 600.18 | 7011.14 ± 600.18 |
| mistral-small-3.2-24b | tg1024 (c10) |   63.13 ± 19.47 |    12.63 ± 1.56 | 150.00 ± 0.00 |     15.67 ± 0.47 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-23 11:37:40 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
