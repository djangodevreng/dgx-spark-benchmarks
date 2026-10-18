# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-10-17 23:34:26
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --served-model-name nemotron-3.5-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  737.25    
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.27      
Output token throughput (tok/s):         131.69    
Peak output token throughput (tok/s):    99.00     
Peak concurrent requests:                36.00     
Total token throughput (tok/s):          1238.42   
---------------Time to First Token----------------
Mean TTFT (ms):                          4526.33   
Median TTFT (ms):                        4170.73   
P50 TTFT (ms):                           4170.73   
P90 TTFT (ms):                           8312.47   
P95 TTFT (ms):                           9089.80   
P99 TTFT (ms):                           10631.30  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          163.21    
Median TPOT (ms):                        165.12    
P50 TPOT (ms):                           165.12    
P90 TPOT (ms):                           193.15    
P95 TPOT (ms):                           210.07    
P99 TPOT (ms):                           249.69    
---------------Inter-token Latency----------------
Mean ITL (ms):                           471.89    
Median ITL (ms):                         338.99    
P50 ITL (ms):                            338.99    
P90 ITL (ms):                            904.83    
P95 ITL (ms):                            916.91    
P99 ITL (ms):                            935.41    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          80790.03  
Median E2EL (ms):                        79796.96  
P50 E2EL (ms):                           79796.96  
P90 E2EL (ms):                           137328.81 
P95 E2EL (ms):                           148991.10 
P99 E2EL (ms):                           162340.91 
---------------Speculative Decoding---------------
Acceptance rate (%):                     67.13     
Acceptance length:                       3.01      
Drafts:                                  32227     
Draft tokens:                            96681     
Accepted tokens:                         64905     
Per-position acceptance (%):
  Position 0:                            82.64     
  Position 1:                            66.46     
  Position 2:                            52.30     
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.
