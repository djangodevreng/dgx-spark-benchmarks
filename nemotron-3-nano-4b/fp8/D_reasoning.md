# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-05 17:03:34
**Profile:** fp8
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8 --served-model-name nemotron-3-nano-4b-fp8 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  487.49    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.10      
Output token throughput (tok/s):         429.35    
Peak output token throughput (tok/s):    660.00    
Peak concurrent requests:                33.00     
Total token throughput (tok/s):          543.82    
---------------Time to First Token----------------
Mean TTFT (ms):                          218.75    
Median TTFT (ms):                        224.35    
P50 TTFT (ms):                           224.35    
P90 TTFT (ms):                           284.05    
P95 TTFT (ms):                           286.99    
P99 TTFT (ms):                           304.23    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          41.90     
Median TPOT (ms):                        43.25     
P50 TPOT (ms):                           43.25     
P90 TPOT (ms):                           47.52     
P95 TPOT (ms):                           48.17     
P99 TPOT (ms):                           49.13     
---------------Inter-token Latency----------------
Mean ITL (ms):                           41.78     
Median ITL (ms):                         44.05     
P50 ITL (ms):                            44.05     
P90 ITL (ms):                            49.87     
P95 ITL (ms):                            50.59     
P99 ITL (ms):                            52.57     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          175098.84 
Median E2EL (ms):                        176817.38 
P50 E2EL (ms):                           176817.38 
P90 E2EL (ms):                           274731.60 
P95 E2EL (ms):                           304930.16 
P99 E2EL (ms):                           315801.38 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
