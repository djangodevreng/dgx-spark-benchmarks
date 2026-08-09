# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-08 10:39:03
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  494.69    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         423.10    
Peak output token throughput (tok/s):    665.00    
Peak concurrent requests:                35.00     
Total token throughput (tok/s):          535.91    
---------------Time to First Token----------------
Mean TTFT (ms):                          440.49    
Median TTFT (ms):                        467.19    
P50 TTFT (ms):                           467.19    
P90 TTFT (ms):                           654.46    
P95 TTFT (ms):                           679.78    
P99 TTFT (ms):                           980.95    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          43.97     
Median TPOT (ms):                        45.86     
P50 TPOT (ms):                           45.86     
P90 TPOT (ms):                           50.07     
P95 TPOT (ms):                           50.28     
P99 TPOT (ms):                           52.15     
---------------Inter-token Latency----------------
Mean ITL (ms):                           43.71     
Median ITL (ms):                         45.15     
P50 ITL (ms):                            45.15     
P90 ITL (ms):                            51.30     
P95 ITL (ms):                            52.39     
P99 ITL (ms):                            60.90     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          183406.10 
Median E2EL (ms):                        186021.62 
P50 E2EL (ms):                           186021.62 
P90 E2EL (ms):                           284677.37 
P95 E2EL (ms):                           317633.87 
P99 E2EL (ms):                           328936.22 
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
