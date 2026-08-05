# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-08 12:50:34
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-31B-IT-NVFP4 --tokenizer nvidia/Gemma-4-31B-IT-NVFP4 --served-model-name gemma-4-31b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  2083.57   
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.02      
Output token throughput (tok/s):         100.45    
Peak output token throughput (tok/s):    192.00    
Peak concurrent requests:                50.00     
Total token throughput (tok/s):          127.18    
---------------Time to First Token----------------
Mean TTFT (ms):                          2292.15   
Median TTFT (ms):                        1611.45   
P50 TTFT (ms):                           1611.45   
P90 TTFT (ms):                           5357.73   
P95 TTFT (ms):                           6300.16   
P99 TTFT (ms):                           6830.17   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          327.85    
Median TPOT (ms):                        318.62    
P50 TPOT (ms):                           318.62    
P90 TPOT (ms):                           416.71    
P95 TPOT (ms):                           429.65    
P99 TPOT (ms):                           499.84    
---------------Inter-token Latency----------------
Mean ITL (ms):                           302.87    
Median ITL (ms):                         265.55    
P50 ITL (ms):                            265.55    
P90 ITL (ms):                            409.83    
P95 ITL (ms):                            450.06    
P99 ITL (ms):                            544.36    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          1270119.58
Median E2EL (ms):                        1267697.04
P50 E2EL (ms):                           1267697.04
P90 E2EL (ms):                           1781237.14
P95 E2EL (ms):                           1918105.88
P99 E2EL (ms):                           1974816.81
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
