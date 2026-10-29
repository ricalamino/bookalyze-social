import pathlib, re
src=pathlib.Path('/home/claude/bookalyze-social/template/exemplo_lote1.py').read_text()
BASE=re.search(r'BASE = """(.*?)"""',src,re.S).group(1)
D=pathlib.Path('/home/claude/build')
def page(n,theme,tag,body):
    logo="logo_white.png" if theme=="dark" else "logo_color.png"
    (D/f"post{n}.html").write_text(BASE%dict(theme=theme,tag=tag,body=body,logo=logo),encoding="utf-8")
CARD="background:#fff;border-radius:28px;box-shadow:0 8px 30px rgba(42,73,106,.08)"

# 1 Você sabia: os 20% piores imóveis
vals=[220,205,198,190,184,176,168,160,118,104]
rows=""
for i,v in enumerate(vals):
    c="var(--coral)" if i>=8 else "var(--blue)"
    rows+=f'''<div style="display:flex;align-items:center;gap:18px;margin:6px 0">
<div style="width:140px;flex-shrink:0;font-size:24px;font-weight:700;color:{'var(--coral)' if i>=8 else 'var(--navy)'}">Imóvel {chr(65+i)}</div>
<div style="flex:1;height:30px"><div style="height:30px;width:{v/220*100:.0f}%;background:{c};border-radius:8px"></div></div>
<div style="width:110px;text-align:right;font-size:24px;font-weight:800;color:{c}">R$ {v}</div></div>'''
qs=["Diária fora da época?","Estadia mínima alta?","Anúncio desatualizado?","Avaliações recentes?"]
chips="".join(f'<div style="background:rgba(224,122,95,.12);color:#B5553C;border-radius:16px;padding:16px 20px;font-size:25px;font-weight:700">{q}</div>' for q in qs)
page(1,"light","VOCÊ SABIA?",f"""
<h1>Comece pelos <em>20% de baixo.</em></h1>
<div class="stage" style="padding-top:26px">
<div style="{CARD};padding:30px 40px 24px">
<div style="font-size:24px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:6px">RANKING POR REVPAR · OUTUBRO</div>
{rows}
<div class="note" style="margin-top:10px">Exemplo ilustrativo · 10 imóveis</div></div>
<div style="font-size:26px;font-weight:800;color:var(--navy);margin-top:30px;margin-bottom:14px">Antes de qualquer decisão, pergunte:</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">{chips}</div>
</div>""")

# 2 Novidade: comparativos YoY e MoM
def cmp(tag,q,lbl,val,c):
    return f'''<div style="flex:1;background:rgba(255,255,255,.07);border-radius:28px;padding:34px 32px;display:flex;flex-direction:column">
<div style="font-size:24px;font-weight:800;letter-spacing:.1em;color:var(--sky)">{tag}</div>
<div style="font-size:34px;font-weight:800;color:#fff;line-height:1.15;margin-top:16px;min-height:120px">{q}</div>
<div style="height:2px;background:rgba(255,255,255,.12);margin:22px 0"></div>
<div style="font-size:24px;color:#B9CCDD">{lbl}</div>
<div style="font-size:76px;font-weight:800;color:{c};line-height:1.1;margin-top:6px">{val}</div></div>'''
page(2,"dark","NOVIDADE",f"""
<h1>Dois comparativos, <em>duas perguntas.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="display:flex;gap:26px">
{cmp('MoM','O mês melhorou em relação ao anterior?','RevPAR de outubro vs. setembro','+12%','var(--sky)')}
{cmp('YoY','Cresceu de verdade, descontando a época?','RevPAR de outubro vs. out/2025','−4%','var(--coral)')}
</div>
<div class="note">Exemplo ilustrativo</div>
<p class="sub" style="margin-top:26px">O mesmo mês pode subir no MoM e cair no YoY. No Bookalyze você vê os dois comparativos sem montar planilha.</p>
</div>""")

# 3 Institucional: RevPAR, ocupação e diária média por imóvel no mesmo painel
data=[("Imóvel A","82%","R$ 240","R$ 197",False),("Imóvel B","64%","R$ 330","R$ 211",True),("Imóvel C","91%","R$ 180","R$ 164",False),("Imóvel D","70%","R$ 260","R$ 182",False)]
th='<div style="display:grid;grid-template-columns:1.3fr 1fr 1.1fr 1.1fr;gap:10px;font-size:22px;font-weight:800;letter-spacing:.08em;color:var(--blue);padding:0 8px 14px;border-bottom:2px solid #E3EAF1"><div>IMÓVEL</div><div>OCUPAÇÃO</div><div>DIÁRIA MÉDIA</div><div style="text-align:right">REVPAR</div></div>'
tr=""
for n,o,a,r,w in data:
    bg="background:rgba(82,135,174,.10);" if w else ""
    tr+=f'<div style="display:grid;grid-template-columns:1.3fr 1fr 1.1fr 1.1fr;gap:10px;align-items:center;font-size:30px;font-weight:700;color:var(--navy);padding:20px 8px;border-bottom:2px solid #EEF2F6;border-radius:12px;{bg}"><div>{n}</div><div>{o}</div><div>{a}</div><div style="text-align:right;font-weight:800;color:{"var(--blue)" if w else "var(--navy)"}">{r}</div></div>'
page(3,"light","NUM SÓ LUGAR",f"""
<h1>Três métricas, <em>por imóvel, no mesmo painel.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="{CARD};padding:34px 36px 26px">{th}{tr}
<div class="note" style="margin-top:16px">Exemplo ilustrativo · RevPAR = diária média × ocupação</div></div>
<p class="sub" style="margin-top:36px">O imóvel mais ocupado nem sempre é o que mais rende. Com as três lado a lado, você enxerga onde mexer.</p>
</div>""")
print("ok")
