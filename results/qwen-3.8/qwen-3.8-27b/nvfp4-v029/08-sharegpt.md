# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-09-21 11:14:34
**Profile:** nvfp4-v029
**Model:** nvidia/Qwen3.8-27B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Qwen3.8-27B-NVFP4 --tokenizer nvidia/Qwen3.8-27B-NVFP4 --served-model-name qwen3.8-27b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  868.84    
Total input tokens:                      67729     
Total generated tokens:                  52272     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         60.16     
Peak output token throughput (tok/s):    159.00    
Peak concurrent requests:                17.00     
Total token throughput (tok/s):          138.12    
---------------Time to First Token----------------
Mean TTFT (ms):                          746.37    
Median TTFT (ms):                        637.50    
P50 TTFT (ms):                           637.50    
P90 TTFT (ms):                           1345.04   
P95 TTFT (ms):                           1572.72   
P99 TTFT (ms):                           1979.33   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          104.99    
Median TPOT (ms):                        102.61    
P50 TPOT (ms):                           102.61    
P90 TPOT (ms):                           116.76    
P95 TPOT (ms):                           127.66    
P99 TPOT (ms):                           210.27    
---------------Inter-token Latency----------------
Mean ITL (ms):                           102.71    
Median ITL (ms):                         92.14     
P50 ITL (ms):                            92.14     
P90 ITL (ms):                            105.83    
P95 ITL (ms):                            148.19    
P99 ITL (ms):                            474.79    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          22202.82  
Median E2EL (ms):                        13996.11  
P50 E2EL (ms):                           13996.11  
P90 E2EL (ms):                           52527.69  
P95 E2EL (ms):                           66216.46  
P99 E2EL (ms):                           88476.64  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.
