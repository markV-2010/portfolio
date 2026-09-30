[← 포트폴리오](../README.md)

# 스타랩스

**Cloud Technical Architecture · Governance Strategy Consulting**
`2018.11 – 2020.01` · LG 지주사 클라우드 사업화 컨설팅

---

## 이 시기의 상황

그룹사 전체가 클라우드를 쓰려면 두 가지가 없었습니다 — **규제를 통과하는 방법**과 **인트라넷에서 닿는 경로**.
당시 관행은 클라우드에도 기존 보안 장비를 그대로 얹는 것이었습니다.

## 맡은 범위

그룹사 전체가 클라우드를 쓸 수 있는 기반과, LG CNS가 그것을 사업화할 수 있는 체계를 함께 만드는 일.

## 케이스

- **[클라우드 보안 프레임워크 · ISMS-P](../projects/07-cloud-security-framework.md)**
  별도 장비 없이 AWS Managed Service만으로 ISMS-P 요건을 충족하는 프레임워크를 설계해 심사 승인.
  LG화학 · LG디스플레이 · LG CNS 운영 가이던스로 확산했고, 이후 [트렌비 보안 프레임워크](trenbe.md)의 원형이 됐습니다.

## 그 밖의 업무

**LG그룹 인트라넷–Public Cloud 연결 (그룹 최초)**

- LG\*net과 Public Cloud 연결 — MPLS 회선 Associate, BGP Routing Propagate 설계·구축
- FWaaS(Firewall as a Service) 설계·구축 — 인트라넷·클라우드 구간을 서비스형 방화벽으로 제공하고 Circuit Breaker 구성

**클라우드 도입 기반과 SaaS 플랫폼 TF**

- AWS Organization · Landing Zone · Security VPC(UTM · WAF · 접근제어) 구축
- EKS 기반 Application Container 적용, GCP Anthos로 Multi Cloud 구성
- 지주사 SaaS 플랫폼 TF Agile Scrum Master — 판토스 물류 · LG전자 홈페이지 · LG화학 인사시스템 Integration
