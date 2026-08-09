# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-06 13:14:31
**Profile:** nvfp4-v23
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  675.82    
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         309.70    
Peak output token throughput (tok/s):    484.00    
Peak concurrent requests:                44.00     
Total token throughput (tok/s):          392.10    
---------------Time to First Token----------------
Mean TTFT (ms):                          346.10    
Median TTFT (ms):                        338.50    
P50 TTFT (ms):                           338.50    
P90 TTFT (ms):                           467.16    
P95 TTFT (ms):                           479.00    
P99 TTFT (ms):                           581.94    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          74.24     
Median TPOT (ms):                        75.02     
P50 TPOT (ms):                           75.02     
P90 TPOT (ms):                           83.12     
P95 TPOT (ms):                           83.47     
P99 TPOT (ms):                           87.85     
---------------Inter-token Latency----------------
Mean ITL (ms):                           73.29     
Median ITL (ms):                         74.03     
P50 ITL (ms):                            74.03     
P90 ITL (ms):                            90.74     
P95 ITL (ms):                            91.82     
P99 ITL (ms):                            94.46     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          307127.18 
Median E2EL (ms):                        310371.19 
P50 E2EL (ms):                           310371.19 
P90 E2EL (ms):                           461439.50 
P95 E2EL (ms):                           506584.13 
P99 E2EL (ms):                           525691.50 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
