# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-07 18:24:01
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  650.79    
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         321.61    
Peak output token throughput (tok/s):    559.00    
Peak concurrent requests:                43.00     
Total token throughput (tok/s):          406.93    
---------------Time to First Token----------------
Mean TTFT (ms):                          319.36    
Median TTFT (ms):                        317.71    
P50 TTFT (ms):                           317.71    
P90 TTFT (ms):                           437.82    
P95 TTFT (ms):                           460.07    
P99 TTFT (ms):                           508.78    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          65.72     
Median TPOT (ms):                        66.51     
P50 TPOT (ms):                           66.51     
P90 TPOT (ms):                           72.48     
P95 TPOT (ms):                           73.70     
P99 TPOT (ms):                           76.04     
---------------Inter-token Latency----------------
Mean ITL (ms):                           65.46     
Median ITL (ms):                         66.20     
P50 ITL (ms):                            66.20     
P90 ITL (ms):                            76.92     
P95 ITL (ms):                            78.18     
P99 ITL (ms):                            80.16     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          274285.66 
Median E2EL (ms):                        273083.83 
P50 E2EL (ms):                           273083.83 
P90 E2EL (ms):                           419932.75 
P95 E2EL (ms):                           461617.87 
P99 E2EL (ms):                           474695.08 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
