import pathlib, re
src=pathlib.Path('/home/claude/bookalyze-social/template/exemplo_lote1.py').read_text()
BASE=re.search(r'BASE = """(.*?)"""',src,re.S).group(1)
D=pathlib.Path('/home/claude/build')
def page(n,theme,tag,body):
    logo="logo_white.png" if theme=="dark" else "logo_color.png"
    (D/f"post{n}.html").write_text(BASE%dict(theme=theme,tag=tag,body=body,logo=logo),encoding="utf-8")
CARD="background:#fff;border-radius:28px;box-shadow:0 8px 30px rgba(42,73,106,.08)"

# 1 Você sabia: noites órfãs (lacuna de 2 noites com mínimo de 3)
OC="background:var(--blue);color:#fff"
GAP="background:repeating-linear-gradient(135deg,var(--coral) 0 7px,#F2C2B4 7px 14px);color:var(--ink)"
FR="background:#E3EAF1;color:var(--navy)"
states=[OC]*4+[GAP]*2+[OC]*5+[FR]*3
cells="".join(f'<div style="height:96px;border-radius:12px;{s};display:flex;align-items:flex-end;justify-content:center;padding-bottom:10px;font-size:24px;font-weight:800">{d}</div>' for d,s in zip(range(10,24),states))
def leg(s,t): return f'<div style="display:flex;align-items:center;gap:12px;font-size:25px;font-weight:700;color:var(--navy)"><div style="width:30px;height:30px;border-radius:7px;{s}"></div>{t}</div>'
page(1,"light","VOCÊ SABIA?",f"""
<h1>Duas noites livres<br><em>que ninguém consegue reservar.</em></h1>
<div class="stage" style="padding-top:26px">
<div style="{CARD};padding:32px 34px 28px">
<div style="font-size:24px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:18px">UM IMÓVEL · DIAS 10 A 23</div>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:10px">{cells}</div>
<div style="display:flex;justify-content:space-between;margin-top:22px">{leg(OC,'Reservada')}{leg(GAP,'Noite órfã')}{leg(FR,'Livre')}</div>
</div>
<div style="{CARD};padding:28px 34px;margin-top:22px;display:flex;align-items:center;gap:28px">
<div style="font-size:92px;font-weight:800;line-height:1;color:#B5553C">2 &lt; 3</div>
<div style="font-size:30px;font-weight:700;color:var(--navy);line-height:1.25">Lacuna de 2 noites,<br>estadia mínima de 3.<br><span style="color:#6B7F93;font-weight:500">Essas noites ficam vazias.</span></div>
</div>
<div class="note" style="margin-top:14px">Exemplo ilustrativo</div>
</div>""")

# 2 Institucional: a reunião de segunda começa com os números prontos
def item(n,q,a):
    return f'''<div style="display:flex;gap:26px;align-items:flex-start;background:rgba(255,255,255,.07);border-radius:28px;padding:28px 32px;margin-bottom:20px">
<div style="flex-shrink:0;width:62px;height:62px;border-radius:50%;background:var(--sky);color:var(--navy);font-size:32px;font-weight:800;display:flex;align-items:center;justify-content:center">{n}</div>
<div><div style="font-size:38px;font-weight:800;color:#fff;line-height:1.15">{q}</div>
<div style="display:inline-block;margin-top:14px;background:rgba(156,197,228,.16);color:var(--sky);border-radius:999px;padding:9px 20px;font-size:25px;font-weight:700">{a}</div></div></div>'''
page(2,"dark","INSTITUCIONAL",f"""
<h1>A reunião de segunda<br><em>começa com os números prontos.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="font-size:24px;font-weight:700;color:var(--sky);letter-spacing:.1em;margin-bottom:18px">PAUTA DA SEMANA</div>
{item(1,'Estamos acima do ano passado?','Comparativos YoY e MoM')}
{item(2,'Quais imóveis ficaram para trás?','Ranking de imóveis')}
{item(3,'O que pede atenção esta semana?','Alertas operacionais')}
</div>""")

# 3 Você sabia: ritmo de reservas (on the books vs mesmo ponto do ano passado)
def bar(lbl,v,c,tc):
    return f'''<div style="margin-bottom:30px"><div style="font-size:28px;font-weight:700;color:{tc}">{lbl}</div>
<div style="display:flex;align-items:center;gap:22px;margin-top:12px">
<div style="height:64px;width:{v*9:.0f}px;background:{c};border-radius:10px"></div>
<div style="font-size:52px;font-weight:800;color:{tc}">{v}%</div></div></div>'''
page(3,"light","VOCÊ SABIA?",f"""
<h1 style="font-size:74px">45% de dezembro já reservado.<br><em>Isso é bom ou ruim?</em></h1>
<div class="stage" style="padding-top:26px">
<div style="{CARD};padding:36px 40px 22px">
<div style="font-size:24px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:26px">OCUPAÇÃO DE DEZEMBRO JÁ RESERVADA EM 20/11</div>
{bar('Este ano',45,'var(--blue)','var(--navy)')}
{bar('Ano passado, na mesma data',58,'#B4CBDD','#6B7F93')}
<div style="border-top:2px solid #E3EAF1;padding-top:20px;font-size:30px;font-weight:800;color:#B5553C">13 pontos atrás, faltando 11 dias.</div>
<div class="note" style="margin-top:12px">Exemplo ilustrativo</div>
</div>
</div>""")
print("ok")
