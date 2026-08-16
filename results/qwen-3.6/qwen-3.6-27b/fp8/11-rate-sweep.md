# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.6-27B-FP8
**Profiel:** fp8

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 38628 ms. Verlaag K_RATES om de bodem te vinden.

**Wachtrij-knik bij 0.1 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.087 | 100/100 | 18313 ms | 38628 ms | 42319 ms | 43 | 31 |
| 0.2 | 0.103 | 100/100 | 114927 ms | 226750 ms | 235786 ms | 51 | 98 |
| 0.3 | 0.104 | 100/100 | 207728 ms | 385912 ms | 396113 ms | 51 | 99 |
| 0.5 | 0.108 | 125/125 | 337665 ms | 634143 ms | 655010 ms | 53 | 125 |
| 0.7 | 0.111 | 175/175 | 512102 ms | 999599 ms | 1022155 ms | 54 | 175 |
| 1.0 | 0.114 | 250/250 | 799325 ms | 1546098 ms | 1602871 ms | 56 | 250 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
