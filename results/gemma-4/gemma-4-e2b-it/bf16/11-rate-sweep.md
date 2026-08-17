# Test 11 - rate sweep, capaciteit onder SLO

**Model:** google/gemma-4-E2B-it
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **1.0** | 0.918 | 1691 ms | 452 |
| 5 s | **1.0** | 0.918 | 1691 ms | 452 |
| 10 s | **1.0** | 0.918 | 1691 ms | 452 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.098 | 100/100 | 523 ms | 914 ms | 1451 ms | 48 | 5 |
| 0.2 | 0.191 | 100/100 | 560 ms | 1044 ms | 1274 ms | 94 | 8 |
| 0.3 | 0.281 | 100/100 | 568 ms | 1152 ms | 1390 ms | 138 | 13 |
| 0.5 | 0.466 | 125/125 | 570 ms | 1246 ms | 1699 ms | 228 | 15 |
| 0.7 | 0.648 | 175/175 | 586 ms | 1334 ms | 1731 ms | 316 | 20 |
| 1.0 | 0.918 | 250/250 | 670 ms | 1691 ms | 2054 ms | 452 | 35 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
