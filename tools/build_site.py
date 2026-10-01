#!/usr/bin/env python3
"""
README.md 와 companies/*.md 를 GitHub Pages 용 정적 사이트(docs/)로 변환한다.

사용법:
    pip install markdown
    python3 tools/build_site.py

마크다운이 단일 소스이며, 사이트는 항상 여기서 생성된다.
"""

import os
import re
import shutil
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")

INDEX = ("README.md", "index.html", "전체 개요")

# (마크다운 경로, 출력 파일, 사이드바 라벨, 우측 메타)
PROJECTS = [
    ("projects/01-incident-management-framework.md", "p01-incident-framework.html", "장애관리 프레임워크", "무신사"),
    ("projects/02-company-wide-slo.md", "p02-slo.html", "전사 SLO 체계", "무신사"),
    ("projects/03-incident-drill-program.md", "p03-drill.html", "비상대응훈련", "무신사"),
    ("projects/04-reliability-automation.md", "p04-automation.html", "신뢰성 자동화", "무신사"),
    ("projects/05-ai-governance.md", "p05-ai-governance.html", "AI 거버넌스", "진행 중"),
    ("projects/06-privacy-incident-response.md", "p06-privacy.html", "개인정보 사고대응", "트렌비"),
    ("projects/07-cloud-security-framework.md", "p07-security.html", "보안·ISMS-P 대응", "3개 조직"),
    ("projects/08-eks-platform-rebuild.md", "p08-eks.html", "EKS 플랫폼 리빌드", "트렌비"),
    ("projects/09-cloud-cost-optimization.md", "p09-cost.html", "비용·제3자 리스크", "트렌비"),
    ("projects/10-financial-container-compliance.md", "p10-fin-compliance.html", "금융권 규제", "넥스클라우드"),
    ("projects/11-neutral-datacenter.md", "p11-neutral-dc.html", "중립 데이터센터", "NAVER"),
    ("projects/12-chuncheon-datacenter.md", "p12-chuncheon-dc.html", "춘천 데이터센터", "NAVER"),
    ("projects/13-security-governance.md", "p13-governance.html", "보안 거버넌스", "트렌비"),
]

COMPANIES = [
    ("companies/musinsa.md", "c-musinsa.html", "무신사", "2025.01 –"),
    ("companies/trenbe.md", "c-trenbe.html", "트렌비", "2021 – 2024"),
    ("companies/nexcloud.md", "c-nexcloud.html", "넥스클라우드", "2020 – 2021"),
    ("companies/osc-korea.md", "c-osc-korea.html", "OSC Korea", "2020"),
    ("companies/starlabs.md", "c-starlabs.html", "스타랩스", "2018 – 2020"),
    ("companies/insoft.md", "c-insoft.html", "아이엔소프트", "2016 – 2018"),
    ("companies/naver.md", "c-naver.html", "NAVER", "2002 – 2014"),
    ("companies/yahoo-korea.md", "c-yahoo-korea.html", "Yahoo Korea", "2006 – 2007"),
]

PAGES = [INDEX] + [(s, o, l) for s, o, l, _ in PROJECTS + COMPANIES]

# 마크다운 파일명 → 사이트 파일명 (본문 링크 치환용)
SLUGS = {
    os.path.basename(src): out
    for src, out, _, _ in PROJECTS + COMPANIES
}

PROJECT_GROUPS = [
    ("신뢰성 · 장애관리", PROJECTS[0:4]),
    ("거버넌스 · 보안 · 규제", [PROJECTS[12], PROJECTS[5], PROJECTS[6], PROJECTS[9], PROJECTS[4]]),
    ("플랫폼 · 비용", [PROJECTS[7], PROJECTS[8]]),
    ("인프라 · 대외협력", PROJECTS[10:12]),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · 신윤상 Portfolio</title>
<meta name="description" content="신윤상 — SRE · Cloud Native &amp; Security Architect 포트폴리오">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #0d1117;
  --bg-soft: #131a23;
  --bg-card: #161d27;
  --line: #232c38;
  --line-soft: #1c242f;
  --fg: #d8dee6;
  --fg-dim: #8b97a6;
  --fg-faint: #616d7c;
  --accent: #58a6ff;
  --accent-dim: #2f5f96;
  --green: #4ec9a5;
  --amber: #d4a548;
  --head: #f0f4f8;
}}
@media (prefers-color-scheme: light) {{
  :root:not([data-theme="dark"]) {{
    --bg: #ffffff; --bg-soft: #f6f8fa; --bg-card: #ffffff;
    --line: #d5dce4; --line-soft: #e6ebf0;
    --fg: #27313d; --fg-dim: #5c6773; --fg-faint: #8a939e;
    --accent: #0a5fc4; --accent-dim: #9dbde4;
    --green: #17795e; --amber: #8a6416; --head: #10233a;
  }}
}}
* {{ box-sizing: border-box; }}
html {{ scroll-behavior: smooth; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font-family: "IBM Plex Sans KR", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 15px; line-height: 1.75;
  -webkit-font-smoothing: antialiased;
}}
.wrap {{ display: flex; max-width: 1180px; margin: 0 auto; gap: 0; }}

