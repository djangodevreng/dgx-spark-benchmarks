# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-05-04 14:28:56
**Profile:** fp8
**Model:** Qwen/Qwen3.6-27B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-27b-fp8 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |        t/s (req) |     peak t/s |   peak t/s (req) |         ttfr (ms) |      est_ppt (ms) |     e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|-----------------:|-------------:|-----------------:|------------------:|------------------:|------------------:|
| qwen3.6-27b-fp8 |  pp1024 (c1) | 2166.06 ± 537.09 | 2166.06 ± 537.09 |              |                  |    614.77 ± 89.34 |    458.02 ± 89.34 |    614.77 ± 89.34 |
| qwen3.6-27b-fp8 |  tg1024 (c1) |      7.83 ± 0.02 |      7.83 ± 0.02 |  8.33 ± 0.47 |      8.33 ± 0.47 |                   |                   |                   |
| qwen3.6-27b-fp8 |  pp1024 (c5) | 1661.85 ± 241.17 |  510.10 ± 176.43 |              |                  |  2188.39 ± 664.23 |  2031.63 ± 664.23 |  2188.39 ± 664.23 |
| qwen3.6-27b-fp8 |  tg1024 (c5) |     37.18 ± 0.20 |      7.49 ± 0.04 | 40.00 ± 0.00 |      8.00 ± 0.00 |                   |                   |                   |
| qwen3.6-27b-fp8 | pp1024 (c10) | 1573.58 ± 402.46 |  288.42 ± 176.19 |              |                  | 4477.44 ± 2181.48 | 4320.69 ± 2181.48 | 4477.44 ± 2181.48 |
| qwen3.6-27b-fp8 | tg1024 (c10) |     68.54 ± 0.51 |      7.00 ± 0.07 | 80.00 ± 0.00 |      8.00 ± 0.00 |                   |                   |                   |

llama-benchy (0.3.7)
date: 2026-05-04 14:07:39 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
