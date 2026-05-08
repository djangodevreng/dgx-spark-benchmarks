# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-07 21:22:22
**Profile:** bf16
**Model:** Qwen/Qwen3.5-4B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-4B --tokenizer Qwen/Qwen3.5-4B --served-model-name qwen3.5-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  630.59    
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         331.92    
Peak output token throughput (tok/s):    611.00    
Peak concurrent requests:                42.00     
Total token throughput (tok/s):          419.97    
---------------Time to First Token----------------
Mean TTFT (ms):                          347.63    
Median TTFT (ms):                        333.88    
P50 TTFT (ms):                           333.88    
P90 TTFT (ms):                           471.65    
P95 TTFT (ms):                           505.40    
P99 TTFT (ms):                           556.03    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          61.25     
Median TPOT (ms):                        61.82     
P50 TPOT (ms):                           61.82     
P90 TPOT (ms):                           66.27     
P95 TPOT (ms):                           67.31     
P99 TPOT (ms):                           69.27     
---------------Inter-token Latency----------------
Mean ITL (ms):                           62.76     
Median ITL (ms):                         61.88     
P50 ITL (ms):                            61.88     
P90 ITL (ms):                            70.83     
P95 ITL (ms):                            76.01     
P99 ITL (ms):                            130.08    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          256388.72 
Median E2EL (ms):                        251069.41 
P50 E2EL (ms):                           251069.41 
P90 E2EL (ms):                           397019.04 
P95 E2EL (ms):                           435814.44 
P99 E2EL (ms):                           447613.70 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
