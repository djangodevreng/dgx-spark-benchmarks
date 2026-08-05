# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-06-26 07:26:10
**Profile:** nvfp4
**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model RedHatAI/Qwen3.6-35B-A3B-NVFP4 --tokenizer RedHatAI/Qwen3.6-35B-A3B-NVFP4 --served-model-name qwen3.6-35b-a3b-nvfp4 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  745.33    
Total input tokens:                      55522     
Total generated tokens:                  209303    
Request throughput (req/s):              0.07      
Output token throughput (tok/s):         280.82    
Peak output token throughput (tok/s):    413.00    
Peak concurrent requests:                44.00     
Total token throughput (tok/s):          355.31    
---------------Time to First Token----------------
Mean TTFT (ms):                          431.00    
Median TTFT (ms):                        430.12    
P50 TTFT (ms):                           430.12    
P90 TTFT (ms):                           615.17    
P95 TTFT (ms):                           689.70    
P99 TTFT (ms):                           763.54    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          86.50     
Median TPOT (ms):                        87.63     
P50 TPOT (ms):                           87.63     
P90 TPOT (ms):                           99.36     
P95 TPOT (ms):                           100.04    
P99 TPOT (ms):                           104.94    
---------------Inter-token Latency----------------
Mean ITL (ms):                           98.38     
Median ITL (ms):                         89.50     
P50 ITL (ms):                            89.50     
P90 ITL (ms):                            150.75    
P95 ITL (ms):                            195.80    
P99 ITL (ms):                            294.64    
----------------End-to-end Latency----------------
Mean E2EL (ms):                          358644.34 
Median E2EL (ms):                        366545.92 
P50 E2EL (ms):                           366545.92 
P90 E2EL (ms):                           542057.19 
P95 E2EL (ms):                           589121.23 
P99 E2EL (ms):                           608512.55 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
