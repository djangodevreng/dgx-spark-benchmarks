# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-07 14:18:55
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  390.37    
Total input tokens:                      55622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.13      
Output token throughput (tok/s):         536.17    
Peak output token throughput (tok/s):    927.00    
Peak concurrent requests:                24.00     
Total token throughput (tok/s):          678.65    
---------------Time to First Token----------------
Mean TTFT (ms):                          199.78    
Median TTFT (ms):                        169.30    
P50 TTFT (ms):                           169.30    
P90 TTFT (ms):                           224.55    
P95 TTFT (ms):                           329.87    
P99 TTFT (ms):                           855.74    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          23.60     
Median TPOT (ms):                        24.25     
P50 TPOT (ms):                           24.25     
P90 TPOT (ms):                           25.13     
P95 TPOT (ms):                           25.22     
P99 TPOT (ms):                           25.46     
---------------Inter-token Latency----------------
Mean ITL (ms):                           24.09     
Median ITL (ms):                         23.96     
P50 ITL (ms):                            23.96     
P90 ITL (ms):                            26.23     
P95 ITL (ms):                            28.04     
P99 ITL (ms):                            51.11     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          99085.74  
Median E2EL (ms):                        94011.39  
P50 E2EL (ms):                           94011.39  
P90 E2EL (ms):                           158566.36 
P95 E2EL (ms):                           172958.31 
P99 E2EL (ms):                           182657.49 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
