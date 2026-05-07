# Run D — 1k prompt + 4k output, Poisson 0.2 rps, lange CoT

**Generated:** 2026-05-05 15:20:08
**Profile:** bf16
**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Hardware:** DGX Spark NVIDIA GB10 128GB
**Tool:** vllm

## Command

```bash
docker exec -e PYTHONUNBUFFERED=1 vllm-bench vllm bench serve --backend openai-chat --base-url http://localhost:8000 --endpoint /v1/chat/completions --model nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --tokenizer nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16 --served-model-name nemotron-3-nano-4b-bf16 --percentile-metrics ttft,tpot,itl,e2el --metric-percentiles 50,90,95,99 --seed 42 --save-result --result-dir /tmp --dataset-name random --random-input-len 1024 --random-output-len 4096 --random-range-ratio 0.9 --num-prompts 50 --request-rate 0.2 --burstiness 1.0 --result-filename D_reasoning.json
```

## Results

============ Serving Benchmark Result ============
Successful requests:                     50        
Failed requests:                         0         
Request rate configured (RPS):           0.20      
Benchmark duration (s):                  592.64    
Total input tokens:                      55805     
Total generated tokens:                  209303    
Request throughput (req/s):              0.08      
Output token throughput (tok/s):         353.17    
Peak output token throughput (tok/s):    600.00    
Peak concurrent requests:                41.00     
Total token throughput (tok/s):          447.34    
---------------Time to First Token----------------
Mean TTFT (ms):                          264.41    
Median TTFT (ms):                        256.84    
P50 TTFT (ms):                           256.84    
P90 TTFT (ms):                           345.61    
P95 TTFT (ms):                           381.85    
P99 TTFT (ms):                           499.11    
-----Time per Output Token (excl. 1st token)------
Mean TPOT (ms):                          57.75     
Median TPOT (ms):                        58.78     
P50 TPOT (ms):                           58.78     
P90 TPOT (ms):                           64.07     
P95 TPOT (ms):                           65.20     
P99 TPOT (ms):                           67.23     
---------------Inter-token Latency----------------
Mean ITL (ms):                           57.43     
Median ITL (ms):                         59.24     
P50 ITL (ms):                            59.24     
P90 ITL (ms):                            68.65     
P95 ITL (ms):                            70.03     
P99 ITL (ms):                            72.39     
----------------End-to-end Latency----------------
Mean E2EL (ms):                          240682.02 
Median E2EL (ms):                        241097.43 
P50 E2EL (ms):                           241097.43 
P90 E2EL (ms):                           368961.66 
P95 E2EL (ms):                           406603.63 
P99 E2EL (ms):                           419359.48 
==================================================

---

Volledige log in `D_reasoning.log`. Server-config in `meta.json`.
