# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-08 10:30:38
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  833.89    
Total input tokens:                      58416     
Total generated tokens:                  51878     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         62.21     
Peak output token throughput (tok/s):    266.00    
Peak concurrent requests:                8.00      
Total token throughput (tok/s):          132.26    
---------------Time to First Token----------------
Mean TTFT (ms):                          157.31    
Median TTFT (ms):                        107.44    
P50 TTFT (ms):                           107.44    
P90 TTFT (ms):                           403.15    
P95 TTFT (ms):                           477.89    
P99 TTFT (ms):                           675.55    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          23.49     
Median TPOT (ms):                        23.33     
P50 TPOT (ms):                           23.33     
P90 TPOT (ms):                           24.87     
P95 TPOT (ms):                           25.55     
P99 TPOT (ms):                           27.50     
---------------Inter-token Latency----------------
Mean ITL (ms):                           23.37     
Median ITL (ms):                         23.00     
P50 ITL (ms):                            23.00     
P90 ITL (ms):                            24.98     
P95 ITL (ms):                            25.87     
P99 ITL (ms):                            35.38     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          5006.80   
Median E2EL (ms):                        3194.98   
P50 E2EL (ms):                           3194.98   
P90 E2EL (ms):                           11829.57  
P95 E2EL (ms):                           15055.98  
P99 E2EL (ms):                           19393.28  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.
