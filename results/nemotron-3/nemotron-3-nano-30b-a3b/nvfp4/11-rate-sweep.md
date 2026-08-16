# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4
**Profiel:** nvfp4

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.2** | 0.194 | 1828 ms | 95 |
| 5 s | **1.0** | 0.774 | 4367 ms | 381 |
| 10 s | **1.0** | 0.774 | 4367 ms | 381 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.099 | 100/100 | 892 ms | 1669 ms | 1973 ms | 48 | 5 |
| 0.2 | 0.194 | 100/100 | 925 ms | 1828 ms | 2307 ms | 95 | 13 |
| 0.3 | 0.283 | 100/100 | 986 ms | 2162 ms | 2605 ms | 139 | 15 |
| 0.5 | 0.462 | 125/125 | 1121 ms | 2594 ms | 3104 ms | 226 | 31 |
| 0.7 | 0.6 | 175/175 | 1209 ms | 2702 ms | 3674 ms | 293 | 57 |
| 1.0 | 0.774 | 250/250 | 1978 ms | 4367 ms | 4636 ms | 381 | 145 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
