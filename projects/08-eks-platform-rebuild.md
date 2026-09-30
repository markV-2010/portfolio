[← 포트폴리오](../README.md) · [트렌비](../companies/trenbe.md)

# EKS 플랫폼 리빌드와 가용성 99.98%

> 레거시 위에 EKS 플랫폼을 신규 구축하고 Chaos Engineering을 상시화해, **비용을 줄이면서 가용성을 올렸습니다.**

| 조직 | 시기 | 역할 |
|---|---|---|
| 트렌비 | 2021.06 – 2024.12 | SRE Lead — 설계 · 구축 · 운영 |

**출발점** — 쿠버네티스 플랫폼 없음. 배포 흐름도 환경 분리도 정립돼 있지 않음.

---

## 문제

서비스는 레거시 위에서 돌고 있었고, 그 위에서 할 수 있는 개선은 한계에 닿아 있었습니다.

- 배포가 수작업 비중이 높아 되돌리기 어려웠습니다.
- dev / stage / prod 환경의 구성이 서로 달라, Staging에서의 검증이 prod를 보장하지 못했습니다.
- 장애 내성이 **검증된 적이 없었습니다.** 이중화가 되어 있다고 믿었지만 실제로 내려본 적이 없었습니다.

## 제약

- **서비스를 멈출 수 없었습니다.** 레거시를 걷어내고 새로 짓는 방식은 불가능했습니다.
- 같은 기간에 [비용을 43.9% 줄여야](09-cloud-cost-optimization.md) 했습니다. 가용성을 돈으로 사는 선택지가 없었습니다.
- 플랫폼 전담 인력이 없었습니다. 운영 부담이 큰 구성은 도입해도 유지가 안 됩니다.

## 설계

### 1. 레거시 위에 신규 플랫폼을 올렸다

교체가 아니라 병존으로 시작했습니다. EKS 플랫폼을 신규 구축하고, 워크로드를 순차 이전하는 방식입니다.

**플랫폼 구성**

| 영역 | 선택 |
|---|---|
| 배포 | ArgoCD, Argo Workflows |
| 서비스 메시 | Istio · Kiali |
| 관측 | Prometheus · Grafana · **Loki** |
| 접근 | Teleport |
| 레지스트리 | Harbor |
| DB | Percona |

Loki와 Percona는 [비용 최적화](09-cloud-cost-optimization.md)와 맞물린 선택이었습니다.
ElasticSearch → Loki + Promtail, 상용 DB → Percona로 가면서 **상용 제품 종속성과 비용을 동시에** 줄였습니다.

### 2. GitOps와 환경 정합성

- GitOps 파이프라인으로 배포를 선언적으로 전환 — 되돌리기가 커밋 단위가 됨
- dev / stage / prod 데이터·배포 흐름 정의
- **Argo Workflows 연동 Staging(QA) 환경 구축** — Staging이 prod 구성을 실제로 반영하게 만듦

### 3. 장애 내성을 믿지 않고 검증했다

이 플랫폼에서 가장 중요한 결정입니다. **이중화를 주장하지 않고 상시 검증했습니다.**

| 시나리오 | 방식 |
|---|---|
| Instance Fail | 상시 검증 |
| Zone Fail | **Active** — 실제 장애 시 서비스 지속 |
| Region Fail | **Standby** — 복구 절차 검증 |

Zone은 Active로, Region은 Standby로 둔 것은 비용 판단이었습니다.
Region Active는 비용이 배로 드는데, 당시 서비스의 손실 규모가 그것을 정당화하지 못했습니다.
대신 **Standby 복구 절차를 주기적으로 검증**해서 "있다고 믿는 DR"이 되지 않게 했습니다.

### 4. 네트워크 재설계

- Multi VPC, Transit Gateway (Multi Region)
- Site-to-Site IPSec
- **IAM Rebuild** — 권한을 처음부터 다시 설계
- Private 전환 — 80/443 외 차단

---

## 결과

> **가용성 99.98%** — 같은 기간 월 인프라 비용 43.9% 절감

- 배포가 선언적으로 바뀌면서 롤백이 절차에서 커밋으로 내려옴
- Staging 검증이 prod를 실제로 반영하게 됨
- 장애 내성이 **주장이 아니라 검증 결과**가 됨

## 회고

**"가용성과 비용은 트레이드오프"라는 말은 절반만 맞습니다.**
같은 기간에 비용을 43.9% 줄이면서 99.98%를 확보할 수 있었던 건,
기존 지출의 상당 부분이 가용성이 아니라 **검증되지 않은 안심**에 쓰이고 있었기 때문입니다.
실제로 내려보면 필요한 것과 필요 없는 것이 갈립니다.

**Region을 Standby로 둔 판단은 지금도 같게 하겠습니다.** 다만 그때 배운 건,
Standby는 검증 주기를 정해 두지 않으면 사실상 없는 것과 같다는 점입니다.

이때의 Instance / Zone / Region 검증 체계가 이후
[무신사의 복구 시나리오 상시 검증과 모의훈련 프로그램](03-incident-drill-program.md)으로 이어집니다.

---

**관련 케이스** — [클라우드 비용 최적화](09-cloud-cost-optimization.md) · [클라우드 보안 프레임워크](07-cloud-security-framework.md) · [비상대응훈련 프로그램](03-incident-drill-program.md)

`AWS EKS` `ArgoCD` `Argo Workflows` `Istio/Kiali` `Prometheus` `Grafana` `Loki` `Teleport` `Harbor` `Percona`
`Transit Gateway` `IPSec` `GitOps` `Chaos Engineering`
