# Test 11 - rate sweep, capaciteit onder SLO

**Model:** google/gemma-4-26B-A4B-it
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.7** | 0.429 | 4888 ms | 210 |
| 10 s | **1.0** | 0.531 | 7627 ms | 261 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.095 | 100/100 | 1208 ms | 2301 ms | 2889 ms | 47 | 14 |
| 0.2 | 0.179 | 100/100 | 1366 ms | 2828 ms | 3428 ms | 88 | 20 |
| 0.3 | 0.241 | 100/100 | 1476 ms | 3490 ms | 3983 ms | 119 | 33 |
| 0.5 | 0.357 | 125/125 | 1816 ms | 3632 ms | 4970 ms | 175 | 76 |
| 0.7 | 0.429 | 175/175 | 2167 ms | 4888 ms | 5656 ms | 210 | 129 |
| 1.0 | 0.531 | 250/250 | 3912 ms | 7627 ms | 8782 ms | 261 | 221 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
