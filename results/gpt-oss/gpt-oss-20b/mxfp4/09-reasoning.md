# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-14 13:21:51
**Profile:** mxfp4
**Model:** openai/gpt-oss-20b
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model openai/gpt-oss-20b --tokenizer openai/gpt-oss-20b --served-model-name gpt-oss-20b-mxfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  540.36    
Total input tokens:                      57819     
Total generated tokens:                  177938    
Request throughput (req/s):              0.09      
Output token throughput (tok/s):         329.30    
Peak output token throughput (tok/s):    153.00    
Peak concurrent requests:                34.00     
Total token throughput (tok/s):          436.30    
---------------Time to First Token----------------
Mean TTFT (ms):                          260.93    
Median TTFT (ms):                        256.27    
P50 TTFT (ms):                           256.27    
P90 TTFT (ms):                           356.84    
P95 TTFT (ms):                           367.02    
P99 TTFT (ms):                           400.34    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          59.35     
Median TPOT (ms):                        54.92     
P50 TPOT (ms):                           54.92     
P90 TPOT (ms):                           58.80     
P95 TPOT (ms):                           80.12     
P99 TPOT (ms):                           168.50    
---------------Inter-token Latency----------------
Mean ITL (ms):                           230.10    
Median ITL (ms):                         52.92     
P50 ITL (ms):                            52.92     
P90 ITL (ms):                            60.12     
P95 ITL (ms):                            61.79     
P99 ITL (ms):                            65.76     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          190341.78 
Median E2EL (ms):                        195197.01 
P50 E2EL (ms):                           195197.01 
P90 E2EL (ms):                           344824.84 
P95 E2EL (ms):                           378473.35 
P99 E2EL (ms):                           391138.90 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
