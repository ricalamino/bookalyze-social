import pathlib, re
src=pathlib.Path('/home/claude/bookalyze-social/template/exemplo_lote1.py').read_text()
BASE=re.search(r'BASE = """(.*?)"""',src,re.S).group(1)
D=pathlib.Path('/home/claude/build')
def page(n,theme,tag,body):
    logo="logo_white.png" if theme=="dark" else "logo_color.png"
    (D/f"post{n}.html").write_text(BASE%dict(theme=theme,tag=tag,body=body,logo=logo),encoding="utf-8")

# 1 Você sabia: permanência média x turnover
def dots(n,c):
    return "".join(f'<div style="width:30px;height:30px;border-radius:8px;background:{c if i<n else "#E3EAF1"}"></div>' for i in range(30))
def card(lbl,stays,turn,cost,c,tc):
    return f'''<div style="background:#fff;border-radius:24px;padding:30px 34px;box-shadow:0 8px 30px rgba(42,73,106,.08);margin-bottom:22px">
<div style="display:flex;justify-content:space-between;align-items:baseline">
<div style="font-size:30px;font-weight:800;color:var(--navy)">{lbl}</div>
<div style="font-size:24px;font-weight:700;color:#6B7F93">{stays}</div></div>
<div style="display:grid;grid-template-columns:repeat(15,30px);gap:8px;margin-top:20px">{dots(turn,c)}</div>
<div style="display:flex;justify-content:space-between;margin-top:20px;font-size:28px;font-weight:800">
<span style="color:{tc}">{turn} limpezas no mês</span><span style="color:{tc}">{cost}</span></div></div>'''
page(1,"light","VOCÊ SABIA?",f"""
<h1>Estadia curta <em>multiplica a limpeza.</em></h1>
<div class="stage" style="padding-top:34px">
<div style="font-size:26px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:18px">MESMO IMÓVEL · 30 NOITES OCUPADAS</div>
{card('Permanência média 2 noites','15 estadias',15,'R$ 2.250','var(--coral)','var(--coral)')}
{card('Permanência média 5 noites','6 estadias',6,'R$ 900','var(--blue)','var(--blue)')}
<div class="note">Exemplo ilustrativo · limpeza a R$ 150 por check-out</div>
<p class="sub" style="margin-top:22px">Mesma ocupação, custo de virada bem diferente. Olhe a permanência média antes de mexer na estadia mínima.</p>
</div>""")

# 2 Novidade: alertas operacionais
def alert(cat,txt,c):
    return f'''<div style="display:flex;gap:24px;align-items:center;background:rgba(255,255,255,.07);border-left:8px solid {c};border-radius:18px;padding:26px 30px;margin-bottom:20px">
<div style="width:20px;height:20px;border-radius:50%;background:{c};flex-shrink:0"></div>
<div><div style="font-size:22px;font-weight:800;letter-spacing:.1em;color:{c}">{cat}</div>
<div style="font-size:30px;font-weight:700;color:#fff;margin-top:6px;line-height:1.25">{txt}</div></div></div>'''
page(2,"dark","NOVIDADE",f"""
<h1>O painel avisa <em>o que pede atenção.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="font-size:26px;font-weight:700;color:var(--sky);letter-spacing:.08em;margin-bottom:22px">ALERTAS OPERACIONAIS · HOJE</div>
{alert('OCUPAÇÃO','Imóvel C com datas vazias na próxima semana','var(--coral)')}
{alert('DIÁRIA','Imóvel A abaixo da média do portfólio','#F2C14E')}
{alert('AVALIAÇÕES','2 hóspedes ainda podem avaliar a estadia','var(--sky)')}
<div class="note">Exemplo ilustrativo</div>
<p class="sub" style="margin-top:26px">Em vez de caçar o problema no relatório, você abre o Bookalyze e começa pelo que importa.</p>
</div>""")

# 3 Institucional: a partir de 2 imóveis
def house(c,sz=64):
    return f'''<svg width="{sz}" height="{sz}" viewBox="0 0 64 64"><path d="M8 30 L32 10 L56 30 V56 H8 Z" fill="{c}"/><rect x="18" y="38" width="6" height="12" fill="#fff"/><rect x="29" y="32" width="6" height="18" fill="#fff"/><rect x="40" y="26" width="6" height="24" fill="#fff"/></svg>'''
def group(n,lbl,c):
    sz=64 if n<=6 else 50
    hs="".join(house(c,sz) for _ in range(n))
    return f'''<div style="flex:1;background:#fff;border-radius:24px;padding:28px 22px;box-shadow:0 8px 30px rgba(42,73,106,.08);display:flex;flex-direction:column;align-items:center">
<div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center;height:180px;align-content:center;width:220px">{hs}</div>
<div style="font-size:30px;font-weight:800;color:var(--navy);margin-top:16px">{lbl}</div></div>'''
chips="".join(f'<span style="background:var(--navy);color:#fff;border-radius:999px;padding:14px 26px;font-size:28px;font-weight:700">{t}</span>' for t in ["RevPAR","Ocupação","Diária média"])
page(3,"light","PARA QUEM É",f"""
<h1>Tem 2 imóveis? <em>Já vale ter BI.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="display:flex;gap:22px">{group(2,'2 imóveis','var(--sky)')}{group(6,'10 imóveis','var(--blue)')}{group(12,'50+','var(--navy)')}</div>
<div style="display:flex;gap:16px;margin-top:34px;flex-wrap:wrap">{chips}</div>
<p class="sub" style="margin-top:30px">Os mesmos números, por imóvel e no mesmo painel. Do segundo apartamento ao portfólio inteiro.</p>
</div>""")
print("ok")
