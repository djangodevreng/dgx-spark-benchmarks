# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-07 15:25:19
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  394.54    
Total input tokens:                      55622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.13      
Output token throughput (tok/s):         530.50    
Peak output token throughput (tok/s):    851.00    
Peak concurrent requests:                24.00     
Total token throughput (tok/s):          671.48    
---------------Time to First Token----------------
Mean TTFT (ms):                          143.56    
Median TTFT (ms):                        141.85    
P50 TTFT (ms):                           141.85    
P90 TTFT (ms):                           191.30    
P95 TTFT (ms):                           194.40    
P99 TTFT (ms):                           210.93    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          24.78     
Median TPOT (ms):                        25.52     
P50 TPOT (ms):                           25.52     
P90 TPOT (ms):                           27.08     
P95 TPOT (ms):                           27.17     
P99 TPOT (ms):                           27.26     
---------------Inter-token Latency----------------
Mean ITL (ms):                           24.75     
Median ITL (ms):                         25.50     
P50 ITL (ms):                            25.50     
P90 ITL (ms):                            28.32     
P95 ITL (ms):                            29.09     
P99 ITL (ms):                            31.37     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          103766.06 
Median E2EL (ms):                        99751.10  
P50 E2EL (ms):                           99751.10  
P90 E2EL (ms):                           166180.81 
P95 E2EL (ms):                           182824.51 
P99 E2EL (ms):                           192682.17 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
