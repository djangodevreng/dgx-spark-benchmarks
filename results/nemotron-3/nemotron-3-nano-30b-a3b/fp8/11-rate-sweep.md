# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8
**Profiel:** fp8

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.2** | 0.19 | 1794 ms | 93 |
| 5 s | **1.0** | 0.847 | 3748 ms | 139 |
| 10 s | **1.0** | 0.847 | 3748 ms | 139 |

**Wachtrij-knik bij 0.7 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.098 | 100/100 | 860 ms | 1644 ms | 1948 ms | 48 | 8 |
| 0.2 | 0.19 | 100/100 | 925 ms | 1794 ms | 2408 ms | 93 | 14 |
| 0.3 | 0.27 | 100/100 | 1032 ms | 2195 ms | 2662 ms | 133 | 20 |
| 0.5 | 0.418 | 125/125 | 1210 ms | 2452 ms | 3072 ms | 205 | 54 |
| 0.7 | 0.517 | 175/175 | 1752 ms | 3141 ms | 3435 ms | 253 | 98 |
| 1.0 | 0.847 | 250/250 | 1902 ms | 3748 ms | 4441 ms | 139 | 200 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
