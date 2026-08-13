# Test 11 - rate sweep, capaciteit onder SLO

**Model:** mistralai/Mistral-Small-4-119B-2603-NVFP4
**Profiel:** nvfp4

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.3** | 0.219 | 4749 ms | 108 |
| 10 s | **0.7** | 0.332 | 7718 ms | 162 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 1455 ms | 2854 ms | 3970 ms | 47 | 13 |
| 0.2 | 0.175 | 100/100 | 1680 ms | 3737 ms | 5025 ms | 86 | 23 |
| 0.3 | 0.219 | 100/100 | 2027 ms | 4749 ms | 5096 ms | 108 | 46 |
| 0.5 | 0.286 | 125/125 | 2660 ms | 5417 ms | 6812 ms | 140 | 98 |
| 0.7 | 0.332 | 175/175 | 3784 ms | 7718 ms | 8626 ms | 162 | 156 |
| 1.0 | 0.382 | 250/250 | 12028 ms | 19724 ms | 21336 ms | 188 | 244 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
