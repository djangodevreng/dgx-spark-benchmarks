# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-23 12:31:33
**Profile:** nvfp4
**Model:** RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4 --tokenizer RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4 --served-model-name mistral-small-3.2-24b --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  1107.48   
Total input tokens:                      937836    
Total generated tokens:                  97092     
Request throughput (req/s):              0.18      
Output token throughput (tok/s):         87.67     
Peak output token throughput (tok/s):    468.00    
Peak concurrent requests:                199.00    
Total token throughput (tok/s):          934.49    
---------------Time to First Token----------------
Mean TTFT (ms):                          87764.48  
Median TTFT (ms):                        86739.92  
P50 TTFT (ms):                           86739.92  
P90 TTFT (ms):                           131104.43 
P95 TTFT (ms):                           155844.87 
P99 TTFT (ms):                           189661.14 
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          1606.27   
Median TPOT (ms):                        1267.12   
P50 TPOT (ms):                           1267.12   
P90 TPOT (ms):                           3122.71   
P95 TPOT (ms):                           4429.32   
P99 TPOT (ms):                           6312.57   
---------------Inter-token Latency----------------
Mean ITL (ms):                           1178.03   
Median ITL (ms):                         472.52    
P50 ITL (ms):                            472.52    
P90 ITL (ms):                            5444.12   
P95 ITL (ms):                            7066.53   
P99 ITL (ms):                            7172.13   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          659648.52 
Median E2EL (ms):                        666057.59 
P50 E2EL (ms):                           666057.59 
P90 E2EL (ms):                           944282.28 
P95 E2EL (ms):                           997624.24 
P99 E2EL (ms):                           1056501.42
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.
