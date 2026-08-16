# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-13 15:07:29
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --served-model-name nemotron-3-nano-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  498.14    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         420.17    
Peak output token throughput (tok/s):    680.00    
Peak concurrent requests:                42.00     
Total token throughput (tok/s):          532.19    
---------------Time to First Token----------------
Mean TTFT (ms):                          481.20    
Median TTFT (ms):                        454.88    
P50 TTFT (ms):                           454.88    
P90 TTFT (ms):                           610.69    
P95 TTFT (ms):                           768.42    
P99 TTFT (ms):                           1488.93   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          52.62     
Median TPOT (ms):                        53.25     
P50 TPOT (ms):                           53.25     
P90 TPOT (ms):                           62.61     
P95 TPOT (ms):                           64.28     
P99 TPOT (ms):                           66.57     
---------------Inter-token Latency----------------
Mean ITL (ms):                           50.78     
Median ITL (ms):                         49.98     
P50 ITL (ms):                            49.98     
P90 ITL (ms):                            66.05     
P95 ITL (ms):                            69.90     
P99 ITL (ms):                            82.35     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          212960.10 
Median E2EL (ms):                        224682.25 
P50 E2EL (ms):                           224682.25 
P90 E2EL (ms):                           321065.36 
P95 E2EL (ms):                           344357.71 
P99 E2EL (ms):                           367756.88 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
