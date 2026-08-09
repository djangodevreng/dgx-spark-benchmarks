# Test 11 - rate sweep, capaciteit onder SLO

**Model:** google/gemma-4-26B-A4B-it
**Profiel:** bf16-v23

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | **0.7** | 0.437 | 4578 ms | 213 |
| 10 s | **1.0** | 0.527 | 7628 ms | 259 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.095 | 100/100 | 1211 ms | 2302 ms | 2878 ms | 47 | 14 |
| 0.2 | 0.178 | 100/100 | 1356 ms | 2876 ms | 3347 ms | 88 | 20 |
| 0.3 | 0.241 | 100/100 | 1495 ms | 3234 ms | 3841 ms | 118 | 32 |
| 0.5 | 0.357 | 125/125 | 1818 ms | 3591 ms | 4857 ms | 175 | 77 |
| 0.7 | 0.437 | 175/175 | 2189 ms | 4578 ms | 5364 ms | 213 | 129 |
| 1.0 | 0.527 | 250/250 | 3956 ms | 7628 ms | 8807 ms | 259 | 221 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
