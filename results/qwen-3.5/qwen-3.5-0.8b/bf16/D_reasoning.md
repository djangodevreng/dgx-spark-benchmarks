# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-04 23:12:50
**Profile:** bf16
**Model:** Qwen/Qwen3.5-0.8B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-0.8B --tokenizer Qwen/Qwen3.5-0.8B --served-model-name qwen3.5-0.8b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  301.91    
Total input tokens:                      55622     
Total generated tokens:                  209303    
Request throughput (req/s):              0.17      
Output token throughput (tok/s):         693.26    
Peak output token throughput (tok/s):    1178.00   
Peak concurrent requests:                14.00     
Total token throughput (tok/s):          877.49    
---------------Time to First Token----------------
Mean TTFT (ms):                          101.12    
Median TTFT (ms):                        96.13     
P50 TTFT (ms):                           96.13     
P90 TTFT (ms):                           116.99    
P95 TTFT (ms):                           126.73    
P99 TTFT (ms):                           295.63    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          10.51     
Median TPOT (ms):                        10.62     
P50 TPOT (ms):                           10.62     
P90 TPOT (ms):                           11.34     
P95 TPOT (ms):                           11.39     
P99 TPOT (ms):                           11.62     
---------------Inter-token Latency----------------
Mean ITL (ms):                           10.63     
Median ITL (ms):                         10.52     
P50 ITL (ms):                            10.52     
P90 ITL (ms):                            11.78     
P95 ITL (ms):                            12.22     
P99 ITL (ms):                            22.14     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          43882.29  
Median E2EL (ms):                        42708.51  
P50 E2EL (ms):                           42708.51  
P90 E2EL (ms):                           70276.37  
P95 E2EL (ms):                           74581.84  
P99 E2EL (ms):                           81844.36  
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
