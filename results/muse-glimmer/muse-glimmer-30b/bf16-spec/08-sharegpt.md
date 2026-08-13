# Test 08-sharegpt — ShareGPT replay, Poisson 0.3 rps, burstiness 0.7

**Generated:** 2026-08-12 18:49:23
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16-spec --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name sharegpt --dataset-path /tmp/ShareGPT_V3.json --num-prompts 250 --request-rate 0.3 --burstiness 0.7 --result-filename 08-sharegpt.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     250       
Failed requests:                         0         
Request rate configured (RPS):           0.30      
Benchmark duration (s):                  875.56    
Total input tokens:                      67099     
Total generated tokens:                  50182     
Request throughput (req/s):              0.29      
Output token throughput (tok/s):         57.31     
Peak output token throughput (tok/s):    40.00     
Peak concurrent requests:                13.00     
Total token throughput (tok/s):          133.95    
---------------Time to First Token----------------
Mean TTFT (ms):                          1044.77   
Median TTFT (ms):                        940.67    
P50 TTFT (ms):                           940.67    
P90 TTFT (ms):                           1401.63   
P95 TTFT (ms):                           1558.71   
P99 TTFT (ms):                           2721.09   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          77.25     
Median TPOT (ms):                        77.40     
P50 TPOT (ms):                           77.40     
P90 TPOT (ms):                           129.64    
P95 TPOT (ms):                           138.58    
P99 TPOT (ms):                           149.14    
---------------Inter-token Latency----------------
Mean ITL (ms):                           323.77    
Median ITL (ms):                         309.44    
P50 ITL (ms):                            309.44    
P90 ITL (ms):                            350.67    
P95 ITL (ms):                            371.05    
P99 ITL (ms):                            637.74    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          20554.27  
Median E2EL (ms):                        10747.45  
P50 E2EL (ms):                           10747.45  
P90 E2EL (ms):                           55921.41  
P95 E2EL (ms):                           68395.69  
P99 E2EL (ms):                           86652.44  
---------------Speculative Decoding---------------
Acceptance rate (%):                     15.77     
Acceptance length:                       3.36      
Drafts:                                  15099     
Draft tokens:                            226485    
Accepted tokens:                         35707     
Per-position acceptance (%):
  Position 0:                            68.30     
  Position 1:                            42.15     
  Position 2:                            26.84     
  Position 3:                            18.13     
  Position 4:                            13.22     
  Position 5:                            10.54     
  Position 6:                            8.87      
  Position 7:                            7.85      
  Position 8:                            7.05      
  Position 9:                            6.51      
  Position 10:                           6.15      
  Position 11:                           5.78      
  Position 12:                           5.32      
  Position 13:                           5.06      
  Position 14:                           4.72      
==================================================

---

Volledige log in `08-sharegpt.log`. Server-config in `meta.json`.
