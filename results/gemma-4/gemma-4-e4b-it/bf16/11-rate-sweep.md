# Test 11 - rate sweep, capaciteit onder SLO

**Model:** google/gemma-4-E4B-it
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.2** | 0.184 | 1886 ms | 90 |
| 5 s | **1.0** | 0.796 | 4063 ms | 392 |
| 10 s | **1.0** | 0.796 | 4063 ms | 392 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 897 ms | 1683 ms | 2010 ms | 47 | 8 |
| 0.2 | 0.184 | 100/100 | 914 ms | 1886 ms | 2362 ms | 90 | 15 |
| 0.3 | 0.265 | 100/100 | 1013 ms | 2169 ms | 2694 ms | 130 | 17 |
| 0.5 | 0.436 | 125/125 | 1084 ms | 2589 ms | 3115 ms | 214 | 31 |
| 0.7 | 0.583 | 175/175 | 1181 ms | 2631 ms | 3278 ms | 285 | 52 |
| 1.0 | 0.796 | 250/250 | 1778 ms | 4063 ms | 4536 ms | 392 | 130 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
