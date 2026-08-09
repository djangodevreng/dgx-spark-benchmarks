# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-07 22:37:12
**Profile:** bf16
**Model:** Qwen/Qwen3.5-9B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-9B --tokenizer Qwen/Qwen3.5-9B --served-model-name qwen3.5-9b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  944.90    
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.05      
Output token throughput (tok/s):         221.51    
Peak output token throughput (tok/s):    414.00    
Peak concurrent requests:                46.00     
Total token throughput (tok/s):          280.27    
---------------Time to First Token----------------
Mean TTFT (ms):                          524.06    
Median TTFT (ms):                        530.55    
P50 TTFT (ms):                           530.55    
P90 TTFT (ms):                           679.41    
P95 TTFT (ms):                           719.19    
P99 TTFT (ms):                           835.97    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          110.87    
Median TPOT (ms):                        111.57    
P50 TPOT (ms):                           111.57    
P90 TPOT (ms):                           118.19    
P95 TPOT (ms):                           118.77    
P99 TPOT (ms):                           120.44    
---------------Inter-token Latency----------------
Mean ITL (ms):                           110.00    
Median ITL (ms):                         112.03    
P50 ITL (ms):                            112.03    
P90 ITL (ms):                            120.35    
P95 ITL (ms):                            121.43    
P99 ITL (ms):                            132.03    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          460885.23 
Median E2EL (ms):                        448958.87 
P50 E2EL (ms):                           448958.87 
P90 E2EL (ms):                           699329.48 
P95 E2EL (ms):                           761223.16 
P99 E2EL (ms):                           782337.38 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
