# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.8-27B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 16397 ms. Verlaag K_RATES om de bodem te vinden.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.081 | 100/100 | 6752 ms | 16397 ms | 18190 ms | 40 | 29 |
| 0.2 | 0.122 | 100/100 | 12185 ms | 23396 ms | 27495 ms | 60 | 85 |
| 0.3 | 0.134 | 100/100 | 39068 ms | 72849 ms | 77744 ms | 66 | 97 |
| 0.5 | 0.148 | 125/125 | 136221 ms | 254833 ms | 260720 ms | 72 | 122 |
| 0.7 | 0.158 | 175/175 | 233492 ms | 459858 ms | 469146 ms | 77 | 175 |
| 1.0 | 0.169 | 250/250 | 393804 ms | 801392 ms | 838941 ms | 83 | 249 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
