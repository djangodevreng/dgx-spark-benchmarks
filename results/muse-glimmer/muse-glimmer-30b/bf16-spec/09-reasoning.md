# Test 09-reasoning — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-08-12 19:18:55
**Profile:** bf16-spec
**Model:** meta-models/Muse-Glimmer-30B
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model meta-models/Muse-Glimmer-30B --tokenizer meta-models/Muse-Glimmer-30B --served-model-name muse-glimmer-30b-bf16-spec --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename 09-reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  1725.74   
Total input tokens:                      57758     
Total generated tokens:                  209303    
Request throughput (req/s):              0.03      
Output token throughput (tok/s):         121.28    
Peak output token throughput (tok/s):    83.00     
Peak concurrent requests:                49.00     
Total token throughput (tok/s):          154.75    
---------------Time to First Token----------------
Mean TTFT (ms):                          2727.65   
Median TTFT (ms):                        2601.98   
P50 TTFT (ms):                           2601.98   
P90 TTFT (ms):                           4153.71   
P95 TTFT (ms):                           4338.38   
P99 TTFT (ms):                           4473.18   
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          248.51    
Median TPOT (ms):                        230.54    
P50 TPOT (ms):                           230.54    
P90 TPOT (ms):                           386.50    
P95 TPOT (ms):                           423.03    
P99 TPOT (ms):                           488.73    
---------------Inter-token Latency----------------
Mean ITL (ms):                           1022.16   
Median ITL (ms):                         1034.33   
P50 ITL (ms):                            1034.33   
P90 ITL (ms):                            1113.65   
P95 ITL (ms):                            1124.71   
P99 ITL (ms):                            2200.21   
----------------End-to-end Latency----------------
Mean E2EL (ms):                          904739.04 
Median E2EL (ms):                        922910.53 
P50 E2EL (ms):                           922910.53 
P90 E2EL (ms):                           1203974.54
P95 E2EL (ms):                           1391017.47
P99 E2EL (ms):                           1572005.88
---------------Speculative Decoding---------------
Acceptance rate (%):                     18.86     
Acceptance length:                       3.83      
Drafts:                                  54713     
Draft tokens:                            820695    
Accepted tokens:                         154753    
Per-position acceptance (%):
  Position 0:                            68.26     
  Position 1:                            46.70     
  Position 2:                            31.16     
  Position 3:                            21.67     
  Position 4:                            17.07     
  Position 5:                            14.24     
  Position 6:                            12.41     
  Position 7:                            11.15     
  Position 8:                            10.14     
  Position 9:                            9.49      
  Position 10:                           8.94      
  Position 11:                           8.47      
  Position 12:                           8.14      
  Position 13:                           7.78      
  Position 14:                           7.23      
==================================================

---

Volledige log in `09-reasoning.log`. Server-config in `meta.json`.
