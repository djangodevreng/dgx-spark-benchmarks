# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-06-26 10:15:15
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  567.13    
Total input tokens:                      57819     
Total generated tokens:                  176886    
Request throughput (req/s):              0.09      
Output token throughput (tok/s):         311.90    
Peak output token throughput (tok/s):    239.00    
Peak concurrent requests:                35.00     
Total token throughput (tok/s):          413.85    
---------------Time to First Token----------------
Mean TTFT (ms):                          252.78    
Median TTFT (ms):                        243.65    
P50 TTFT (ms):                           243.65    
P90 TTFT (ms):                           344.25    
P95 TTFT (ms):                           373.28    
P99 TTFT (ms):                           400.04    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          56.31     
Median TPOT (ms):                        54.47     
P50 TPOT (ms):                           54.47     
P90 TPOT (ms):                           58.65     
P95 TPOT (ms):                           84.59     
P99 TPOT (ms):                           108.02    
---------------Inter-token Latency----------------
Mean ITL (ms):                           150.02    
Median ITL (ms):                         54.16     
P50 ITL (ms):                            54.16     
P90 ITL (ms):                            60.23     
P95 ITL (ms):                            61.89     
P99 ITL (ms):                            81.23     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          194270.84 
Median E2EL (ms):                        188235.78 
P50 E2EL (ms):                           188235.78 
P90 E2EL (ms):                           346351.51 
P95 E2EL (ms):                           376189.12 
P99 E2EL (ms):                           396405.73 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
