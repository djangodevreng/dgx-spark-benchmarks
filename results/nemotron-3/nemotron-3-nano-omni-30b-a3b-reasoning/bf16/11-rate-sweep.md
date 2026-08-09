# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.1** | 0.096 | 1760 ms | 47 |
| 5 s | **0.7** | 0.442 | 3647 ms | 216 |
| 10 s | **1.0** | 0.555 | 5908 ms | 273 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.096 | 100/100 | 957 ms | 1760 ms | 2128 ms | 47 | 14 |
| 0.2 | 0.179 | 100/100 | 1147 ms | 2298 ms | 2598 ms | 88 | 20 |
| 0.3 | 0.246 | 100/100 | 1246 ms | 2557 ms | 2962 ms | 121 | 33 |
| 0.5 | 0.358 | 125/125 | 1548 ms | 2970 ms | 3491 ms | 175 | 75 |
| 0.7 | 0.442 | 175/175 | 1854 ms | 3647 ms | 4235 ms | 216 | 125 |
| 1.0 | 0.555 | 250/250 | 2790 ms | 5908 ms | 6911 ms | 273 | 209 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
