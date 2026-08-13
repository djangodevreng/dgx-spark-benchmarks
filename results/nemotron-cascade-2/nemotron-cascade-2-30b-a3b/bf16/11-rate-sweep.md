# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Nemotron-Cascade-2-30B-A3B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **1.0** | 0.527 | 4303 ms | 259 |
| 10 s | **1.0** | 0.527 | 4303 ms | 259 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 988 ms | 2132 ms | 2775 ms | 47 | 14 |
| 0.2 | 0.174 | 100/100 | 1182 ms | 2339 ms | 2537 ms | 86 | 23 |
| 0.3 | 0.231 | 100/100 | 1264 ms | 2639 ms | 2963 ms | 113 | 39 |
| 0.5 | 0.328 | 125/125 | 1495 ms | 2870 ms | 3327 ms | 161 | 76 |
| 0.7 | 0.406 | 175/175 | 1684 ms | 3132 ms | 3718 ms | 198 | 121 |
| 1.0 | 0.527 | 250/250 | 2334 ms | 4303 ms | 4828 ms | 259 | 196 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
