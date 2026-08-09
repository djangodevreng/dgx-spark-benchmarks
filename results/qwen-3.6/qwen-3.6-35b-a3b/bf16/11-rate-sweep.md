# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.6-35B-A3B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.3** | 0.233 | 4687 ms | 115 |
| 10 s | **0.5** | 0.324 | 6835 ms | 159 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 1659 ms | 3360 ms | 3898 ms | 47 | 13 |
| 0.2 | 0.177 | 100/100 | 1949 ms | 4067 ms | 5482 ms | 87 | 21 |
| 0.3 | 0.233 | 100/100 | 2323 ms | 4687 ms | 5980 ms | 115 | 42 |
| 0.5 | 0.324 | 125/125 | 3259 ms | 6835 ms | 7447 ms | 159 | 86 |
| 0.7 | 0.387 | 175/175 | 5644 ms | 11310 ms | 15248 ms | 189 | 136 |
| 1.0 | 0.44 | 250/250 | 44033 ms | 94123 ms | 96178 ms | 216 | 221 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
