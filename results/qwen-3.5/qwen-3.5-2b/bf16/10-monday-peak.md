# Test 10-monday-peak — Random 4k Poisson 1.5 rps, cap 25

**Generated:** 2026-08-07 15:29:45
**Profile:** bf16
**Model:** Qwen/Qwen3.5-2B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model Qwen/Qwen3.5-2B --tokenizer Qwen/Qwen3.5-2B --served-model-name qwen3.5-2b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 4000 --random-output-len 500 --random-range-ratio 0.9 --num-prompts 300 --request-rate 1.5 --burstiness 1.0 --max-concurrency 25 --result-filename 10-monday-peak.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     300       
Failed requests:                         0         
Maximum request concurrency:             25        
Request rate configured (RPS):           1.50      
Benchmark duration (s):                  253.76    
Total input tokens:                      1201770   
Total generated tokens:                  150317    
Request throughput (req/s):              1.18      
Output token throughput (tok/s):         592.36    
Peak output token throughput (tok/s):    899.00    
Peak concurrent requests:                29.00     
Total token throughput (tok/s):          5328.18   
---------------Time to First Token----------------
Mean TTFT (ms):                          438.12    
Median TTFT (ms):                        432.44    
P50 TTFT (ms):                           432.44    
P90 TTFT (ms):                           681.42    
P95 TTFT (ms):                           780.18    
P99 TTFT (ms):                           983.67    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          38.49     
Median TPOT (ms):                        39.08     
P50 TPOT (ms):                           39.08     
P90 TPOT (ms):                           41.40     
P95 TPOT (ms):                           42.65     
P99 TPOT (ms):                           45.53     
---------------Inter-token Latency----------------
Mean ITL (ms):                           38.33     
Median ITL (ms):                         28.97     
P50 ITL (ms):                            28.97     
P90 ITL (ms):                            57.95     
P95 ITL (ms):                            136.24    
P99 ITL (ms):                            144.84    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          19642.26  
Median E2EL (ms):                        19366.15  
P50 E2EL (ms):                           19366.15  
P90 E2EL (ms):                           35142.08  
P95 E2EL (ms):                           36529.36  
P99 E2EL (ms):                           37990.85  
==================================================

---

Volledige log in `10-monday-peak.log`. Server-config in `meta.json`.
