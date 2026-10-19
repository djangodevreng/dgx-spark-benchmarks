# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Qwen3.8-Flash-Next-FP4-Local
**Profiel:** nvfp4-b12x

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | **0.2** | 0.177 | 9953 ms | 87 |

**Wachtrij-knik bij 0.2 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.097 | 100/100 | 2980 ms | 7200 ms | 7599 ms | 48 | 14 |
| 0.2 | 0.177 | 100/100 | 4351 ms | 9953 ms | 10340 ms | 87 | 23 |
| 0.3 | 0.195 | 100/100 | 40972 ms | 102844 ms | 113848 ms | 96 | 48 |
| 0.5 | 0.203 | 125/125 | 140354 ms | 285516 ms | 297971 ms | 99 | 88 |
| 0.7 | 0.206 | 175/175 | 255734 ms | 497399 ms | 516191 ms | 101 | 139 |
| 1.0 | 0.207 | 250/250 | 420818 ms | 837703 ms | 880867 ms | 102 | 211 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
