# Test 01-chat — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-08-14 07:06:26
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model                 |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| qwen3.6-35b-a3b-nvfp4 |  pp1024 (c1) | 6486.84 ± 194.87 | 6486.84 ± 194.87 |               |                  |    206.88 ± 7.40 |    145.55 ± 7.40 |    206.88 ± 7.40 |
| qwen3.6-35b-a3b-nvfp4 |  tg1024 (c1) |     42.62 ± 0.27 |     42.62 ± 0.27 |  44.33 ± 0.47 |     44.33 ± 0.47 |                  |                  |                  |
| qwen3.6-35b-a3b-nvfp4 |  pp1024 (c5) | 5200.64 ± 292.54 | 1710.48 ± 901.25 |               |                  |  720.12 ± 214.75 |  658.79 ± 214.75 |  720.12 ± 214.75 |
| qwen3.6-35b-a3b-nvfp4 |  tg1024 (c5) |    133.38 ± 2.20 |     27.56 ± 0.43 | 151.67 ± 2.36 |     34.00 ± 4.07 |                  |                  |                  |
| qwen3.6-35b-a3b-nvfp4 | pp1024 (c10) | 5281.78 ± 169.38 | 1068.72 ± 737.30 |               |                  | 1214.18 ± 454.52 | 1152.86 ± 454.52 | 1214.18 ± 454.52 |
| qwen3.6-35b-a3b-nvfp4 | tg1024 (c10) |    196.13 ± 2.16 |     20.27 ± 0.35 | 233.33 ± 4.71 |     23.33 ± 0.47 |                  |                  |                  |

llama-benchy (0.4.0)
date: 2026-08-14 06:58:49 | latency mode: generation

---

Volledige log in `01-chat.log`. Server-config in `meta.json`.
