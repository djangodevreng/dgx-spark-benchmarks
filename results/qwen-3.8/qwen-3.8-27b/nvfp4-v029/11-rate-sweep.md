# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Qwen3.8-27B-NVFP4
**Profiel:** nvfp4-v029

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 23566 ms. Verlaag K_RATES om de bodem te vinden.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.092 | 100/100 | 9888 ms | 23566 ms | 25997 ms | 45 | 20 |
| 0.2 | 0.133 | 100/100 | 40081 ms | 64739 ms | 71256 ms | 65 | 95 |
| 0.3 | 0.133 | 100/100 | 118239 ms | 224437 ms | 231528 ms | 66 | 98 |
| 0.5 | 0.139 | 125/125 | 233748 ms | 437734 ms | 451558 ms | 68 | 125 |
| 0.7 | 0.142 | 175/175 | 368916 ms | 721869 ms | 735690 ms | 69 | 175 |
| 1.0 | 0.145 | 250/250 | 588832 ms | 1150946 ms | 1194104 ms | 71 | 250 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
