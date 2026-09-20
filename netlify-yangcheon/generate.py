from pathlib import Path
from html import escape
from datetime import datetime, timezone
import re

root=Path('site')
root.mkdir(parents=True, exist_ok=True)

dongs=['목동','신정동','신월동']
grades=['초등','초등학생','초1','초2','초3','초4','초5','초6','중등','중학생','중1','중2','중3','고등','고등학생','고1','고2','고3']
subjects=['영어과외','수학과외']
schools=['목동중학교','목동중','신목중학교','신목중','월촌중학교','월촌중','양정중학교','양정중','양정고등학교','양정고','한가람고등학교','한가람고','강서고등학교','강서고']
apts=[f'목동신시가지{i}단지' for i in range(1,15)]

CSS=''':root{--ink:#13223a;--muted:#5d6b7f;--line:#e6ebf1;--bg:#f7f9fc;--brand:#2257d7;--card:#fff}
*{box-sizing:border-box}body{margin:0;font-family:Arial,"Noto Sans KR",sans-serif;color:var(--ink);background:var(--bg);line-height:1.72}
a{text-decoration:none;color:inherit}.wrap{max-width:1120px;margin:auto;padding:0 22px}header{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.nav{height:68px;display:flex;align-items:center;justify-content:space-between}.brand{font-size:21px;font-weight:800}.nav small{color:var(--muted)}
.hero{padding:74px 0 48px;background:linear-gradient(135deg,#eef4ff 0%,#fff 55%,#f4f7ff 100%)}.eyebrow{font-weight:800;color:var(--brand);font-size:14px}.hero h1{font-size:clamp(34px,5vw,62px);line-height:1.12;margin:12px 0 18px;letter-spacing:-2px}.hero p{max-width:760px;color:var(--muted);font-size:18px}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}.btn{padding:13px 18px;border-radius:12px;font-weight:800;border:1px solid var(--line);background:#fff}.btn.primary{background:var(--brand);color:#fff;border-color:var(--brand)}
section{padding:52px 0}.section-title{font-size:29px;margin:0 0 10px}.section-desc{color:var(--muted);margin:0 0 24px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:0 7px 24px rgba(21,43,78,.05)}.card h3{margin:0 0 8px}.card p{color:var(--muted);margin:0 0 14px}.links{display:flex;gap:8px;flex-wrap:wrap}.chip{padding:8px 11px;border-radius:999px;background:#eef3ff;color:#234aa8;font-size:14px;font-weight:700}
.content{max-width:860px}.content h2{margin-top:34px;font-size:26px}.content p{color:#3d4c61}.breadcrumb{font-size:14px;color:var(--muted);margin-top:26px}.faq details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:10px 0}.faq summary{font-weight:800;cursor:pointer}
.floating{position:fixed;right:18px;bottom:18px;display:flex;flex-direction:column;gap:10px;z-index:30}.float{border:0;border-radius:999px;padding:13px 17px;font-weight:800;box-shadow:0 8px 28px rgba(0,0,0,.14);cursor:pointer}.call{background:#13223a;color:#fff}.apply{background:#2257d7;color:#fff}footer{border-top:1px solid var(--line);padding:34px 0;color:var(--muted);font-size:14px;background:#fff}
@media(max-width:760px){.grid{grid-template-columns:1fr}.hero{padding-top:52px}.nav small{display:none}.floating{right:12px;bottom:12px}.float{font-size:13px;padding:12px 14px}}
'''
(root/'styles.css').write_text(CSS,encoding='utf-8')
(root/'app.js').write_text("document.addEventListener('click',e=>{const t=e.target.closest('[data-call],[data-apply]');if(!t)return;if(t.hasAttribute('data-call'))location.href='tel:01045476978';if(t.hasAttribute('data-apply'))location.href='mailto:djreodusqhdlbh@naver.com?subject='+encodeURIComponent('양천구 과외 상담 신청');});",encoding='utf-8')

def slug(s):
    m={'목동':'mokdong','신정동':'sinjeong','신월동':'sinwol','영어과외':'english','수학과외':'math','초등':'elementary','초등학생':'elementary-student','중등':'middle','중학생':'middle-student','고등':'high','고등학생':'high-student'}
    if s in m:return m[s]
    return re.sub(r'[^0-9A-Za-z가-힣-]+','-',s.replace('학교','-school').replace('고등','high').replace('중','middle')).strip('-')

