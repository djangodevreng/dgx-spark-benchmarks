# Test 11 - rate sweep, capaciteit onder SLO

**Model:** mistralai/Ministral-3-3B-Instruct-2512
**Profiel:** bf16

> **Sweep afgekapt bij 1.0 req/s: de server viel weg.** De treden daarboven zijn niet gemeten, dus de capaciteit hieronder is een ondergrens, geen gevonden plafond. Zie `_server-crash.log`.

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.3** | 0.281 | 1567 ms | 138 |
| 5 s | **0.5** | 0.461 | 2050 ms | 225 |
| 10 s | **0.5** | 0.461 | 2050 ms | 225 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.098 | 100/100 | 660 ms | 1061 ms | 1373 ms | 48 | 5 |
| 0.2 | 0.192 | 100/100 | 666 ms | 1186 ms | 1404 ms | 95 | 13 |
| 0.3 | 0.281 | 100/100 | 755 ms | 1567 ms | 1981 ms | 138 | 14 |
| 0.5 | 0.461 | 125/125 | 1098 ms | 2050 ms | 2285 ms | 225 | 37 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
