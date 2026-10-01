# 신윤상 — Portfolio

> **SRE · Cloud Native & Security Architect · 前 CISO·CPO**
> 없던 것을 만드는 쪽에서 커리어를 보냈습니다. 데이터센터는 연구과제에서 준공까지, 무너진 플랫폼은 재건 쪽으로, 흩어진 장애 대응은 전사 체계로.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-yoonsang--shin-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yoonsang-shin-859b8b1a2)
![Experience](https://img.shields.io/badge/경력-20년-1b3a5c?style=flat-square)
![Cases](https://img.shields.io/badge/케이스-13건-2d6a4f?style=flat-square)
![Regulators](https://img.shields.io/badge/규제기관_대응-6곳-8a5a1b?style=flat-square)

---

## 이 저장소에 대하여

**프로젝트 케이스**가 본문이고, **근무 기업**은 맥락 인덱스입니다.
각 케이스는 조직·시기·제약을 헤더에 고정으로 달아, 그 문서만 따로 읽어도 배경이 서도록 했습니다.

케이스는 다음 구조를 따릅니다.

```
문제  →  제약  →  설계(왜 그 선택이었나)  →  결과  →  회고
```

성과 나열이 아니라 **판단의 기록**으로 썼습니다. 같은 이유로 잘 안 된 판단과 지금이라면 다르게 할 부분도 함께 적었습니다.

---

## 케이스

### 신뢰성 · 장애관리

| 케이스 | 조직 | 핵심 |
|---|---|---|
| **[전사 장애관리 프레임워크](projects/01-incident-management-framework.md)** | 무신사 | SEV 등급부터 Close 게이트까지 13개 영역. 장애 중에는 IC 단일 지휘로 승인 게이트를 제거하고, 거버넌스는 DACI로 분리 |
| **[전사 SLO 체계 수립](projects/02-company-wide-slo.md)** | 무신사 · 29CM | CUJ 단위로 핵심 사용자 여정 정의. 반복 롤백 원인 규명, Staging 과투자를 Chaos 투자로 전환 |
| **[비상대응훈련 프로그램](projects/03-incident-drill-program.md)** | 무신사 | 100점 루브릭 · LLM 이중 채점 · 70점 재실시. Reliability 주도에서 조직 자체 주도로 이관 |
| **[신뢰성 자동화](projects/04-reliability-automation.md)** | 무신사 | 멀티소스 Alert Gateway(중복 제거 · LLM/RAG 보강), Slack 인시던트 봇, 온콜 전사 확장 |

### 거버넌스 · 보안 · 규제

| 케이스 | 조직 | 핵심 |
|---|---|---|
| **[보안 거버넌스 — 정보보호위원회와 조직 리딩](projects/13-security-governance.md)** | 트렌비 | 정보보호위원회 운영, 약관에 고지된 공식 CPO, 정책 체계와 승인 구조 수립 |
| **[AI 거버넌스 프레임워크](projects/05-ai-governance.md)** `진행 중` | 무신사 | 생산성을 저해하지 않는 통제 범위. 자동화 경계 — 무엇을 AI가 판단하고 무엇을 사람이 지휘할지 |
| **[개인정보 유출 사고 대응](projects/06-privacy-incident-response.md)** | 트렌비 | CPO로서 사고 발생부터 규제기관 현장점검까지 지휘. **과징금 없이 종결**, 이후 3년간 시정조치·개선권고 이행보고 |
| **[클라우드 보안 프레임워크 · ISMS-P](projects/07-cloud-security-framework.md)** | 스타랩스 → 트렌비 → 무신사 | 별도 장비 없이 관리형 서비스만으로 심사 승인. 망분리를 **VDI → ZTNA → 클라우드 작업환경 분리** 세 방식으로 |
| **[금융권 컨테이너 도입 — 금감원 소명자료](projects/10-financial-container-compliance.md)** | 넥스클라우드 | 선례가 없던 시점에 통제 항목 × 구현 수단 매핑으로 규제 근거 수립 |

### 플랫폼 · 비용

| 케이스 | 조직 | 핵심 |
|---|---|---|
| **[EKS 플랫폼 리빌드](projects/08-eks-platform-rebuild.md)** | 트렌비 | 레거시 위에 신규 구축. Instance/Zone/Region Fail 상시 검증으로 **가용성 99.98%** |
| **[클라우드 비용 최적화와 제3자 의존성 제거](projects/09-cloud-cost-optimization.md)** | 트렌비 | **월 비용 43.9% 절감**(연 약 10억). MSP 기술지원 미수령 자체 운영 전환 |

### 인프라 · 대외협력

| 케이스 | 조직 | 핵심 |
|---|---|---|
| **[중립 데이터센터 지위 확보](projects/11-neutral-datacenter.md)** | NAVER | 방통위 중재 승소로 타사 회선 수용 확보, **통신사 약관 개정**. 공정위 조사·고용노동부 현장점검 대응 포함 |
| **[춘천 데이터센터](projects/12-chuncheon-datacenter.md)** | NAVER | 타당성 연구 PL부터 준공, 퍼블릭 클라우드 상품화까지 약 5년 |

---

## 근무 기업

| 기간 | 조직 | 역할 | 케이스 |
|---|---|---|---|
| 2025.01 – 재직 중 | **[무신사](companies/musinsa.md)** | SRE · 전사 장애관리 Incident Owner | 01 · 02 · 03 · 04 · 05 · 07 |
| 2021.06 – 2024.12 | **[트렌비](companies/trenbe.md)** | SRE Lead 겸 CISO·CPO | 06 · 07 · 08 · 09 · 13 |
| 2020.09 – 2021.05 | **[넥스클라우드](companies/nexcloud.md)** | Consulting Team Leader | 10 |
| 2020.02 – 2020.08 | **[OSC Korea](companies/osc-korea.md)** | Cloud Native Consultant | — |
| 2018.11 – 2020.01 | **[스타랩스](companies/starlabs.md)** | Cloud Architecture / Governance Consulting | 07 |
| 2016.05 – 2018.10 | **[아이엔소프트](companies/insoft.md)** | PO / PM | — |
| 2007.04 – 2014.07 | **[NAVER](companies/naver.md)** | 데이터센터/클라우드 사업 PO · IT기획 · IT구매 | 11 · 12 |
| 2006.04 – 2007.03 | **[Yahoo Korea](companies/yahoo-korea.md)** | Oracle DBA · 보안 (ASIA) | — |
| 2002.12 – 2006.02 | **[NAVER](companies/naver.md)** | 인프라 운영 PL | — |

---

## 역량 맵

| 영역 | 무신사 | 트렌비 | 넥스클라우드 | OSC | 스타랩스 | 아이엔소프트 | NAVER | Yahoo |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 장애관리·업무연속성 | ● | ● | | ○ | | ○ | ● | |
| SLO/SLI·신뢰성 공학 | ● | ● | | ○ | | | | |
| 정보보호·인증심사 | ● | ● | ○ | | ● | | ○ | ○ |
| 보안 거버넌스·조직 리딩 | ● | ● | | | | | ○ | |
| 규제·감독기관 대응 | | ● | ● | | ● | | ● | |
| 제3자 리스크·계약 | | ● | | | | ● | ● | |
| 클라우드 아키텍처 | ● | ● | ● | ● | ● | ● | ● | |
| 원가·TCO·사업기획 | ○ | ● | | | | ● | ● | |
| AI·LLM 적용 | ● | | | | | | | |
| 대규모 인프라 운영 | ● | ● | | | | | ● | ● |

● 주도 · ○ 부분 참여

---

## 되풀이되는 방법론

케이스를 가로로 읽으면 같은 방법이 반복됩니다.

**통제 항목 × 구현 수단 매핑** — 규제 항목을 구조화하고, 각 항목에 대해 대체 수단의 동등성을 근거로 입증합니다.
[ISMS-P 심사](projects/07-cloud-security-framework.md) · [금감원 소명](projects/10-financial-container-compliance.md) ·
[개인정보보호위원회·KISA 현장점검](projects/06-privacy-incident-response.md) ·
[방통위 중재 · 공정위 조사 · 고용노동부 현장점검](projects/11-neutral-datacenter.md) —
**여섯 곳의 규제기관**을 같은 방식으로 대응했습니다.

**예외가 아니라 규칙을 바꾼다** — 개별 승인은 사람이 바뀌면 사라지지만, 약관과 기준 문서는 남습니다.
[통신사 약관 개정](projects/11-neutral-datacenter.md)에서 배운 것이
[프레임워크를 기준 문서 형태로 만드는 습관](projects/01-incident-management-framework.md)으로 이어졌습니다.

**믿지 않고 검증한다** — 이중화는 실제로 내려봐야 이중화입니다.
[Chaos Engineering](companies/osc-korea.md) → [Instance/Zone/Region Fail 상시 검증](projects/08-eks-platform-rebuild.md)
→ [모의훈련 루브릭 채점](projects/03-incident-drill-program.md).

---

## 자주 쓰는 기술

**Cloud** AWS (EKS, Organizations, Landing Zone, Transit Gateway, KMS, WAF) · GCP Anthos · OpenStack
**Kubernetes** ArgoCD · Argo Workflows · Istio/Kiali · Multus · MetalLB · Terragrunt
**Observability** Datadog · Prometheus · Grafana · Loki · CloudWatch · PagerDuty
**Security** Okta (SSO/SAML/ZTNA) · GuardDuty · CSPM/CWPP · Teleport · Harbor
**Data** Airflow · Redshift Serverless (ZeroETL) · EMR · Flink · Athena · Imply/Druid
**AI** LLM 기반 알림 보강 · RAG 컨텍스트 주입 · 훈련 자동 채점 · 인시던트 대응 자동화

---

## 경력기술서

지원 포지션에 따라 강조점을 달리한 버전입니다. 사실관계는 동일하고 구성과 서술 비중만 다릅니다.

| 버전 | 초점 |
|---|---|
| **[정보보안팀장](resume/신윤상_경력기술서_정보보안팀장.pdf)** | ISMS-P · 규제기관 대응 · 개인정보 · 3rd Party · 보안 거버넌스 |
| **[IT 거버넌스 · BCP](resume/신윤상_경력기술서_IT거버넌스_BCP.pdf)** | 업무연속성 · 인증심사 · 제3자 리스크 · AI 거버넌스 |
| **[IT Planning Team Leader](resume/신윤상_경력기술서_IT_Planning_Team_Leader.pdf)** | 내부통제 · 경영계획 · 투자심의 · 협의체 운영 |
| **[SRE](resume/신윤상_경력기술서_SRE.pdf)** | 장애관리 · SLO · 플랫폼 · 신뢰성 자동화 |

웹으로 보기 → **[GitHub Pages](https://markv-2010.github.io/portfolio/)**

## 저장소 구조

```
├── README.md              이 문서 — 케이스 인덱스 · 기업 인덱스 · 역량 맵
├── projects/              프로젝트 케이스 13건 (본문)
├── companies/             근무 기업 8곳 (맥락 인덱스)
├── assets/                다이어그램 · 차트
├── resume/                포지션별 경력기술서 PDF
├── tools/build_site.py    마크다운 → GitHub Pages 사이트 빌드
└── docs/                  생성된 사이트 (GitHub Pages 소스)
```

```bash
pip install markdown
python3 tools/build_site.py
```

## 연락

- Email — sysang0891@gmail.com
- LinkedIn — [yoonsang-shin](https://www.linkedin.com/in/yoonsang-shin-859b8b1a2)

---

<sub>개인 포트폴리오입니다. 각 조직에서 수행한 업무를 역할과 판단 중심으로 기술했으며, 내부 문서·식별자·고객 데이터는 포함하지 않습니다.</sub>
