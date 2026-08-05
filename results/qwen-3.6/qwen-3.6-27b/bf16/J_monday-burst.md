# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-10 01:58:14
**Profile:** bf16
**Model:** Qwen/Qwen3.6-27B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-27B --tokenizer Qwen/Qwen3.6-27B --served-model-name qwen3.6-27b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  2873.64   
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         52.31     
Peak output token throughput (tok/s):    101.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          470.30    
---------------Time to First Token----------------
Mean TTFT (ms):                          7818.31   
Median TTFT (ms):                        5357.27   
P50 TTFT (ms):                           5357.27   
P90 TTFT (ms):                           9866.39   
P95 TTFT (ms):                           23659.27  
P99 TTFT (ms):                           65606.62  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          451.40    
Median TPOT (ms):                        452.08    
P50 TPOT (ms):                           452.08    
P90 TPOT (ms):                           492.33    
P95 TPOT (ms):                           516.27    
P99 TPOT (ms):                           593.38    
---------------Inter-token Latency----------------
Mean ITL (ms):                           447.67    
Median ITL (ms):                         308.74    
P50 ITL (ms):                            308.74    
P90 ITL (ms):                            976.44    
P95 ITL (ms):                            1685.85   
P99 ITL (ms):                            1840.63   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          230858.61 
Median E2EL (ms):                        222899.14 
P50 E2EL (ms):                           222899.14 
P90 E2EL (ms):                           406989.49 
P95 E2EL (ms):                           424013.04 
P99 E2EL (ms):                           455972.99 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.
