# Run E — depth=4 (5 turns), 2k startcontext, c=1/5/10

**Generated:** 2026-06-23 11:50:17
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model mistral-small-3.2-24b --runs 3 --latency-mode generation --format md --pp 2048 --tg 512 --depth 4 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |              test |     t/s (total) |       t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------|------------------:|----------------:|----------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| mistral-small-3.2-24b |  pp2048 @ d4 (c1) | 1742.86 ± 40.02 | 1742.86 ± 40.02 |               |                  |    1707.06 ± 39.86 |    1120.43 ± 39.86 |    1707.06 ± 39.86 |
| mistral-small-3.2-24b |   tg512 @ d4 (c1) |    15.30 ± 0.00 |    15.30 ± 0.00 |  16.00 ± 0.00 |     16.00 ± 0.00 |                    |                    |                    |
| mistral-small-3.2-24b |  pp2048 @ d4 (c5) |  1205.95 ± 0.37 |  322.14 ± 68.29 |               |                  |  7007.68 ± 1101.97 |  6421.05 ± 1101.97 |  7007.68 ± 1101.97 |
| mistral-small-3.2-24b |   tg512 @ d4 (c5) |    60.90 ± 4.77 |    14.34 ± 0.67 |  75.00 ± 0.00 |     15.80 ± 0.40 |                    |                    |                    |
| mistral-small-3.2-24b | pp2048 @ d4 (c10) |  1211.48 ± 5.02 |  181.47 ± 65.12 |               |                  | 12382.24 ± 3167.85 | 11795.62 ± 3167.85 | 12382.24 ± 3167.85 |
| mistral-small-3.2-24b |  tg512 @ d4 (c10) |    94.20 ± 3.92 |    12.67 ± 1.23 | 150.00 ± 0.00 |     15.27 ± 0.44 |                    |                    |                    |

llama-benchy (0.3.8)
date: 2026-06-23 11:41:56 | latency mode: generation

---

Volledige log in `E_multi-turn.log`. Server-config in `meta.json`.
