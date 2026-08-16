# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.8-27B-FP8
**Profiel:** fp8

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 39632 ms. Verlaag K_RATES om de bodem te vinden.

**Wachtrij-knik bij 0.1 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.087 | 100/100 | 18499 ms | 39632 ms | 44679 ms | 43 | 31 |
| 0.2 | 0.103 | 100/100 | 115962 ms | 228815 ms | 237804 ms | 51 | 98 |
| 0.3 | 0.103 | 100/100 | 208833 ms | 388586 ms | 399039 ms | 51 | 99 |
| 0.5 | 0.108 | 125/125 | 338874 ms | 639609 ms | 660652 ms | 53 | 125 |
| 0.7 | 0.11 | 175/175 | 515134 ms | 1005888 ms | 1025174 ms | 54 | 175 |
| 1.0 | 0.113 | 250/250 | 802450 ms | 1555960 ms | 1614355 ms | 56 | 250 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
