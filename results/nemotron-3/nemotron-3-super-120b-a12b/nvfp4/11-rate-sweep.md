# Test 11 - rate sweep, capaciteit onder SLO

**Model:** nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
**Profiel:** nvfp4

## Capaciteit

| p95 TTFT onder | rate (req/s) | daadwerkelijk | p95 gemeten | output tok/s |
| ---: | ---: | ---: | ---: | ---: |
| 2 s | geen enkele trede | | | |
| 5 s | geen enkele trede | | | |
| 10 s | geen enkele trede | | | |

Zelfs de laagste trede bleef niet onder de soepelste grens. Laagst gemeten p95 TTFT: 14391 ms. Verlaag K_RATES om de bodem te vinden.

## Alle treden

| rate | gehaald | voltooid | p50 | p95 | p99 | output tok/s | piek gelijktijdig |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.1 | 0.093 | 100/100 | 6516 ms | 14391 ms | 16340 ms | 46 | 19 |
| 0.2 | 0.132 | 100/100 | 66318 ms | 167767 ms | 179598 ms | 65 | 46 |
| 0.3 | 0.134 | 100/100 | 158197 ms | 325063 ms | 339667 ms | 66 | 68 |
| 0.5 | 0.131 | 125/125 | 272730 ms | 570648 ms | 597739 ms | 64 | 103 |
| 0.7 | 0.139 | 175/175 | 454364 ms | 875628 ms | 909863 ms | 68 | 153 |
| 1.0 | 0.14 | 250/250 | 705471 ms | 1377886 ms | 1446093 ms | 69 | 224 |

---

Ruwe cijfers per trede in `11-rate-sweep-<rate>.json`.
