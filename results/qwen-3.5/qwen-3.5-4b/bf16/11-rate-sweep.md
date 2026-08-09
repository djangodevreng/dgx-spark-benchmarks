# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.5-4B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.1** | 0.096 | 1765 ms | 47 |
| 5 s | **0.7** | 0.58 | 2967 ms | 283 |
| 10 s | **1.0** | 0.736 | 6611 ms | 362 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 942 ms | 1765 ms | 2112 ms | 47 | 8 |
| 0.2 | 0.185 | 100/100 | 1003 ms | 2045 ms | 2418 ms | 91 | 15 |
| 0.3 | 0.267 | 100/100 | 1067 ms | 2358 ms | 2873 ms | 131 | 17 |
| 0.5 | 0.441 | 125/125 | 1150 ms | 2575 ms | 3215 ms | 216 | 31 |
| 0.7 | 0.58 | 175/175 | 1398 ms | 2967 ms | 3734 ms | 283 | 57 |
| 1.0 | 0.736 | 250/250 | 2766 ms | 6611 ms | 8151 ms | 362 | 150 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
