# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-10-17 23:48:29
**Profile:** nvfp4-v031
**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 --served-model-name nemotron-3.5-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  832.20    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.06      
Output token throughput (tok/s):         251.51    
Peak output token throughput (tok/s):    135.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          318.56    
---------------Time to First Token----------------
Mean TTFT (ms):                          1236.50   
Median TTFT (ms):                        1192.50   
P50 TTFT (ms):                           1192.50   
P90 TTFT (ms):                           1706.15   
P95 TTFT (ms):                           1754.12   
P99 TTFT (ms):                           2034.19   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          108.93    
Median TPOT (ms):                        107.78    
P50 TPOT (ms):                           107.78    
P90 TPOT (ms):                           133.05    
P95 TPOT (ms):                           141.76    
P99 TPOT (ms):                           146.65    
---------------Inter-token Latency----------------
Mean ITL (ms):                           387.40    
Median ITL (ms):                         385.52    
P50 ITL (ms):                            385.52    
P90 ITL (ms):                            432.91    
P95 ITL (ms):                            435.66    
P99 ITL (ms):                            687.03    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          436725.53 
Median E2EL (ms):                        440221.15 
P50 E2EL (ms):                           440221.15 
P90 E2EL (ms):                           635705.93 
P95 E2EL (ms):                           682839.11 
P99 E2EL (ms):                           727127.59 
---------------Speculative Decoding---------------
Acceptance rate (%):                     85.65     
Acceptance length:                       3.57      
Drafts:                                  58642     
Draft tokens:                            175926    
Accepted tokens:                         150684    
Per-position acceptance (%):
  Position 0:                            92.09     
  Position 1:                            85.53     
  Position 2:                            79.34     
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
