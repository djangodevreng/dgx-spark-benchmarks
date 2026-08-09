# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.1** | 0.096 | 1755 ms | 47 |
| 5 s | **1.0** | 0.543 | 4441 ms | 267 |
| 10 s | **1.0** | 0.543 | 4441 ms | 267 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 957 ms | 1755 ms | 2137 ms | 47 | 14 |
| 0.2 | 0.176 | 100/100 | 1131 ms | 2322 ms | 2598 ms | 87 | 22 |
| 0.3 | 0.24 | 100/100 | 1209 ms | 2462 ms | 2943 ms | 118 | 34 |
| 0.5 | 0.348 | 125/125 | 1501 ms | 2866 ms | 3305 ms | 170 | 76 |
| 0.7 | 0.415 | 175/175 | 1713 ms | 3075 ms | 3680 ms | 203 | 122 |
| 1.0 | 0.543 | 250/250 | 2301 ms | 4441 ms | 5046 ms | 267 | 198 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