def layout(title,desc,body):
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title><meta name="description" content="{escape(desc)}"><meta name="robots" content="index,follow,max-image-preview:large"><meta property="og:type" content="website"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(desc)}"><link rel="alternate" type="application/rss+xml" title="양천구 과외 RSS" href="/rss.xml"><link rel="stylesheet" href="/styles.css"><script defer src="/app.js"></script><script type="application/ld+json">{{"@context":"https://schema.org","@type":"EducationalOrganization","name":"양천구 과외","areaServed":"서울특별시 양천구","description":"양천구 영어 수학 1:1 과외 안내"}}</script></head><body><header><div class="wrap nav"><a class="brand" href="/">양천구 과외</a><small>영어 · 수학 · 방문/온라인 1:1</small></div></header>{body}<div class="floating"><button class="float call" data-call>전화 상담</button><button class="float apply" data-apply>온라인 신청</button></div><footer><div class="wrap">서울 양천구 영어·수학 과외 정보 사이트 · 방문 및 온라인 수업 상담</div></footer></body></html>'''

def detail_page(keyword,intro):
    title=f'{keyword} | 양천구 1:1 맞춤 과외'
    desc=f'{keyword}를 찾는 학생과 학부모를 위한 1:1 맞춤 과외 안내. 진단, 학습계획, 내신·기초·심화 관리, 방문·온라인 수업 상담.'
    body=f'''<main><div class="wrap content"><div class="breadcrumb"><a href="/">홈</a> › {escape(keyword)}</div><section><div class="eyebrow">YANGCHEON TUTORING GUIDE</div><h1 class="section-title">{escape(keyword)}</h1><p class="section-desc">{escape(intro)}</p><div class="btns"><button class="btn primary" data-apply>온라인 상담 신청</button><button class="btn" data-call>전화 상담</button></div></section><section><h2>수업은 이렇게 진행합니다</h2><p>첫 상담에서는 최근 시험지, 오답 유형, 숙제 습관과 수업 이해 속도를 함께 확인합니다. 이후 주간 학습량과 학교 일정에 맞춰 과제량과 복습 주기를 조정합니다.</p><h2>영어 과외</h2><p>어휘·문법·독해를 학교 진도와 시험 범위 안에서 연결합니다. 기초는 문장 구조와 핵심 어휘부터, 상위권은 서술형·변형 문제·시간 관리 중심으로 수업합니다.</p><h2>수학 과외</h2><p>개념 확인 → 대표 유형 → 오답 재풀이 → 누적 복습 순서로 진행합니다. 풀이 과정을 설명하도록 하여 계산 실수와 개념 누락을 구분합니다.</p><h2>방문과 온라인 모두 가능</h2><p>학생 일정과 학습 환경에 따라 방문 또는 온라인 수업으로 진행할 수 있습니다. 매 회차 진도와 과제를 기준으로 다음 수업 계획을 연결합니다.</p></section><section class="faq"><h2>자주 묻는 질문</h2><details><summary>기초가 부족해도 시작할 수 있나요?</summary><p>가능합니다. 현재 수준을 먼저 확인하고 필요한 단원부터 학습 순서를 다시 잡습니다.</p></details><details><summary>내신 대비도 하나요?</summary><p>학교 시험 범위와 일정에 맞춰 교과서, 부교재, 프린트, 기출 유형을 중심으로 대비합니다.</p></details><details><summary>상담 시 무엇을 알려주면 되나요?</summary><p>지역, 학년, 과목, 현재 수준, 원하는 수업 방식과 가능한 시간대를 알려주시면 됩니다.</p></details></section></div></main>'''
    return layout(title,desc,body)

