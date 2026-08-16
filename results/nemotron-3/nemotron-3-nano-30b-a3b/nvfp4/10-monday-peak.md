# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-13 15:17:44
**Profile:** nvfp4
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4 --served-model-name nemotron-3-nano-30b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  577.53    
Total input tokens:                      1202858   
Total generated tokens:                  150317    
Request throughput (req/s):              0.52      
Output token throughput (tok/s):         260.28    
Peak output token throughput (tok/s):    425.00    
Peak concurrent requests:                28.00     
Total token throughput (tok/s):          2343.03   
---------------Time to First Token----------------
Mean TTFT (ms):                          1063.46   
Median TTFT (ms):                        903.22    
P50 TTFT (ms):                           903.22    
P90 TTFT (ms):                           1627.59   
P95 TTFT (ms):                           2120.62   
P99 TTFT (ms):                           5449.97   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          91.78     
Median TPOT (ms):                        92.15     
P50 TPOT (ms):                           92.15     
P90 TPOT (ms):                           99.70     
P95 TPOT (ms):                           104.61    
P99 TPOT (ms):                           134.06    
---------------Inter-token Latency----------------
Mean ITL (ms):                           90.26     
Median ITL (ms):                         65.01     
P50 ITL (ms):                            65.01     
P90 ITL (ms):                            76.87     
P95 ITL (ms):                            109.93    
P99 ITL (ms):                            907.37    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          46286.29  
Median E2EL (ms):                        44614.96  
P50 E2EL (ms):                           44614.96  
P90 E2EL (ms):                           82069.28  
P95 E2EL (ms):                           85426.03  
P99 E2EL (ms):                           90172.53  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.
