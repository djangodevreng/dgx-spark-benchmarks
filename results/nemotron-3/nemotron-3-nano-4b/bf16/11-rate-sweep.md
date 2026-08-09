# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16
**Profiel:** bf16

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | **0.3** | 0.272 | 1756 ms | 134 |
| 5 s | **1.0** | 0.756 | 4815 ms | 372 |
| 10 s | **1.0** | 0.756 | 4815 ms | 372 |

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.097 | 100/100 | 787 ms | 1358 ms | 1626 ms | 47 | 7 |
| 0.2 | 0.187 | 100/100 | 816 ms | 1634 ms | 2073 ms | 92 | 14 |
| 0.3 | 0.272 | 100/100 | 867 ms | 1756 ms | 2191 ms | 134 | 15 |
| 0.5 | 0.449 | 125/125 | 948 ms | 2030 ms | 2721 ms | 220 | 24 |
| 0.7 | 0.597 | 175/175 | 1094 ms | 2191 ms | 2981 ms | 292 | 42 |
| 1.0 | 0.756 | 250/250 | 1935 ms | 4815 ms | 6312 ms | 372 | 133 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
