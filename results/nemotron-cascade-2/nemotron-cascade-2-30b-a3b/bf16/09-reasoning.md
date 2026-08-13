# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-09 13:07:38
**Profile:** bf16
**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Nemotron-Cascade-2-30B-A3B --tokenizer nvidia/Nemotron-Cascade-2-30B-A3B --served-model-name nemotron-cascade-2-30b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1414.08   
Total input tokens:                      56609     
Total generated tokens:                  209303    
Request throughput (req/s):              0.04      
Output token throughput (tok/s):         148.01    
Peak output token throughput (tok/s):    245.00    
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          188.05    
---------------Time to First Token----------------
Mean TTFT (ms):                          734.19    
Median TTFT (ms):                        706.45    
P50 TTFT (ms):                           706.45    
P90 TTFT (ms):                           921.31    
P95 TTFT (ms):                           972.67    
P99 TTFT (ms):                           1057.40   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          204.11    
Median TPOT (ms):                        206.17    
P50 TPOT (ms):                           206.17    
P90 TPOT (ms):                           234.76    
P95 TPOT (ms):                           237.15    
P99 TPOT (ms):                           241.71    
---------------Inter-token Latency----------------
Mean ITL (ms):                           196.72    
Median ITL (ms):                         200.83    
P50 ITL (ms):                            200.83    
P90 ITL (ms):                            244.90    
P95 ITL (ms):                            250.50    
P99 ITL (ms):                            279.64    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          824209.48 
Median E2EL (ms):                        836339.97 
P50 E2EL (ms):                           836339.97 
P90 E2EL (ms):                           1186733.50
P95 E2EL (ms):                           1274503.36
P99 E2EL (ms):                           1311854.21
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
