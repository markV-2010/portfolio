[← 포트폴리오](../README.md)

# 트렌비

**SRE Lead 겸 정보보호최고책임자(CISO) · 개인정보보호책임자(CPO)**
`2021.06 – 2024.12` · CISO 선임 2024.06

---

## 이 시기의 상황

대부분 '없는 상태'에서 시작했습니다 — 보안 프레임워크도, 쿠버네티스 플랫폼도, 데이터 파이프라인도, 비용 관리 체계도.
인프라 비용은 우상향 중이었고, 명목상 MSP에 운영을 맡기고 있었지만 실제 통제권은 안에도 밖에도 없었습니다.

## 맡은 범위

플랫폼 신뢰성 · 정보보호 · 개인정보보호 · 클라우드 비용.
네 개를 한 사람이 맡는 구조였고, 그래서 **보안 요구사항과 비용 구조와 가용성 설계를 하나의 판단으로 묶을 수 있었습니다.**

## 케이스

- **[보안 거버넌스 — 정보보호위원회와 조직 리딩](../projects/13-security-governance.md)** — 정보보호위원회 운영, 약관에 고지된 공식 CPO, 정책 체계 수립
- **[개인정보 유출 사고 대응](../projects/06-privacy-incident-response.md)** — CPO로서 규제기관 현장점검까지 지휘, 과징금 없이 종결, 이후 3년간 시정조치·개선권고 이행보고
- **[클라우드 보안 프레임워크 · ISMS-P](../projects/07-cloud-security-framework.md)** — Layer × Component 매트릭스, Identity 기반 망분리
- **[EKS 플랫폼 리빌드](../projects/08-eks-platform-rebuild.md)** — 가용성 99.98%, Instance/Zone/Region Fail 상시 검증
- **[클라우드 비용 최적화와 제3자 의존성 제거](../projects/09-cloud-cost-optimization.md)** — 43.9% 절감, MSP 기술지원 미수령 자체 운영 전환

## 그 밖의 업무

**데이터 플랫폼 3단계**

| 단계 | 내용 |
|---|---|
| 1차 | Airflow · DMS · Athena · Redash · QuickSight 기반 DW와 개인정보 Processing |
| 2차 | Redshift Serverless View 기반 ZeroETL 파이프라인 전환 |
| 3차 | EMR 빅데이터 플랫폼, Flink 실시간 WAF 모니터링, Imply 기반 클라우드 Audit |

## 남은 것

3년여 보안 무사고 · 정보보호위원회와 정책 체계 · 무중단 서비스와 연간 가용성 99.98% · 월 인프라 비용 43.9% 절감 · 외부 사업자 없이 인프라를 운영할 수 있는 내부 역량
