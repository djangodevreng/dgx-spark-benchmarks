# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-14 08:45:33
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  710.36    
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         294.64    
Peak output token throughput (tok/s):    473.00    
Peak concurrent requests:                44.00     
Total token throughput (tok/s):          372.80    
---------------Time to First Token----------------
Mean TTFT (ms):                          388.68    
Median TTFT (ms):                        379.54    
P50 TTFT (ms):                           379.54    
P90 TTFT (ms):                           547.89    
P95 TTFT (ms):                           588.62    
P99 TTFT (ms):                           616.45    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          80.60     
Median TPOT (ms):                        82.27     
P50 TPOT (ms):                           82.27     
P90 TPOT (ms):                           92.10     
P95 TPOT (ms):                           93.41     
P99 TPOT (ms):                           97.65     
---------------Inter-token Latency----------------
Mean ITL (ms):                           79.92     
Median ITL (ms):                         82.73     
P50 ITL (ms):                            82.73     
P90 ITL (ms):                            99.69     
P95 ITL (ms):                            101.09    
P99 ITL (ms):                            111.10    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          334818.56 
Median E2EL (ms):                        339824.01 
P50 E2EL (ms):                           339824.01 
P90 E2EL (ms):                           508298.62 
P95 E2EL (ms):                           553089.67 
P99 E2EL (ms):                           572418.07 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
