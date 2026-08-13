# Test 11 - rate sweep, capaciteit onder SLO

**Model:** meta-models/Muse-Glimmer-30B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 10659 ms. Verlaag K_RATES om de bodem te vinden.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.082 | 100/100 | 4476 ms | 10659 ms | 13031 ms | 40 | 24 |
| 0.2 | 0.114 | 100/100 | 7580 ms | 15878 ms | 19242 ms | 56 | 85 |
| 0.3 | 0.124 | 100/100 | 12225 ms | 22944 ms | 25254 ms | 61 | 97 |
| 0.5 | 0.134 | 125/125 | 73328 ms | 139247 ms | 140784 ms | 66 | 125 |
| 0.7 | 0.14 | 175/175 | 148362 ms | 299464 ms | 305662 ms | 68 | 175 |
| 1.0 | 0.146 | 250/250 | 270784 ms | 557280 ms | 580367 ms | 72 | 250 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
