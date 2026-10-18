# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4
**Profiel:** nvfp4-v031

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | **0.3** | 0.251 | 8772 ms | 123 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.097 | 100/100 | 2703 ms | 5537 ms | 6965 ms | 48 | 12 |
| 0.2 | 0.183 | 100/100 | 3356 ms | 7795 ms | 8647 ms | 90 | 19 |
| 0.3 | 0.251 | 100/100 | 4338 ms | 8772 ms | 10094 ms | 123 | 30 |
| 0.5 | 0.349 | 125/125 | 14790 ms | 34486 ms | 37355 ms | 171 | 81 |
| 0.7 | 0.365 | 175/175 | 66630 ms | 132573 ms | 136301 ms | 178 | 126 |
| 1.0 | 0.383 | 250/250 | 149261 ms | 294698 ms | 303023 ms | 189 | 198 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
