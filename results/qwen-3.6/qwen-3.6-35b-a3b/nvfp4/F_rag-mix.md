# Run F — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-06-26 07:39:30
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model qwen3.6-35b-a3b-nvfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model                 |         test |     t/s (total) |         t/s (req) |      peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:----------------------|-------------:|----------------:|------------------:|--------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| qwen3.6-35b-a3b-nvfp4 |  pp8192 (c5) | 6294.49 ± 34.07 | 2595.65 ± 1474.34 |               |                  |  3764.05 ± 1589.56 |  3704.59 ± 1589.56 |  3764.05 ± 1589.56 |
| qwen3.6-35b-a3b-nvfp4 |   tg512 (c5) |    98.46 ± 0.24 |      21.89 ± 1.34 | 125.00 ± 0.00 |     26.13 ± 1.45 |                    |                    |                    |
| qwen3.6-35b-a3b-nvfp4 | pp8192 (c10) |  6029.35 ± 7.09 | 1647.33 ± 1314.82 |               |                  |  6876.51 ± 3470.66 |  6817.04 ± 3470.66 |  6876.51 ± 3470.66 |
| qwen3.6-35b-a3b-nvfp4 |  tg512 (c10) |   128.67 ± 0.25 |      15.25 ± 1.41 | 186.67 ± 4.71 |     21.73 ± 3.26 |                    |                    |                    |
| qwen3.6-35b-a3b-nvfp4 | pp8192 (c20) |  5415.65 ± 7.74 |  973.15 ± 1044.61 |               |                  | 13884.96 ± 7871.54 | 13825.49 ± 7871.54 | 13884.96 ± 7871.54 |
| qwen3.6-35b-a3b-nvfp4 |  tg512 (c20) |   161.88 ± 0.28 |      10.56 ± 1.53 | 280.00 ± 0.00 |     18.37 ± 4.22 |                    |                    |                    |

llama-benchy (0.3.8)
date: 2026-06-26 07:30:33 | latency mode: generation

---

Volledige log in `F_rag-mix.log`. Server-config in `meta.json`.
