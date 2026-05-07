# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-05 05:02:04
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name nemotron-3-super --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  855.12    
Total input tokens:                      58416     
Total generated tokens:                  52085     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         60.91     
Peak output token throughput (tok/s):    51.00     
Peak concurrent requests:                18.00     
Total token throughput (tok/s):          129.22    
---------------Time to First Token----------------
Mean TTFT (ms):                          1149.87   
Median TTFT (ms):                        1082.04   
P50 TTFT (ms):                           1082.04   
P90 TTFT (ms):                           1543.33   
P95 TTFT (ms):                           1692.21   
P99 TTFT (ms):                           2302.92   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          127.00    
Median TPOT (ms):                        130.40    
P50 TPOT (ms):                           130.40    
P90 TPOT (ms):                           163.13    
P95 TPOT (ms):                           168.74    
P99 TPOT (ms):                           196.20    
---------------Inter-token Latency----------------
Mean ITL (ms):                           335.83    
Median ITL (ms):                         337.68    
P50 ITL (ms):                            337.68    
P90 ITL (ms):                            415.59    
P95 ITL (ms):                            455.17    
P99 ITL (ms):                            703.91    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          28980.66  
Median E2EL (ms):                        17157.92  
P50 E2EL (ms):                           17157.92  
P90 E2EL (ms):                           74666.25  
P95 E2EL (ms):                           85975.70  
P99 E2EL (ms):                           121805.08 
---------------Speculative Decoding---------------
Acceptance rate (%):                     51.47     
Acceptance length:                       2.54      
Drafts:                                  20481     
Draft tokens:                            61443     
Accepted tokens:                         31626     
Per-position acceptance (%):
  Position 0:                            73.59     
  Position 1:                            49.46     
  Position 2:                            31.37     
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.
