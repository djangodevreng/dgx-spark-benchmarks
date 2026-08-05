# Run H — Random 4k Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-06-26 08:15:41
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 200 --request-rate 0.3 --burstiness 0.7 --result-filename H_office-baseline.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     200       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  695.74    
Total input tokens:                      814812    
Total generated tokens:                  97092     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         139.55    
Peak output token throughput (tok/s):    272.00    
Peak concurrent requests:                16.00     
Total token throughput (tok/s):          1310.69   
---------------Time to First Token----------------
Mean TTFT (ms):                          1120.01   
Median TTFT (ms):                        1012.04   
P50 TTFT (ms):                           1012.04   
P90 TTFT (ms):                           1829.14   
P95 TTFT (ms):                           2154.19   
P99 TTFT (ms):                           3032.07   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          60.08     
Median TPOT (ms):                        61.75     
P50 TPOT (ms):                           61.75     
P90 TPOT (ms):                           73.10     
P95 TPOT (ms):                           77.36     
P99 TPOT (ms):                           85.98     
---------------Inter-token Latency----------------
Mean ITL (ms):                           60.12     
Median ITL (ms):                         54.77     
P50 ITL (ms):                            54.77     
P90 ITL (ms):                            58.90     
P95 ITL (ms):                            120.65    
P99 ITL (ms):                            343.42    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          30101.24  
Median E2EL (ms):                        28713.13  
P50 E2EL (ms):                           28713.13  
P90 E2EL (ms):                           53397.16  
P95 E2EL (ms):                           58882.70  
P99 E2EL (ms):                           64719.71  
==================================================

---

Volledige log in `H_office-baseline.log`. Server-config in `meta.json`.
