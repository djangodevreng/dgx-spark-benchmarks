# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-06-23 12:11:35
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model mistral-small-3.2-24b --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |    t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |           ttfr (ms) |        est_ppt (ms) |       e2e_ttft (ms) |
|:----------------------|-------------:|---------------:|----------------:|--------------:|-----------------:|--------------------:|--------------------:|--------------------:|
| mistral-small-3.2-24b |  pp8192 (c5) | 1175.79 ± 1.34 | 423.50 ± 208.40 |               |                  |  22974.21 ± 8227.12 |  22386.15 ± 8227.12 |  22974.21 ± 8227.12 |
| mistral-small-3.2-24b |   tg512 (c5) |   16.58 ± 1.34 |     7.38 ± 4.36 |  68.33 ± 2.36 |     14.40 ± 0.71 |                     |                     |                     |
| mistral-small-3.2-24b | pp8192 (c10) | 1176.70 ± 0.05 | 290.94 ± 227.23 |               |                  | 39892.65 ± 18878.06 | 39304.59 ± 18878.06 | 39892.65 ± 18878.06 |
| mistral-small-3.2-24b |  tg512 (c10) |   17.16 ± 4.64 |     4.58 ± 3.76 | 118.67 ± 1.89 |     13.30 ± 1.24 |                     |                     |                     |
| mistral-small-3.2-24b | pp8192 (c20) | 1172.86 ± 0.22 | 182.34 ± 191.89 |               |                  | 74809.77 ± 39333.32 | 74221.70 ± 39333.32 | 74809.77 ± 39333.32 |
| mistral-small-3.2-24b |  tg512 (c20) |   17.46 ± 1.34 |     2.90 ± 3.20 | 180.00 ± 0.00 |     11.42 ± 2.09 |                     |                     |                     |

llama-benchy (0.3.8)
date: 2026-06-23 11:50:18 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
