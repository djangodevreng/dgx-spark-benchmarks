# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-17 04:29:59
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  837.28    
Total input tokens:                      59269     
Total generated tokens:                  50835     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         60.71     
Peak output token throughput (tok/s):    209.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.50    
---------------Time to First Token----------------
Mean TTFT (ms):                          174.24    
Median TTFT (ms):                        165.37    
P50 TTFT (ms):                           165.37    
P90 TTFT (ms):                           232.72    
P95 TTFT (ms):                           249.56    
P99 TTFT (ms):                           305.34    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          44.99     
Median TPOT (ms):                        44.32     
P50 TPOT (ms):                           44.32     
P90 TPOT (ms):                           46.74     
P95 TPOT (ms):                           48.55     
P99 TPOT (ms):                           51.23     
---------------Inter-token Latency----------------
Mean ITL (ms):                           44.54     
Median ITL (ms):                         43.77     
P50 ITL (ms):                            43.77     
P90 ITL (ms):                            47.23     
P95 ITL (ms):                            51.13     
P99 ITL (ms):                            56.88     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          9230.18   
Median E2EL (ms):                        5956.27   
P50 E2EL (ms):                           5956.27   
P90 E2EL (ms):                           22163.59  
P95 E2EL (ms):                           30214.10  
P99 E2EL (ms):                           38088.38  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.
