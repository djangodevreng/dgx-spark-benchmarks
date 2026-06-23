# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-06-23 04:25:59
**Profile:** mtp-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b-mtp --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model               |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:--------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b-mtp |  pp1024 (c1) | 4056.06 ± 179.21 | 4056.06 ± 179.21 |               |                  |    386.16 ± 3.33 |    234.73 ± 3.33 |    386.16 ± 3.33 |
| gemma-4-26b-a4b-mtp |  tg1024 (c1) |     32.54 ± 2.88 |     32.54 ± 2.88 |  45.00 ± 3.74 |     45.00 ± 3.74 |                  |                  |                  |
| gemma-4-26b-a4b-mtp |  pp1024 (c5) | 4978.92 ± 394.40 | 1442.88 ± 598.51 |               |                  |  853.61 ± 161.46 |  702.18 ± 161.46 |  853.61 ± 161.46 |
| gemma-4-26b-a4b-mtp |  tg1024 (c5) |     89.68 ± 4.55 |     22.33 ± 2.53 | 133.33 ± 2.05 |     35.80 ± 5.62 |                  |                  |                  |
| gemma-4-26b-a4b-mtp | pp1024 (c10) |  5551.25 ± 16.45 |   758.33 ± 84.94 |               |                  | 1400.13 ± 142.07 | 1248.70 ± 142.07 | 1400.13 ± 142.07 |
| gemma-4-26b-a4b-mtp | tg1024 (c10) |    138.97 ± 6.68 |     17.79 ± 1.55 | 205.67 ± 2.05 |     29.90 ± 4.75 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-23 04:20:05 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
