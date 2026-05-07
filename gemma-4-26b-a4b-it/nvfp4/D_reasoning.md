# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-06 10:52:29
**Profile:** nvfp4
**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/Gemma-4-26B-A4B-NVFP4 --tokenizer nvidia/Gemma-4-26B-A4B-NVFP4 --served-model-name gemma-4-26b-a4b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  669.58    
Total input tokens:                      55684     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         312.59    
Peak output token throughput (tok/s):    528.00    
Peak concurrent requests:                44.00     
Total token throughput (tok/s):          395.75    
---------------Time to First Token----------------
Mean TTFT (ms):                          365.26    
Median TTFT (ms):                        356.25    
P50 TTFT (ms):                           356.25    
P90 TTFT (ms):                           500.92    
P95 TTFT (ms):                           530.73    
P99 TTFT (ms):                           658.92    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          72.36     
Median TPOT (ms):                        73.13     
P50 TPOT (ms):                           73.13     
P90 TPOT (ms):                           80.35     
P95 TPOT (ms):                           80.83     
P99 TPOT (ms):                           84.31     
---------------Inter-token Latency----------------
Mean ITL (ms):                           71.56     
Median ITL (ms):                         72.21     
P50 ITL (ms):                            72.21     
P90 ITL (ms):                            86.99     
P95 ITL (ms):                            88.15     
P99 ITL (ms):                            107.35    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          299907.45 
Median E2EL (ms):                        300946.05 
P50 E2EL (ms):                           300946.05 
P90 E2EL (ms):                           453123.22 
P95 E2EL (ms):                           498158.28 
P99 E2EL (ms):                           515845.35 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