cards=''.join(f'<div class="card"><h3>{d}</h3><p>{d} 영어·수학 과외와 학년별 페이지를 확인하세요.</p><div class="links"><a class="chip" href="/{slug(d)}/english/">영어과외</a><a class="chip" href="/{slug(d)}/math/">수학과외</a></div></div>' for d in dongs)
home=f'''<main><section class="hero"><div class="wrap"><div class="eyebrow">서울 양천구 1:1 맞춤 과외</div><h1>동네와 학년에 맞춰 찾는<br>양천구 영어·수학 과외</h1><p>목동·신정동·신월동을 중심으로 초등부터 고등까지, 영어와 수학 학습 상황에 맞는 1:1 방문·온라인 과외 정보를 제공합니다.</p><div class="btns"><button class="btn primary" data-apply>온라인 상담 신청</button><button class="btn" data-call>전화 상담</button></div></div></section><section><div class="wrap"><h2 class="section-title">지역별 과외 찾기</h2><p class="section-desc">원하는 동과 과목을 선택하면 상세 안내로 이동합니다.</p><div class="grid">{cards}</div></div></section><section><div class="wrap"><h2 class="section-title">학년별 학습 관리</h2><div class="grid"><div class="card"><h3>초등</h3><p>학습 습관과 기본 개념을 먼저 잡습니다.</p></div><div class="card"><h3>중등</h3><p>학교 시험 범위와 서술형, 오답 누적 관리를 진행합니다.</p></div><div class="card"><h3>고등</h3><p>내신과 수능형 문제를 구분해 약점 단원과 시간 관리까지 연결합니다.</p></div></div></div></section></main>'''
(root/'index.html').write_text(layout('양천구 과외 | 목동 신정동 신월동 영어과외 수학과외','서울 양천구 목동 신정동 신월동 영어과외 수학과외. 초등 중등 고등 1:1 방문·온라인 맞춤 과외 상담.',home),encoding='utf-8')

urls=['/']
for d in dongs:
    for sub in subjects:
        p=root/slug(d)/slug(sub); p.mkdir(parents=True,exist_ok=True)
        (p/'index.html').write_text(detail_page(f'{d} {sub}',f'{d}에서 {sub}를 찾는 학생을 위한 수준별 1:1 수업 안내입니다.'),encoding='utf-8'); urls.append('/'+slug(d)+'/'+slug(sub)+'/')
        for g in grades:
            q=p/slug(g); q.mkdir(parents=True,exist_ok=True)
            (q/'index.html').write_text(detail_page(f'{d} {g} {sub}',f'{d} {g} 학생의 현재 진도와 목표에 맞춘 {sub} 수업 안내입니다.'),encoding='utf-8'); urls.append('/'+slug(d)+'/'+slug(sub)+'/'+slug(g)+'/')

for s in schools:
    for sub in subjects:
        p=root/'school'/slug(s)/slug(sub); p.mkdir(parents=True,exist_ok=True)
        (p/'index.html').write_text(detail_page(f'양천구 {s} {sub}',f'{s} 학생의 학교 진도와 시험 범위를 고려한 {sub} 학습 안내입니다.'),encoding='utf-8'); urls.append('/school/'+slug(s)+'/'+slug(sub)+'/')
for a in apts:
    for sub in subjects:
        p=root/'apartment'/slug(a)/slug(sub); p.mkdir(parents=True,exist_ok=True)
        (p/'index.html').write_text(detail_page(f'양천구 {a} {sub}',f'{a} 인근 방문·온라인 {sub} 상담 안내입니다.'),encoding='utf-8'); urls.append('/apartment/'+slug(a)+'/'+slug(sub)+'/')

p=root/'apply'; p.mkdir(exist_ok=True)
apply='''<main><div class="wrap content"><section><div class="eyebrow">CONSULTATION</div><h1 class="section-title">온라인 상담 신청</h1><p class="section-desc">지역, 학년, 희망 과목, 현재 수준과 가능한 시간대를 적어 보내주세요.</p><div class="btns"><button class="btn primary" data-apply>상담 메일 작성</button><button class="btn" data-call>전화 상담</button></div></section></div></main>'''
(p/'index.html').write_text(layout('온라인 상담 신청 | 양천구 과외','양천구 영어 수학 과외 온라인 상담 신청 안내.',apply),encoding='utf-8'); urls.append('/apply/')

(root/'netlify.toml').write_text('[build]\n  publish = "."\n',encoding='utf-8')
(root/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n',encoding='utf-8')
base='https://dazzling-cranachan-01b3f8.netlify.app'
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{base}{u}</loc><changefreq>weekly</changefreq></url>\n' for u in urls)+'</urlset>',encoding='utf-8')
(root/'rss.xml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>양천구 과외</title><link>{base}</link><description>양천구 영어 수학 과외 정보</description><item><title>양천구 과외 지역별 안내</title><link>{base}</link><pubDate>{datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate></item></channel></rss>''',encoding='utf-8')
print(f'generated {len(urls)} pages')
