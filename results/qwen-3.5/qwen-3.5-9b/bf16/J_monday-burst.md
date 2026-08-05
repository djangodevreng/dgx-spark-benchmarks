# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-05-09 16:49:44
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  887.43    
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.34      
Output token throughput (tok/s):         169.38    
Peak output token throughput (tok/s):    276.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1522.92   
---------------Time to First Token----------------
Mean TTFT (ms):                          2046.04   
Median TTFT (ms):                        1616.62   
P50 TTFT (ms):                           1616.62   
P90 TTFT (ms):                           3078.76   
P95 TTFT (ms):                           5000.04   
P99 TTFT (ms):                           13295.77  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          139.06    
Median TPOT (ms):                        138.92    
P50 TPOT (ms):                           138.92    
P90 TPOT (ms):                           151.70    
P95 TPOT (ms):                           158.25    
P99 TPOT (ms):                           185.17    
---------------Inter-token Latency----------------
Mean ITL (ms):                           137.10    
Median ITL (ms):                         96.24     
P50 ITL (ms):                            96.24     
P90 ITL (ms):                            207.63    
P95 ITL (ms):                            553.60    
P99 ITL (ms):                            568.01    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          70697.59  
Median E2EL (ms):                        68526.63  
P50 E2EL (ms):                           68526.63  
P90 E2EL (ms):                           124721.74 
P95 E2EL (ms):                           130065.20 
P99 E2EL (ms):                           137393.45 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.
