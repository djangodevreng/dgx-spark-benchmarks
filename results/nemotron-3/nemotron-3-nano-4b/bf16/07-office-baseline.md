# Test 07-office-baseline — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 06:40:13
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename 07-office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  691.49    
Total input tokens:                      815936    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         140.41    
Peak output token throughput (tok/s):    328.00    
Peak concurrent requests:                15.00     
Total token throughput (tok/s):          1320.38   
---------------Time to First Token----------------
Mean TTFT (ms):                          847.49    
Median TTFT (ms):                        800.46    
P50 TTFT (ms):                           800.46    
P90 TTFT (ms):                           1423.28   
P95 TTFT (ms):                           1755.35   
P99 TTFT (ms):                           2406.02   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          46.25     
Median TPOT (ms):                        46.07     
P50 TPOT (ms):                           46.07     
P90 TPOT (ms):                           53.29     
P95 TPOT (ms):                           56.17     
P99 TPOT (ms):                           62.70     
---------------Inter-token Latency----------------
Mean ITL (ms):                           46.06     
Median ITL (ms):                         39.89     
P50 ITL (ms):                            39.89     
P90 ITL (ms):                            44.60     
P95 ITL (ms):                            51.53     
P99 ITL (ms):                            267.91    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          23208.44  
Median E2EL (ms):                        22720.22  
P50 E2EL (ms):                           22720.22  
P90 E2EL (ms):                           40290.63  
P95 E2EL (ms):                           43175.28  
P99 E2EL (ms):                           47619.97  
==================================================

---

Volledige log in `07-office-baseline.log`. Server-config in `meta.json`.
