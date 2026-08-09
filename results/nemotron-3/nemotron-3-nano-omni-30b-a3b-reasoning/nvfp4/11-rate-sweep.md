# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4
**Profiel:** nvfp4

> **Sweep afgekapt bij 0.5 req/s: de server viel weg.** De treden daarboven zijn niet gemeten, dus de capaciteit hieronder is een ondergrens, geen gevonden plafond. Zie `_server-crash.log`.

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.1** | 0.099 | 1705 ms | 48 |
| 5 s | **0.3** | 0.283 | 3177 ms | 139 |
| 10 s | **0.3** | 0.283 | 3177 ms | 139 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.099 | 100/100 | 974 ms | 1705 ms | 2837 ms | 48 | 5 |
| 0.2 | 0.193 | 100/100 | 940 ms | 2105 ms | 2545 ms | 95 | 13 |
| 0.3 | 0.283 | 100/100 | 1391 ms | 3177 ms | 7079 ms | 139 | 18 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
