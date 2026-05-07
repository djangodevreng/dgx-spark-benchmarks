# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-06 14:13:37
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  621.11    
Total input tokens:                      55484     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         336.98    
Peak output token throughput (tok/s):    656.00    
Peak concurrent requests:                41.00     
Total token throughput (tok/s):          426.32    
---------------Time to First Token----------------
Mean TTFT (ms):                          313.37    
Median TTFT (ms):                        307.56    
P50 TTFT (ms):                           307.56    
P90 TTFT (ms):                           407.12    
P95 TTFT (ms):                           452.08    
P99 TTFT (ms):                           649.28    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          57.32     
Median TPOT (ms):                        57.60     
P50 TPOT (ms):                           57.60     
P90 TPOT (ms):                           60.23     
P95 TPOT (ms):                           61.20     
P99 TPOT (ms):                           62.13     
---------------Inter-token Latency----------------
Mean ITL (ms):                           57.37     
Median ITL (ms):                         57.20     
P50 ITL (ms):                            57.20     
P90 ITL (ms):                            62.74     
P95 ITL (ms):                            64.00     
P99 ITL (ms):                            72.61     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          240453.38 
Median E2EL (ms):                        228579.25 
P50 E2EL (ms):                           228579.25 
P90 E2EL (ms):                           376528.42 
P95 E2EL (ms):                           409573.61 
P99 E2EL (ms):                           423800.68 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
