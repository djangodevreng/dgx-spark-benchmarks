# Test 11 - rate sweep, capaciteit onder SLO

**Model:** RedHatAI/Qwen3.6-35B-A3B-NVFP4
**Profiel:** nvfp4

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.1** | 0.098 | 1986 ms | 48 |
| 5 s | **0.7** | 0.557 | 3821 ms | 272 |
| 10 s | **0.7** | 0.557 | 3821 ms | 272 |

**Wachtrij-knik bij 0.7 req/s.** Daarboven groeit de gelijktijdigheid sneller dan de doorvoer, dus extra vraag levert vooral wachttijd op.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.098 | 100/100 | 1036 ms | 1986 ms | 2444 ms | 48 | 6 |
| 0.2 | 0.191 | 100/100 | 1084 ms | 2359 ms | 2804 ms | 94 | 14 |
| 0.3 | 0.277 | 100/100 | 1213 ms | 2700 ms | 3299 ms | 136 | 18 |
| 0.5 | 0.444 | 125/125 | 1474 ms | 3221 ms | 4092 ms | 218 | 39 |
| 0.7 | 0.557 | 175/175 | 1826 ms | 3821 ms | 4684 ms | 272 | 73 |
| 1.0 | 0.684 | 250/250 | 4671 ms | 12623 ms | 14823 ms | 337 | 169 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
