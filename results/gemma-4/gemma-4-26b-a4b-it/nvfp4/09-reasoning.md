# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-16 17:11:42
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  676.39    
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         309.44    
Peak output token throughput (tok/s):    516.00    
Peak concurrent requests:                44.00     
Total token throughput (tok/s):          391.77    
---------------Time to First Token----------------
Mean TTFT (ms):                          345.74    
Median TTFT (ms):                        342.89    
P50 TTFT (ms):                           342.89    
P90 TTFT (ms):                           457.62    
P95 TTFT (ms):                           492.30    
P99 TTFT (ms):                           550.73    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          73.84     
Median TPOT (ms):                        74.86     
P50 TPOT (ms):                           74.86     
P90 TPOT (ms):                           83.14     
P95 TPOT (ms):                           83.67     
P99 TPOT (ms):                           87.58     
---------------Inter-token Latency----------------
Mean ITL (ms):                           73.08     
Median ITL (ms):                         74.59     
P50 ITL (ms):                            74.59     
P90 ITL (ms):                            90.08     
P95 ITL (ms):                            91.23     
P99 ITL (ms):                            93.29     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          306255.35 
Median E2EL (ms):                        309911.58 
P50 E2EL (ms):                           309911.58 
P90 E2EL (ms):                           463540.75 
P95 E2EL (ms):                           508282.32 
P99 E2EL (ms):                           525613.49 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
