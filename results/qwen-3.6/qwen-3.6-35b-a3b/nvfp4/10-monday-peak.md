# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-14 08:56:55
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  667.93    
Total input tokens:                      1201174   
Total generated tokens:                  150317    
Request throughput (req/s):              0.45      
Output token throughput (tok/s):         225.05    
Peak output token throughput (tok/s):    350.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2023.40   
---------------Time to First Token----------------
Mean TTFT (ms):                          1268.91   
Median TTFT (ms):                        1074.28   
P50 TTFT (ms):                           1074.28   
P90 TTFT (ms):                           1897.18   
P95 TTFT (ms):                           2520.76   
P99 TTFT (ms):                           6501.61   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          106.03    
Median TPOT (ms):                        106.41    
P50 TPOT (ms):                           106.41    
P90 TPOT (ms):                           115.14    
P95 TPOT (ms):                           119.34    
P99 TPOT (ms):                           135.49    
---------------Inter-token Latency----------------
Mean ITL (ms):                           104.60    
Median ITL (ms):                         78.99     
P50 ITL (ms):                            78.99     
P90 ITL (ms):                            211.47    
P95 ITL (ms):                            350.84    
P99 ITL (ms):                            389.52    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          53557.64  
Median E2EL (ms):                        52260.67  
P50 E2EL (ms):                           52260.67  
P90 E2EL (ms):                           95488.85  
P95 E2EL (ms):                           99443.90  
P99 E2EL (ms):                           104839.21 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.
