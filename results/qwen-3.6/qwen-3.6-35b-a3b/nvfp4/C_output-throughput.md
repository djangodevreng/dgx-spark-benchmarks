# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-06-26 07:13:35
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |    est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|----------------:|-----------------:|
| qwen3.6-35b-a3b-nvfp4 |  pp1024 (c1) | 7840.94 ± 240.91 | 7840.94 ± 240.91 |               |                  |    186.03 ± 7.16 |   122.70 ± 7.16 |    186.03 ± 7.16 |
| qwen3.6-35b-a3b-nvfp4 |  tg1024 (c1) |     40.57 ± 0.07 |     40.57 ± 0.07 |  42.00 ± 0.00 |     42.00 ± 0.00 |                  |                 |                  |
| qwen3.6-35b-a3b-nvfp4 |  pp1024 (c5) |  6209.87 ± 22.45 | 1814.31 ± 432.69 |               |                  |  606.54 ± 122.04 | 543.21 ± 122.04 |  606.54 ± 122.04 |
| qwen3.6-35b-a3b-nvfp4 |  tg1024 (c5) |    125.57 ± 0.63 |     25.22 ± 0.14 | 140.00 ± 0.00 |     28.00 ± 0.00 |                  |                 |                  |
| qwen3.6-35b-a3b-nvfp4 | pp1024 (c10) |  6276.81 ± 34.03 | 1158.98 ± 588.96 |               |                  | 1025.80 ± 357.09 | 962.47 ± 357.09 | 1025.80 ± 357.09 |
| qwen3.6-35b-a3b-nvfp4 | tg1024 (c10) |    188.83 ± 1.56 |     19.10 ± 0.20 | 226.67 ± 4.71 |     22.67 ± 0.47 |                  |                 |                  |

llama-benchy (0.3.8)
date: 2026-06-26 07:05:39 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
