# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.5-0.8B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **1.0** | 0.97 | 521 ms | 477 |
| 5 s | **1.0** | 0.97 | 521 ms | 477 |
| 10 s | **1.0** | 0.97 | 521 ms | 477 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.099 | 100/100 | 218 ms | 377 ms | 454 ms | 49 | 4 |
| 0.2 | 0.197 | 100/100 | 236 ms | 384 ms | 492 ms | 97 | 5 |
| 0.3 | 0.293 | 100/100 | 237 ms | 407 ms | 507 ms | 144 | 5 |
| 0.5 | 0.488 | 125/125 | 241 ms | 426 ms | 546 ms | 239 | 7 |
| 0.7 | 0.683 | 175/175 | 243 ms | 475 ms | 607 ms | 334 | 12 |
| 1.0 | 0.97 | 250/250 | 242 ms | 521 ms | 689 ms | 477 | 14 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
