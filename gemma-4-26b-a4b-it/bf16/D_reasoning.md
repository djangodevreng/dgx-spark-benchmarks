# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-05 21:16:50
**Profile:** bf16
**Model:** google/gemma-4-26B-A4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-26B-A4B-it --tokenizer google/gemma-4-26B-A4B-it --served-model-name gemma-4-26b-a4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1023.58   
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.05      
Output token throughput (tok/s):         204.48    
Peak output token throughput (tok/s):    336.00    
Peak concurrent requests:                48.00     
Total token throughput (tok/s):          258.88    
---------------Time to First Token----------------
Mean TTFT (ms):                          697.88    
Median TTFT (ms):                        619.57    
P50 TTFT (ms):                           619.57    
P90 TTFT (ms):                           789.54    
P95 TTFT (ms):                           1308.75   
P99 TTFT (ms):                           2101.76   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          134.87    
Median TPOT (ms):                        136.13    
P50 TPOT (ms):                           136.13    
P90 TPOT (ms):                           152.57    
P95 TPOT (ms):                           153.39    
P99 TPOT (ms):                           155.33    
---------------Inter-token Latency----------------
Mean ITL (ms):                           131.00    
Median ITL (ms):                         132.44    
P50 ITL (ms):                            132.44    
P90 ITL (ms):                            157.54    
P95 ITL (ms):                            163.64    
P99 ITL (ms):                            179.39    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          549084.33 
Median E2EL (ms):                        555975.03 
P50 E2EL (ms):                           555975.03 
P90 E2EL (ms):                           801331.84 
P95 E2EL (ms):                           870190.98 
P99 E2EL (ms):                           901537.12 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
