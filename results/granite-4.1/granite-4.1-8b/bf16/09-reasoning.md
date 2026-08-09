# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-09 08:50:37
**Profile:** bf16
**Model:** ibm-granite/granite-4.1-8b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model ibm-granite/granite-4.1-8b --tokenizer ibm-granite/granite-4.1-8b --served-model-name granite-4-1-8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1100.56   
Total input tokens:                      55405     
Total generated tokens:                  209303    
Request throughput (req/s):              0.05      
Output token throughput (tok/s):         190.18    
Peak output token throughput (tok/s):    368.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          240.52    
---------------Time to First Token----------------
Mean TTFT (ms):                          543.02    
Median TTFT (ms):                        523.19    
P50 TTFT (ms):                           523.19    
P90 TTFT (ms):                           734.61    
P95 TTFT (ms):                           763.28    
P99 TTFT (ms):                           872.50    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          129.11    
Median TPOT (ms):                        131.03    
P50 TPOT (ms):                           131.03    
P90 TPOT (ms):                           138.30    
P95 TPOT (ms):                           139.14    
P99 TPOT (ms):                           140.10    
---------------Inter-token Latency----------------
Mean ITL (ms):                           130.03    
Median ITL (ms):                         135.62    
P50 ITL (ms):                            135.62    
P90 ITL (ms):                            143.09    
P95 ITL (ms):                            144.58    
P99 ITL (ms):                            147.84    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          544873.26 
Median E2EL (ms):                        518990.96 
P50 E2EL (ms):                           518990.96 
P90 E2EL (ms):                           851193.17 
P95 E2EL (ms):                           915004.24 
P99 E2EL (ms):                           938335.79 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
