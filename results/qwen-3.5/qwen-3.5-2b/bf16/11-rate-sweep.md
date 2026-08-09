# Test 11 - rate sweep, capaciteit onder SLO

**Model:** Qwen/Qwen3.5-2B
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **1.0** | 0.929 | 1042 ms | 457 |
| 5 s | **1.0** | 0.929 | 1042 ms | 457 |
| 10 s | **1.0** | 0.929 | 1042 ms | 457 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.098 | 100/100 | 386 ms | 614 ms | 786 ms | 48 | 5 |
| 0.2 | 0.192 | 100/100 | 402 ms | 706 ms | 830 ms | 94 | 7 |
| 0.3 | 0.282 | 100/100 | 409 ms | 752 ms | 914 ms | 139 | 10 |
| 0.5 | 0.47 | 125/125 | 410 ms | 828 ms | 1062 ms | 230 | 13 |
| 0.7 | 0.658 | 175/175 | 416 ms | 873 ms | 1141 ms | 321 | 16 |
| 1.0 | 0.929 | 250/250 | 449 ms | 1042 ms | 1293 ms | 457 | 26 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
