# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.6-27B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 15120 ms. Verlaag K_RATES om de bodem te vinden.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.081 | 100/100 | 6841 ms | 15120 ms | 18278 ms | 40 | 29 |
| 0.2 | 0.121 | 100/100 | 12442 ms | 23521 ms | 26321 ms | 60 | 85 |
| 0.3 | 0.134 | 100/100 | 38457 ms | 71876 ms | 76814 ms | 66 | 97 |
| 0.5 | 0.148 | 125/125 | 135731 ms | 252850 ms | 258444 ms | 72 | 122 |
| 0.7 | 0.158 | 175/175 | 232320 ms | 459545 ms | 469628 ms | 77 | 175 |
| 1.0 | 0.17 | 250/250 | 393922 ms | 780836 ms | 809248 ms | 84 | 249 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
