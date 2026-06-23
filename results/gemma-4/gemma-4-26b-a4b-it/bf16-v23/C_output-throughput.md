# Run C — 1k prompt + 1k output, c=1/5/10

**Generated:** 2026-06-23 00:15:03
**Profile:** bf16-v23
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy --base-url http://localhost:8000/v1 --model gemma-4-26b-a4b --runs 3 --latency-mode generation --format md --pp 1024 --tg 1024 --depth 0 --concurrency 1 5 10
```

## Results

Printing results in MD format:



| model           |         test |      t/s (total) |        t/s (req) |      peak t/s |   peak t/s (req) |        ttfr (ms) |     est_ppt (ms) |    e2e_ttft (ms) |
|:----------------|-------------:|-----------------:|-----------------:|--------------:|-----------------:|-----------------:|-----------------:|-----------------:|
| gemma-4-26b-a4b |  pp1024 (c1) |  4215.41 ± 40.60 |  4215.41 ± 40.60 |               |                  |    315.36 ± 0.42 |    207.49 ± 0.42 |    315.36 ± 0.42 |
| gemma-4-26b-a4b |  tg1024 (c1) |     25.12 ± 0.01 |     25.12 ± 0.01 |  26.00 ± 0.00 |     26.00 ± 0.00 |                  |                  |                  |
| gemma-4-26b-a4b |  pp1024 (c5) |  5902.04 ± 41.68 |  1369.46 ± 51.86 |               |                  |   785.72 ± 12.29 |   677.85 ± 12.29 |   785.72 ± 12.29 |
| gemma-4-26b-a4b |  tg1024 (c5) |     60.78 ± 2.43 |     14.46 ± 0.71 |  83.33 ± 2.36 |     19.60 ± 3.83 |                  |                  |                  |
| gemma-4-26b-a4b | pp1024 (c10) | 5905.88 ± 254.83 | 1086.56 ± 970.37 |               |                  | 1342.98 ± 449.90 | 1235.11 ± 449.90 | 1342.98 ± 449.90 |
| gemma-4-26b-a4b | tg1024 (c10) |     90.83 ± 7.87 |     11.47 ± 0.45 | 133.33 ± 4.71 |     14.90 ± 2.01 |                  |                  |                  |

llama-benchy (0.3.8)
date: 2026-06-23 00:06:46 | latency mode: generation

---

Volledige log in `C_output-throughput.log`. Server-config in `meta.json`.