/* ---------- sidebar ---------- */
aside {{
  width: 232px; flex: 0 0 232px; border-right: 1px solid var(--line);
  padding: 34px 20px 60px 16px; position: sticky; top: 0; height: 100vh;
  overflow-y: auto;
}}
aside .brand {{ display: block; text-decoration: none; margin-bottom: 26px; }}
aside .brand b {{ display: block; font-size: 17px; font-weight: 700; color: var(--head); letter-spacing: -0.2px; }}
aside .brand span {{ display: block; font-size: 11.5px; color: var(--fg-faint); margin-top: 2px; letter-spacing: 0.2px; }}
aside .navlabel {{
  font-size: 10.5px; text-transform: uppercase; letter-spacing: 1.1px;
  color: var(--fg-faint); margin: 22px 0 7px 10px; font-weight: 700;
}}
aside .navsub {{
  font-size: 11px; color: var(--fg-faint); margin: 13px 0 4px 10px; font-weight: 600;
  padding-top: 8px; border-top: 1px dashed var(--line-soft);
}}
aside .navsub:first-of-type {{ border-top: 0; padding-top: 0; margin-top: 4px; }}
aside a.nav {{
  display: flex; justify-content: space-between; align-items: baseline; gap: 6px;
  padding: 6px 10px; border-radius: 6px; text-decoration: none;
  color: var(--fg-dim); font-size: 13.5px; line-height: 1.4;
}}
aside a.nav em {{ font-style: normal; font-size: 10.5px; color: var(--fg-faint); font-family: "JetBrains Mono", monospace; white-space: nowrap; }}
aside a.nav:hover {{ background: var(--bg-soft); color: var(--fg); }}
aside a.nav.on {{ background: var(--bg-soft); color: var(--accent); font-weight: 600; box-shadow: inset 2px 0 0 var(--accent); }}
aside .foot {{ margin-top: 28px; padding-top: 16px; border-top: 1px solid var(--line-soft); font-size: 12px; color: var(--fg-faint); }}
aside .foot a {{ color: var(--fg-dim); text-decoration: none; display: block; padding: 3px 0; }}
aside .foot a:hover {{ color: var(--accent); }}

/* ---------- content ---------- */
main {{ flex: 1 1 auto; min-width: 0; padding: 38px 40px 100px; }}
main > :first-child {{ margin-top: 0; }}

