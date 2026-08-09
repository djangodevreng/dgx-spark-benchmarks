# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.5-9B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.3** | 0.244 | 4512 ms | 120 |
| 10 s | **0.7** | 0.469 | 9335 ms | 229 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.093 | 100/100 | 1622 ms | 3338 ms | 3850 ms | 46 | 14 |
| 0.2 | 0.175 | 100/100 | 1766 ms | 3977 ms | 4930 ms | 86 | 19 |
| 0.3 | 0.244 | 100/100 | 1884 ms | 4512 ms | 5214 ms | 120 | 26 |
| 0.5 | 0.384 | 125/125 | 2591 ms | 5674 ms | 6385 ms | 188 | 69 |
| 0.7 | 0.469 | 175/175 | 4365 ms | 9335 ms | 11925 ms | 229 | 129 |
| 1.0 | 0.529 | 250/250 | 39266 ms | 82935 ms | 84944 ms | 260 | 215 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
