# Run B — 25k context, c=5/10/20

**Generated:** 2026-06-23 11:37:40
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model mistral-small-3.2-24b --runs 3 --latency-mode generation --format md --pp 25000 --tg 256 --depth 0 --concurrency 5 10 20 --exit-on-first-fail
```

## Results

Printing results in MD format:



| model                 |          test |    t/s (total) |       t/s (req) |     peak t/s |   peak t/s (req) |             ttfr (ms) |          est_ppt (ms) |         e2e_ttft (ms) |
|:----------------------|--------------:|---------------:|----------------:|-------------:|-----------------:|----------------------:|----------------------:|----------------------:|
| mistral-small-3.2-24b |  pp25000 (c5) | 1076.41 ± 0.29 | 456.63 ± 272.61 |              |                  |   69793.73 ± 30712.47 |   69207.98 ± 30712.47 |   69794.03 ± 30712.09 |
| mistral-small-3.2-24b |    tg256 (c5) |    4.16 ± 0.77 |     3.49 ± 3.72 | 50.00 ± 0.00 |     11.87 ± 1.50 |                       |                       |                       |
| mistral-small-3.2-24b | pp25000 (c10) | 1074.90 ± 0.32 | 294.75 ± 253.99 |              |                  |  126906.55 ± 64166.20 |  126320.80 ± 64166.20 |  126906.99 ± 64166.38 |
| mistral-small-3.2-24b |   tg256 (c10) |    4.26 ± 0.87 |     1.85 ± 2.59 | 80.00 ± 0.00 |     10.13 ± 2.03 |                       |                       |                       |
| mistral-small-3.2-24b | pp25000 (c20) | 1066.86 ± 2.14 | 181.75 ± 210.47 |              |                  | 239203.31 ± 128617.52 | 238617.56 ± 128617.52 | 239210.74 ± 128623.05 |
| mistral-small-3.2-24b |   tg256 (c20) |    4.51 ± 0.71 |     0.97 ± 1.57 | 93.33 ± 2.49 |      7.43 ± 3.13 |                       |                       |                       |

llama-benchy (0.3.8)
date: 2026-06-23 10:41:24 | latency mode: generation

---

Volledige log in `B_concurrency-stress.log`. Server-config in `meta.json`.