h1 {{ font-size: 30px; font-weight: 700; color: var(--head); letter-spacing: -0.7px; margin: 0 0 6px; line-height: 1.25; }}
h2 {{
  font-size: 19px; font-weight: 700; color: var(--head); letter-spacing: -0.3px;
  margin: 44px 0 14px; padding-bottom: 7px; border-bottom: 1px solid var(--line);
}}
h3 {{ font-size: 15.5px; font-weight: 600; color: var(--head); margin: 28px 0 9px; }}
p {{ margin: 0 0 13px; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}

blockquote {{
  margin: 18px 0; padding: 12px 18px; border-left: 3px solid var(--accent-dim);
  background: var(--bg-soft); border-radius: 0 7px 7px 0; color: var(--fg-dim);
}}
blockquote p {{ margin: 0 0 8px; }}
blockquote p:last-child {{ margin: 0; }}
blockquote strong {{ color: var(--green); }}

ul, ol {{ padding-left: 20px; margin: 0 0 14px; }}
li {{ margin-bottom: 5px; }}
li::marker {{ color: var(--fg-faint); }}
strong {{ color: var(--head); font-weight: 600; }}
hr {{ border: 0; border-top: 1px solid var(--line); margin: 34px 0; }}

code {{
  font-family: "JetBrains Mono", monospace; font-size: 12.5px;
  background: var(--bg-soft); border: 1px solid var(--line-soft);
  padding: 1.5px 6px; border-radius: 5px; color: var(--fg-dim);
}}
pre {{
  background: var(--bg-soft); border: 1px solid var(--line);
  border-radius: 9px; padding: 15px 18px; overflow-x: auto; margin: 0 0 16px;
}}
pre code {{ background: none; border: 0; padding: 0; font-size: 12.5px; line-height: 1.75; color: var(--fg-dim); }}

table {{ width: 100%; border-collapse: collapse; margin: 6px 0 20px; font-size: 13.5px; display: block; overflow-x: auto; }}
th {{
  background: var(--bg-soft); color: var(--head); font-weight: 600;
  text-align: left; padding: 8px 12px; border: 1px solid var(--line); white-space: nowrap;
}}
td {{ padding: 8px 12px; border: 1px solid var(--line-soft); vertical-align: top; }}
tr:hover td {{ background: var(--bg-soft); }}

img {{ max-width: 100%; height: auto; border-radius: 10px; border: 1px solid var(--line); margin: 8px 0 18px; display: block; }}
img.badge {{ display: inline-block; height: 20px; width: auto; border: 0; border-radius: 4px; margin: 0 5px 8px 0; vertical-align: middle; }}
p.badges {{ margin-bottom: 8px; }}

/* header block under h1 */
h1 + p {{ color: var(--fg-dim); font-size: 14.5px; }}

@media (max-width: 860px) {{
  .wrap {{ flex-direction: column; }}
  aside {{
    width: auto; flex: none; position: static; height: auto;
    border-right: 0; border-bottom: 1px solid var(--line); padding: 22px 20px 16px;
  }}
  main {{ padding: 26px 20px 70px; }}
  h1 {{ font-size: 25px; }}
}}
</style>
</head>
<body>
<div class="wrap">
<aside>
  <a class="brand" href="index.html">
    <b>신윤상</b>
    <span>SRE · Security · Governance</span>
  </a>
  <a class="nav{home_on}" href="index.html">전체 개요</a>
  <div class="navlabel">프로젝트 케이스</div>
{nav}
  <div class="foot">
    <a href="https://www.linkedin.com/in/yoonsang-shin-859b8b1a2" target="_blank" rel="noopener">LinkedIn ↗</a>
    <a href="mailto:sysang0891@gmail.com">sysang0891@gmail.com</a>
  </div>
</aside>
<main>
{body}
</main>
</div>
</body>
</html>
"""


def build_nav(current):
    out = []
    for title, group in PROJECT_GROUPS:
        out.append(f'  <div class="navsub">{title}</div>')
        for src, html, label, meta in group:
            on = " on" if html == current else ""
            out.append(f'  <a class="nav{on}" href="{html}">{label}<em>{meta}</em></a>')
    out.append('  <div class="navlabel">근무 기업</div>')
    for src, html, label, meta in COMPANIES:
        on = " on" if html == current else ""
        out.append(f'  <a class="nav{on}" href="{html}">{label}<em>{meta}</em></a>')
    return "\n".join(out)


def rewrite_links(html):
    """마크다운 상대경로를 사이트 경로로 변환."""
    html = re.sub(r'href="(?:\.\./)?README\.md"', 'href="index.html"', html)
    # projects/xx.md, companies/xx.md, ../projects/xx.md, 같은 폴더 내 xx.md 를 모두 처리
    def _slug(m):
        return 'href="' + SLUGS.get(m.group(1), m.group(1) + ".html")
    html = re.sub(r'href="(?:\.\./)?(?:projects/|companies/)?([\w.-]+\.md)', _slug, html)
    html = re.sub(r'src="(?:\.\./)?assets/', 'src="assets/', html)
    html = re.sub(r'href="(?:\.\./)?resume/', 'href="resume/', html)
    # shields.io 뱃지는 본문 이미지와 다르게 인라인으로 처리
    html = re.sub(r'<img([^>]*?src="https://img\.shields\.io[^"]*")', r'<img class="badge"\1', html)
    html = re.sub(r'<p>(\s*(?:<a[^>]*>)?<img class="badge")', r'<p class="badges">\1', html)
    return html


def main():
    md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "sane_lists"])

    os.makedirs(os.path.join(DOCS, "assets"), exist_ok=True)
    src_assets = os.path.join(ROOT, "assets")
    for f in os.listdir(src_assets):
        shutil.copy2(os.path.join(src_assets, f), os.path.join(DOCS, "assets", f))

    # 이력서 PDF도 사이트에서 받을 수 있게 복사
    src_resume = os.path.join(ROOT, "resume")
    if os.path.isdir(src_resume):
        dst_resume = os.path.join(DOCS, "resume")
        os.makedirs(dst_resume, exist_ok=True)
        for f in os.listdir(src_resume):
            shutil.copy2(os.path.join(src_resume, f), os.path.join(dst_resume, f))

    for src, out, label in PAGES:
        with open(os.path.join(ROOT, src), encoding="utf-8") as fh:
            text = fh.read()
        md.reset()
        body = rewrite_links(md.convert(text))
        page = TEMPLATE.format(
            title=label,
            nav=build_nav(out),
            home_on=" on" if out == "index.html" else "",
            body=body,
        )
        with open(os.path.join(DOCS, out), "w", encoding="utf-8") as fh:
            fh.write(page)
        print(f"  {src:36s} → docs/{out}")

    # Jekyll 처리를 끄고 정적 파일을 그대로 서빙
    open(os.path.join(DOCS, ".nojekyll"), "w").close()
    print("\n완료 — docs/ 를 GitHub Pages 소스로 지정하세요.")


if __name__ == "__main__":
    main()
