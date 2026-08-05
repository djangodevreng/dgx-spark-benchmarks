# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-09 21:20:31
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  2445.28   
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         85.59     
Peak output token throughput (tok/s):    179.00    
Peak concurrent requests:                50.00     
Total token throughput (tok/s):          108.30    
---------------Time to First Token----------------
Mean TTFT (ms):                          1779.24   
Median TTFT (ms):                        1698.92   
P50 TTFT (ms):                           1698.92   
P90 TTFT (ms):                           2729.66   
P95 TTFT (ms):                           2865.55   
P99 TTFT (ms):                           3302.60   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          334.93    
Median TPOT (ms):                        339.86    
P50 TPOT (ms):                           339.86    
P90 TPOT (ms):                           348.10    
P95 TPOT (ms):                           351.90    
P99 TPOT (ms):                           355.49    
---------------Inter-token Latency----------------
Mean ITL (ms):                           345.61    
Median ITL (ms):                         338.49    
P50 ITL (ms):                            338.49    
P90 ITL (ms):                            346.81    
P95 ITL (ms):                            594.75    
P99 ITL (ms):                            696.31    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1379933.91
Median E2EL (ms):                        1328147.59
P50 E2EL (ms):                           1328147.59
P90 E2EL (ms):                           2096734.90
P95 E2EL (ms):                           2260695.90
P99 E2EL (ms):                           2318418.34
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
