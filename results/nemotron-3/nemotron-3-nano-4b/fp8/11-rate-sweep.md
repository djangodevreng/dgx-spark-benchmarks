# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-FP8
**Profiel:** fp8

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.7** | 0.632 | 1574 ms | 309 |
| 5 s | **1.0** | 0.869 | 2350 ms | 427 |
| 10 s | **1.0** | 0.869 | 2350 ms | 427 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.098 | 100/100 | 634 ms | 1153 ms | 1344 ms | 48 | 5 |
| 0.2 | 0.192 | 100/100 | 620 ms | 1181 ms | 1457 ms | 94 | 10 |
| 0.3 | 0.282 | 100/100 | 644 ms | 1199 ms | 1334 ms | 138 | 14 |
| 0.5 | 0.467 | 125/125 | 717 ms | 1508 ms | 1840 ms | 228 | 17 |
| 0.7 | 0.632 | 175/175 | 866 ms | 1574 ms | 2210 ms | 309 | 28 |
| 1.0 | 0.869 | 250/250 | 1105 ms | 2350 ms | 2975 ms | 427 | 75 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
