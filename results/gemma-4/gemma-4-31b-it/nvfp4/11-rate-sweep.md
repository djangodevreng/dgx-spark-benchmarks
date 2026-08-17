# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Gemma-4-31B-IT-NVFP4
**Profiel:** nvfp4

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 26204 ms. Verlaag K_RATES om de bodem te vinden.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.086 | 100/100 | 9902 ms | 26204 ms | 29691 ms | 42 | 28 |
| 0.2 | 0.108 | 100/100 | 34490 ms | 52217 ms | 58907 ms | 53 | 99 |
| 0.3 | 0.108 | 100/100 | 108666 ms | 197192 ms | 200696 ms | 53 | 100 |
| 0.5 | 0.11 | 125/125 | 220764 ms | 404415 ms | 411171 ms | 54 | 125 |
| 0.7 | 0.11 | 175/175 | 343901 ms | 860062 ms | 930360 ms | 54 | 175 |
| 1.0 | 0.11 | 250/250 | 547794 ms | 1525791 ms | 1582492 ms | 54 | 250 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
