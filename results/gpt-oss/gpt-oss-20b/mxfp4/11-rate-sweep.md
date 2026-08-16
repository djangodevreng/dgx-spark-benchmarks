# Test 11 - rate sweep, capaciteit onder SLO

**Model:** openai/gpt-oss-20b
**Profiel:** mxfp4

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.3** | 0.279 | 1732 ms | 108 |
| 5 s | **1.0** | 0.863 | 3289 ms | 324 |
| 10 s | **1.0** | 0.863 | 3289 ms | 324 |

**Wachtrij-knik bij 0.7 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.1 | 100/100 | 747 ms | 1382 ms | 2057 ms | 15 | 5 |
| 0.2 | 0.191 | 100/100 | 793 ms | 1585 ms | 2030 ms | 59 | 11 |
| 0.3 | 0.279 | 100/100 | 834 ms | 1732 ms | 2340 ms | 108 | 10 |
| 0.5 | 0.47 | 125/125 | 943 ms | 2166 ms | 2728 ms | 196 | 22 |
| 0.7 | 0.609 | 175/175 | 979 ms | 2254 ms | 2876 ms | 276 | 36 |
| 1.0 | 0.863 | 250/250 | 1265 ms | 3289 ms | 3535 ms | 324 | 74 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
