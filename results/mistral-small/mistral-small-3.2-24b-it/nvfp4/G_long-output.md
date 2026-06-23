# Run G — 256 prompt + 4096 output, c=1/5/10

**Generated:** 2026-06-23 12:12:55
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model mistral-small-3.2-24b --runs 3 --latency-mode generation --format md --pp 256 --tg 4096 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |   t/s (total) |    t/s (req) |      peak t/s |   peak t/s (req) |      ttfr (ms) |   est_ppt (ms) |   e2e_ttft (ms) |
|:----------------------|-------------:|--------------:|-------------:|--------------:|-----------------:|---------------:|---------------:|----------------:|
| mistral-small-3.2-24b |   pp256 (c1) |  28.72 ± 0.97 | 28.72 ± 0.97 |               |                  |  625.04 ± 1.21 |   34.86 ± 1.21 |   625.04 ± 1.21 |
| mistral-small-3.2-24b |  tg4096 (c1) |  15.40 ± 0.02 | 15.40 ± 0.02 |  16.44 ± 0.63 |     16.44 ± 0.63 |                |                |                 |
| mistral-small-3.2-24b |   pp256 (c5) |   1.89 ± 0.00 |  0.49 ± 0.00 |               |                  | 2646.49 ± 1.34 | 2056.31 ± 1.34 |  2646.49 ± 1.34 |
| mistral-small-3.2-24b |  tg4096 (c5) |  42.96 ± 4.09 | 15.59 ± 0.07 |  67.67 ± 5.73 |     16.55 ± 0.62 |                |                |                 |
| mistral-small-3.2-24b |  pp256 (c10) |   1.92 ± 0.00 |  0.22 ± 0.00 |               |                  | 5201.33 ± 1.99 | 4611.15 ± 1.99 |  5201.33 ± 1.99 |
| mistral-small-3.2-24b | tg4096 (c10) |  80.24 ± 6.97 | 15.26 ± 0.14 | 135.67 ± 9.18 |     16.35 ± 0.41 |                |                |                 |

llama-benchy (0.3.8)
date: 2026-06-23 12:11:36 | latency mode: generation

---

Volledige log in `G_long-output.log`. Server-config in `meta.json`.
