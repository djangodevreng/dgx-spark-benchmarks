# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-06 01:51:06
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-31b --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model       |         test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:------------|-------------:|-----------------:|-----------------:|-------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-31b |  pp1024 (c1) | 1449.72 ± 274.54 | 1449.72 ± 274.54 |              |                  | 1066.20 ± 109.89 |  682.08 ± 109.89 | 1066.20 ± 109.89 |
| gemma-4-31b |  tg1024 (c1) |      3.72 ± 0.00 |      3.72 ± 0.00 |  4.00 ± 0.00 |      4.00 ± 0.00 |                  |                  |                  |
| gemma-4-31b |  pp1024 (c5) |  1132.00 ± 10.61 |   250.00 ± 10.80 |              |                  |  4079.49 ± 25.21 |  3695.37 ± 25.21 |  4079.49 ± 25.21 |
| gemma-4-31b |  tg1024 (c5) |     12.60 ± 0.14 |      3.54 ± 0.03 | 20.00 ± 0.00 |      4.00 ± 0.00 |                  |                  |                  |
| gemma-4-31b | pp1024 (c10) |   1168.83 ± 9.45 |    136.94 ± 8.69 |              |                  | 7194.20 ± 381.27 | 6810.08 ± 381.27 | 7194.20 ± 381.27 |
| gemma-4-31b | tg1024 (c10) |     20.03 ± 1.65 |      3.40 ± 0.09 | 40.00 ± 0.00 |      4.00 ± 0.00 |                  |                  |                  |

llama-benchy (0.3.7)
date: 2026-05-06 01:29:15 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
