# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-06 02:39:16
**Profile:** no-prefix-cache
**Model:** google/gemma-4-31B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-31B-it --tokenizer google/gemma-4-31B-it --served-model-name gemma-4-31b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  2861.10   
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         73.15     
Peak output token throughput (tok/s):    150.00    
Peak concurrent requests:                50.00     
Total token throughput (tok/s):          92.62     
---------------Time to First Token----------------
Mean TTFT (ms):                          1926.76   
Median TTFT (ms):                        1845.92   
P50 TTFT (ms):                           1845.92   
P90 TTFT (ms):                           2692.78   
P95 TTFT (ms):                           3034.18   
P99 TTFT (ms):                           3615.38   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          396.27    
Median TPOT (ms):                        401.85    
P50 TPOT (ms):                           401.85    
P90 TPOT (ms):                           413.58    
P95 TPOT (ms):                           416.60    
P99 TPOT (ms):                           419.43    
---------------Inter-token Latency----------------
Mean ITL (ms):                           389.14    
Median ITL (ms):                         400.08    
P50 ITL (ms):                            400.08    
P90 ITL (ms):                            415.07    
P95 ITL (ms):                            420.93    
P99 ITL (ms):                            471.58    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1630910.20
Median E2EL (ms):                        1571188.68
P50 E2EL (ms):                           1571188.68
P90 E2EL (ms):                           2476121.92
P95 E2EL (ms):                           2660337.85
P99 E2EL (ms):                           2730455.19
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
