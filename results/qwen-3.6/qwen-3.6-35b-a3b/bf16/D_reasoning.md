# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-05 12:18:43
**Profile:** bf16
**Model:** Qwen/Qwen3.6-35B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.6-35B-A3B --tokenizer Qwen/Qwen3.6-35B-A3B --served-model-name qwen3.6-35b-a3b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1426.74   
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.04      
Output token throughput (tok/s):         146.70    
Peak output token throughput (tok/s):    245.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          185.62    
---------------Time to First Token----------------
Mean TTFT (ms):                          763.59    
Median TTFT (ms):                        740.90    
P50 TTFT (ms):                           740.90    
P90 TTFT (ms):                           1022.34   
P95 TTFT (ms):                           1079.33   
P99 TTFT (ms):                           1345.31   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          199.05    
Median TPOT (ms):                        199.27    
P50 TPOT (ms):                           199.27    
P90 TPOT (ms):                           221.52    
P95 TPOT (ms):                           222.47    
P99 TPOT (ms):                           227.06    
---------------Inter-token Latency----------------
Mean ITL (ms):                           209.02    
Median ITL (ms):                         212.01    
P50 ITL (ms):                            212.01    
P90 ITL (ms):                            236.40    
P95 ITL (ms):                            318.99    
P99 ITL (ms):                            440.82    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          817623.56 
Median E2EL (ms):                        819878.00 
P50 E2EL (ms):                           819878.00 
P90 E2EL (ms):                           1201676.26
P95 E2EL (ms):                           1287324.24
P99 E2EL (ms):                           1323182.20
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
