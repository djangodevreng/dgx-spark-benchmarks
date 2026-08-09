# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-06 06:54:21
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  837.05    
Total input tokens:                      58416     
Total generated tokens:                  51315     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.30     
Peak output token throughput (tok/s):    195.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.09    
---------------Time to First Token----------------
Mean TTFT (ms):                          130.41    
Median TTFT (ms):                        129.09    
P50 TTFT (ms):                           129.09    
P90 TTFT (ms):                           176.14    
P95 TTFT (ms):                           192.51    
P99 TTFT (ms):                           211.03    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          36.16     
Median TPOT (ms):                        35.98     
P50 TPOT (ms):                           35.98     
P90 TPOT (ms):                           38.77     
P95 TPOT (ms):                           39.36     
P99 TPOT (ms):                           39.74     
---------------Inter-token Latency----------------
Mean ITL (ms):                           35.94     
Median ITL (ms):                         35.47     
P50 ITL (ms):                            35.47     
P90 ITL (ms):                            39.31     
P95 ITL (ms):                            40.02     
P99 ITL (ms):                            46.10     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7506.78   
Median E2EL (ms):                        4874.36   
P50 E2EL (ms):                           4874.36   
P90 E2EL (ms):                           17831.83  
P95 E2EL (ms):                           22933.76  
P99 E2EL (ms):                           29506.80  
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.
