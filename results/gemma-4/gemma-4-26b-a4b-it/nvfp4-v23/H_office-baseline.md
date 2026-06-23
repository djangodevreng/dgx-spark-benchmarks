# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 02:54:28
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  698.24    
Total input tokens:                      815399    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         139.05    
Peak output token throughput (tok/s):    288.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1306.85   
---------------Time to First Token----------------
Mean TTFT (ms):                          1145.30   
Median TTFT (ms):                        1051.08   
P50 TTFT (ms):                           1051.08   
P90 TTFT (ms):                           1986.93   
P95 TTFT (ms):                           2393.78   
P99 TTFT (ms):                           3016.23   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          61.25     
Median TPOT (ms):                        61.54     
P50 TPOT (ms):                           61.54     
P90 TPOT (ms):                           73.82     
P95 TPOT (ms):                           77.98     
P99 TPOT (ms):                           85.59     
---------------Inter-token Latency----------------
Mean ITL (ms):                           60.83     
Median ITL (ms):                         50.26     
P50 ITL (ms):                            50.26     
P90 ITL (ms):                            56.93     
P95 ITL (ms):                            58.14     
P99 ITL (ms):                            581.92    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          30674.90  
Median E2EL (ms):                        29290.27  
P50 E2EL (ms):                           29290.27  
P90 E2EL (ms):                           53306.24  
P95 E2EL (ms):                           59621.63  
P99 E2EL (ms):                           62765.55  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.
