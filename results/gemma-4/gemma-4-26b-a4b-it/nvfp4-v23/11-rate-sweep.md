# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Gemma-4-26B-A4B-NVFP4
**Profiel:** nvfp4-v23

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.1** | 0.097 | 1973 ms | 48 |
| 5 s | **0.7** | 0.547 | 3818 ms | 268 |
| 10 s | **1.0** | 0.671 | 6096 ms | 330 |

**Wachtrij-knik bij 0.7 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.097 | 100/100 | 1030 ms | 1973 ms | 2793 ms | 48 | 8 |
| 0.2 | 0.187 | 100/100 | 1113 ms | 2225 ms | 2853 ms | 92 | 15 |
| 0.3 | 0.271 | 100/100 | 1154 ms | 2827 ms | 3347 ms | 133 | 20 |
| 0.5 | 0.437 | 125/125 | 1382 ms | 3138 ms | 3907 ms | 214 | 45 |
| 0.7 | 0.547 | 175/175 | 1581 ms | 3818 ms | 4457 ms | 268 | 83 |
| 1.0 | 0.671 | 250/250 | 2738 ms | 6096 ms | 7145 ms | 330 | 190 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
