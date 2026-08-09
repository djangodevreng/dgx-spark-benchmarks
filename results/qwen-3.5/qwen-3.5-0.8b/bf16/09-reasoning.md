# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-07 10:06:00
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  300.93    
Total input tokens:                      55622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.17      
Output token throughput (tok/s):         695.53    
Peak output token throughput (tok/s):    1204.00   
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          880.37    
---------------Time to First Token----------------
Mean TTFT (ms):                          80.36     
Median TTFT (ms):                        82.11     
P50 TTFT (ms):                           82.11     
P90 TTFT (ms):                           110.81    
P95 TTFT (ms):                           115.00    
P99 TTFT (ms):                           116.56    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          10.31     
Median TPOT (ms):                        10.44     
P50 TPOT (ms):                           10.44     
P90 TPOT (ms):                           11.10     
P95 TPOT (ms):                           11.22     
P99 TPOT (ms):                           11.39     
---------------Inter-token Latency----------------
Mean ITL (ms):                           10.27     
Median ITL (ms):                         10.27     
P50 ITL (ms):                            10.27     
P90 ITL (ms):                            11.73     
P95 ITL (ms):                            12.14     
P99 ITL (ms):                            13.33     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          43059.91  
Median E2EL (ms):                        41743.47  
P50 E2EL (ms):                           41743.47  
P90 E2EL (ms):                           69155.00  
P95 E2EL (ms):                           73056.27  
P99 E2EL (ms):                           80462.97  
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
