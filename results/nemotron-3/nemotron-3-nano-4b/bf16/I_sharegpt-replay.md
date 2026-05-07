# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 16:09:47
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  836.14    
Total input tokens:                      58416     
Total generated tokens:                  51130     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.15     
Peak output token throughput (tok/s):    202.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.01    
---------------Time to First Token----------------
Mean TTFT (ms):                          138.84    
Median TTFT (ms):                        133.71    
P50 TTFT (ms):                           133.71    
P90 TTFT (ms):                           181.53    
P95 TTFT (ms):                           199.16    
P99 TTFT (ms):                           247.40    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          35.51     
Median TPOT (ms):                        35.37     
P50 TPOT (ms):                           35.37     
P90 TPOT (ms):                           37.87     
P95 TPOT (ms):                           38.32     
P99 TPOT (ms):                           38.84     
---------------Inter-token Latency----------------
Mean ITL (ms):                           35.53     
Median ITL (ms):                         35.11     
P50 ITL (ms):                            35.11     
P90 ITL (ms):                            38.78     
P95 ITL (ms):                            39.72     
P99 ITL (ms):                            49.03     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          7404.09   
Median E2EL (ms):                        4984.84   
P50 E2EL (ms):                           4984.84   
P90 E2EL (ms):                           17611.97  
P95 E2EL (ms):                           22306.85  
P99 E2EL (ms):                           28833.56  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.
