# Test 11 - rate sweep, capaciteit onder SLO

**Model:** ibm-granite/granite-4.1-8b
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.3** | 0.234 | 4638 ms | 115 |
| 10 s | **0.7** | 0.391 | 8464 ms | 191 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.093 | 100/100 | 1462 ms | 2951 ms | 3686 ms | 46 | 14 |
| 0.2 | 0.173 | 100/100 | 1665 ms | 4081 ms | 4470 ms | 85 | 20 |
| 0.3 | 0.234 | 100/100 | 1820 ms | 4638 ms | 5460 ms | 115 | 32 |
| 0.5 | 0.342 | 125/125 | 2574 ms | 5647 ms | 6734 ms | 167 | 86 |
| 0.7 | 0.391 | 175/175 | 3884 ms | 8464 ms | 9807 ms | 191 | 153 |
| 1.0 | 0.439 | 250/250 | 20198 ms | 37574 ms | 40041 ms | 216 | 247 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
