# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.6-35B-A3B-FP8
**Profiel:** fp8

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.3** | 0.268 | 4396 ms | 132 |
| 10 s | **0.7** | 0.478 | 8131 ms | 233 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.098 | 100/100 | 1406 ms | 2808 ms | 3412 ms | 48 | 7 |
| 0.2 | 0.19 | 100/100 | 1586 ms | 3482 ms | 4380 ms | 93 | 14 |
| 0.3 | 0.268 | 100/100 | 1862 ms | 4396 ms | 4991 ms | 132 | 20 |
| 0.5 | 0.404 | 125/125 | 2447 ms | 5257 ms | 6197 ms | 198 | 66 |
| 0.7 | 0.478 | 175/175 | 3901 ms | 8131 ms | 10570 ms | 233 | 124 |
| 1.0 | 0.542 | 250/250 | 30592 ms | 66083 ms | 68560 ms | 266 | 207 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
