# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-16 23:56:31
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-31B-IT-NVFP4 --tokenizer nvidia/Gemma-4-31B-IT-NVFP4 --served-model-name gemma-4-31b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1966.42   
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.03      
Output token throughput (tok/s):         106.44    
Peak output token throughput (tok/s):    196.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          134.76    
---------------Time to First Token----------------
Mean TTFT (ms):                          2207.02   
Median TTFT (ms):                        2147.32   
P50 TTFT (ms):                           2147.32   
P90 TTFT (ms):                           3174.23   
P95 TTFT (ms):                           3880.67   
P99 TTFT (ms):                           4730.41   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          280.20    
Median TPOT (ms):                        285.71    
P50 TPOT (ms):                           285.71    
P90 TPOT (ms):                           301.76    
P95 TPOT (ms):                           306.94    
P99 TPOT (ms):                           312.09    
---------------Inter-token Latency----------------
Mean ITL (ms):                           272.26    
Median ITL (ms):                         280.17    
P50 ITL (ms):                            280.17    
P90 ITL (ms):                            303.87    
P95 ITL (ms):                            308.74    
P99 ITL (ms):                            319.19    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1141878.23
Median E2EL (ms):                        1125250.50
P50 E2EL (ms):                           1125250.50
P90 E2EL (ms):                           1683312.16
P95 E2EL (ms):                           1806150.04
P99 E2EL (ms):                           1851452.32
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
