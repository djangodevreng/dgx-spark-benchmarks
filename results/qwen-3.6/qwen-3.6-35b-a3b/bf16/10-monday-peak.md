# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-08 15:01:32
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  1321.96   
Total input tokens:                      1201170   
Total generated tokens:                  150317    
Request throughput (req/s):              0.23      
Output token throughput (tok/s):         113.71    
Peak output token throughput (tok/s):    175.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          1022.33   
---------------Time to First Token----------------
Mean TTFT (ms):                          2318.00   
Median TTFT (ms):                        1849.48   
P50 TTFT (ms):                           1849.48   
P90 TTFT (ms):                           3162.23   
P95 TTFT (ms):                           5856.33   
P99 TTFT (ms):                           14857.21  
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          210.62    
Median TPOT (ms):                        212.24    
P50 TPOT (ms):                           212.24    
P90 TPOT (ms):                           222.40    
P95 TPOT (ms):                           228.02    
P99 TPOT (ms):                           243.51    
---------------Inter-token Latency----------------
Mean ITL (ms):                           208.21    
Median ITL (ms):                         176.72    
P50 ITL (ms):                            176.72    
P90 ITL (ms):                            355.23    
P95 ITL (ms):                            544.17    
P99 ITL (ms):                            587.06    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          106518.69 
Median E2EL (ms):                        103852.06 
P50 E2EL (ms):                           103852.06 
P90 E2EL (ms):                           188843.20 
P95 E2EL (ms):                           195927.77 
P99 E2EL (ms):                           206628.24 
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.
