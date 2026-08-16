# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Kwaipilot/KAT-Coder-V2.5-Dev
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.5** | 0.32 | 4530 ms | 157 |
| 10 s | **1.0** | 0.472 | 8228 ms | 232 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 1242 ms | 2370 ms | 3294 ms | 47 | 13 |
| 0.2 | 0.176 | 100/100 | 1456 ms | 3169 ms | 3968 ms | 87 | 21 |
| 0.3 | 0.233 | 100/100 | 1694 ms | 3906 ms | 4410 ms | 115 | 41 |
| 0.5 | 0.32 | 125/125 | 2076 ms | 4530 ms | 5042 ms | 157 | 84 |
| 0.7 | 0.386 | 175/175 | 2718 ms | 5372 ms | 6479 ms | 189 | 134 |
| 1.0 | 0.472 | 250/250 | 4730 ms | 8228 ms | 9906 ms | 232 | 223 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
