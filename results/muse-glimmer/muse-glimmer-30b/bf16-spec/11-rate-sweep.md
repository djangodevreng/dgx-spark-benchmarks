# Test 11 - rate sweep, capaciteit onder SLO

**Model:** meta-models/Muse-Glimmer-30B
**Profiel:** bf16-spec

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 13180 ms. Verlaag K_RATES om de bodem te vinden.

**Wachtrij-knik bij 0.1 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.072 | 100/100 | 6131 ms | 13180 ms | 16873 ms | 35 | 40 |
| 0.2 | 0.076 | 100/100 | 11392 ms | 25070 ms | 30808 ms | 37 | 89 |
| 0.3 | 0.076 | 100/100 | 19402 ms | 48583 ms | 54695 ms | 37 | 97 |
| 0.5 | 0.079 | 125/125 | 94051 ms | 223929 ms | 233070 ms | 39 | 125 |
| 0.7 | 0.079 | 175/175 | 192208 ms | 510343 ms | 527538 ms | 39 | 175 |
| 1.0 | 0.081 | 250/250 | 370084 ms | 1116349 ms | 1206004 ms | 40 | 250 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
