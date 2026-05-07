# Run I — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-05-06 14:54:49
**Profile:** bf16
**Model:** google/gemma-4-E4B-it
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model google/gemma-4-E4B-it --tokenizer google/gemma-4-E4B-it --served-model-name gemma-4-e4b-it-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename I_sharegpt-replay.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  837.44    
Total input tokens:                      59269     
Total generated tokens:                  51123     
Request throughput (req/s):              0.30      
Output token throughput (tok/s):         61.05     
Peak output token throughput (tok/s):    212.00    
Peak concurrent requests:                10.00     
Total token throughput (tok/s):          131.82    
---------------Time to First Token----------------
Mean TTFT (ms):                          165.89    
Median TTFT (ms):                        158.54    
P50 TTFT (ms):                           158.54    
P90 TTFT (ms):                           229.15    
P95 TTFT (ms):                           245.07    
P99 TTFT (ms):                           291.46    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          46.24     
Median TPOT (ms):                        45.84     
P50 TPOT (ms):                           45.84     
P90 TPOT (ms):                           47.70     
P95 TPOT (ms):                           49.44     
P99 TPOT (ms):                           52.33     
---------------Inter-token Latency----------------
Mean ITL (ms):                           45.97     
Median ITL (ms):                         45.29     
P50 ITL (ms):                            45.29     
P90 ITL (ms):                            51.69     
P95 ITL (ms):                            52.76     
P99 ITL (ms):                            57.25     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          9565.45   
Median E2EL (ms):                        6124.65   
P50 E2EL (ms):                           6124.65   
P90 E2EL (ms):                           23038.86  
P95 E2EL (ms):                           30069.39  
P99 E2EL (ms):                           39433.60  
==================================================

---

Volledige log in `I_sharegpt-replay.log`. Server-config in `meta.json`.
