# Test 02-rag-8k — 8k prompt + 512 output, c=5/10/20

**Generated:** 2026-08-14 11:58:48
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** llama

## Command

```bash
PYTHONUNBUFFERED=1 stdbuf -oL -eL uvx llama-benchy==0.4.0 --base-url http://localhost:8000/v1 --model gpt-oss-20b-mxfp4 --runs 3 --latency-mode generation --format md --pp 8192 --tg 512 --depth 0 --concurrency 5 10 20
```

## Results

Printing results in MD format:



| model             |         test |       t/s (total) |         t/s (req) |       peak t/s |   peak t/s (req) |          ttfr (ms) |       est_ppt (ms) |      e2e_ttft (ms) |
|:------------------|-------------:|------------------:|------------------:|---------------:|-----------------:|-------------------:|-------------------:|-------------------:|
| gpt-oss-20b-mxfp4 |  pp8192 (c5) |  6948.03 ± 135.73 | 3332.20 ± 2088.48 |                |                  |  3287.77 ± 1473.58 |  2983.71 ± 1444.47 |   5051.45 ± 291.42 |
| gpt-oss-20b-mxfp4 |   tg512 (c5) |    108.11 ± 30.06 |      28.42 ± 1.39 | 134.00 ± 24.78 |     31.08 ± 1.49 |                    |                    |                    |
| gpt-oss-20b-mxfp4 | pp8192 (c10) | 4920.40 ± 1614.68 | 1971.14 ± 1786.22 |                |                  |  6112.75 ± 3046.22 |  5900.65 ± 3001.98 |  9186.41 ± 3713.74 |
| gpt-oss-20b-mxfp4 |  tg512 (c10) |    162.14 ± 15.13 |      22.03 ± 1.87 | 224.67 ± 20.42 |     24.25 ± 6.48 |                    |                    |                    |
| gpt-oss-20b-mxfp4 | pp8192 (c20) | 5636.24 ± 1881.09 | 1207.31 ± 1471.83 |                |                  | 11302.77 ± 5994.38 | 11086.74 ± 5941.34 | 15136.87 ± 8236.21 |
| gpt-oss-20b-mxfp4 |  tg512 (c20) |     207.87 ± 9.58 |      14.72 ± 3.00 | 362.67 ± 31.48 |     19.34 ± 3.85 |                    |                    |                    |

llama-benchy (0.4.0)
date: 2026-08-14 11:51:54 | latency mode: generation

---

Volledige log in `02-rag-8k.log`. Server-config in `meta.json`.
