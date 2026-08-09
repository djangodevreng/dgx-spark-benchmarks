# Test 11 - rate sweep, capaciteit onder SLO

**Model:** mistralai/Ministral-3-8B-Instruct-2512
**Profiel:** bf16

> **Sweep afgekapt bij 0.2 req/s: de server viel weg.** De treden daarboven zijn niet gemeten, dus de capaciteit hieronder is een ondergrens, geen gevonden plafond. Zie `_server-crash.log`.

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.1** | 0.096 | 2675 ms | 47 |
| 10 s | **0.1** | 0.096 | 2675 ms | 47 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 1492 ms | 2675 ms | 3363 ms | 47 | 8 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
