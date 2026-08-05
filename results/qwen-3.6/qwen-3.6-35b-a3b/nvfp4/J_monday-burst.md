# Run J — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-06-26 08:42:16
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename J_monday-burst.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  733.10    
Total input tokens:                      1201174   
Total generated tokens:                  150317    
Request throughput (req/s):              0.41      
Output token throughput (tok/s):         205.04    
Peak output token throughput (tok/s):    325.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1843.53   
---------------Time to First Token----------------
Mean TTFT (ms):                          1442.20   
Median TTFT (ms):                        1308.41   
P50 TTFT (ms):                           1308.41   
P90 TTFT (ms):                           2057.72   
P95 TTFT (ms):                           2540.96   
P99 TTFT (ms):                           6637.90   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          116.16    
Median TPOT (ms):                        117.24    
P50 TPOT (ms):                           117.24    
P90 TPOT (ms):                           126.11    
P95 TPOT (ms):                           131.89    
P99 TPOT (ms):                           152.92    
---------------Inter-token Latency----------------
Mean ITL (ms):                           115.42    
Median ITL (ms):                         83.89     
P50 ITL (ms):                            83.89     
P90 ITL (ms):                            255.88    
P95 ITL (ms):                            383.89    
P99 ITL (ms):                            432.95    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          58879.45  
Median E2EL (ms):                        57229.86  
P50 E2EL (ms):                           57229.86  
P90 E2EL (ms):                           105465.04 
P95 E2EL (ms):                           109496.05 
P99 E2EL (ms):                           115562.91 
==================================================

---

Volledige log in `J_monday-burst.log`. Server-config in `meta.json`.
