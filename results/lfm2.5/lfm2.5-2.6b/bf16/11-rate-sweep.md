# Test 11 - rate sweep, capaciteit onder SLO

**Model:** LiquidAI/LFM2.5-2.6B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **1.0** | 0.909 | 1357 ms | 447 |
| 5 s | **1.0** | 0.909 | 1357 ms | 447 |
| 10 s | **1.0** | 0.909 | 1357 ms | 447 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.097 | 100/100 | 473 ms | 772 ms | 1221 ms | 48 | 5 |
| 0.2 | 0.19 | 100/100 | 482 ms | 891 ms | 1044 ms | 93 | 8 |
| 0.3 | 0.278 | 100/100 | 484 ms | 931 ms | 1148 ms | 137 | 14 |
| 0.5 | 0.462 | 125/125 | 498 ms | 1061 ms | 1317 ms | 226 | 15 |
| 0.7 | 0.642 | 175/175 | 514 ms | 1072 ms | 1409 ms | 314 | 20 |
| 1.0 | 0.909 | 250/250 | 566 ms | 1357 ms | 1602 ms | 447 | 35 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
