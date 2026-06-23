# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 12:46:14
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4 --tokenizer RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4 --served-model-name mistral-small-3.2-24b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  870.88    
Total input tokens:                      216757    
Total generated tokens:                  50428     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         57.90     
Peak output token throughput (tok/s):    180.00    
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          306.80    
---------------Time to First Token----------------
Mean TTFT (ms):                          1260.05   
Median TTFT (ms):                        1004.29   
P50 TTFT (ms):                           1004.29   
P90 TTFT (ms):                           2242.49   
P95 TTFT (ms):                           2546.56   
P99 TTFT (ms):                           3322.16   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          90.97     
Median TPOT (ms):                        82.74     
P50 TPOT (ms):                           82.74     
P90 TPOT (ms):                           112.99    
P95 TPOT (ms):                           131.86    
P99 TPOT (ms):                           272.86    
---------------Inter-token Latency----------------
Mean ITL (ms):                           84.37     
Median ITL (ms):                         65.83     
P50 ITL (ms):                            65.83     
P90 ITL (ms):                            68.36     
P95 ITL (ms):                            69.14     
P99 ITL (ms):                            797.53    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          18279.04  
Median E2EL (ms):                        11878.34  
P50 E2EL (ms):                           11878.34  
P90 E2EL (ms):                           44525.19  
P95 E2EL (ms):                           51523.28  
P99 E2EL (ms):                           64056.52  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.
