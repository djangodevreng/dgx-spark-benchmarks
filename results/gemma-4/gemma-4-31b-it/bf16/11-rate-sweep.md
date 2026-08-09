# Test 11 - rate sweep, capaciteit onder SLO

**Model:** google/gemma-4-31B-it
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 19474 ms. Verlaag K_RATES om de bodem te vinden.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.076 | 100/100 | 7897 ms | 19474 ms | 21935 ms | 38 | 42 |
| 0.2 | 0.101 | 100/100 | 16448 ms | 88350 ms | 94568 ms | 50 | 90 |
| 0.3 | 0.103 | 100/100 | 57194 ms | 222385 ms | 246494 ms | 51 | 100 |
| 0.5 | 0.111 | 125/125 | 160542 ms | 511140 ms | 538189 ms | 54 | 125 |
| 0.7 | 0.113 | 175/175 | 323663 ms | 897048 ms | 922524 ms | 55 | 175 |
| 1.0 | 0.117 | 250/250 | 684877 ms | 1419709 ms | 1489279 ms | 58 | 250 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
