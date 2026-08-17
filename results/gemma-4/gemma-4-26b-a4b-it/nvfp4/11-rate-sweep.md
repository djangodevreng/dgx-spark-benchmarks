# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Profiel:** nvfp4

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.1** | 0.097 | 1966 ms | 48 |
| 5 s | **0.7** | 0.554 | 3676 ms | 271 |
| 10 s | **1.0** | 0.653 | 6209 ms | 321 |

**Wachtrij-knik bij 0.7 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.097 | 100/100 | 1013 ms | 1966 ms | 2793 ms | 48 | 8 |
| 0.2 | 0.188 | 100/100 | 1072 ms | 2205 ms | 2889 ms | 92 | 15 |
| 0.3 | 0.272 | 100/100 | 1139 ms | 2503 ms | 3356 ms | 134 | 19 |
| 0.5 | 0.437 | 125/125 | 1364 ms | 3037 ms | 3796 ms | 214 | 44 |
| 0.7 | 0.554 | 175/175 | 1553 ms | 3676 ms | 4176 ms | 271 | 81 |
| 1.0 | 0.653 | 250/250 | 2884 ms | 6209 ms | 7080 ms | 321 | 196 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
