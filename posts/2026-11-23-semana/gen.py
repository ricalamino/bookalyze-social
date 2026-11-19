import pathlib, re
src=pathlib.Path('/home/claude/bookalyze-social/template/exemplo_lote1.py').read_text()
BASE=re.search(r'BASE = """(.*?)"""',src,re.S).group(1)
D=pathlib.Path('/home/claude/build')
def page(n,theme,tag,body):
    logo="logo_white.png" if theme=="dark" else "logo_color.png"
    (D/f"post{n}.html").write_text(BASE%dict(theme=theme,tag=tag,body=body,logo=logo),encoding="utf-8")
CARD="background:#fff;border-radius:28px;box-shadow:0 8px 30px rgba(42,73,106,.08)"

# 1 Você sabia: a nota geral esconde a nota por categoria
cats=[("Localização",4.9),("Comunicação",4.9),("Check-in",4.9),("Precisão",4.8),("Custo-benefício",4.7),("Limpeza",4.3)]
rows=""
for name,v in cats:
    low=v<4.5
    col="#B5553C" if low else "var(--blue)"
    w=(v-3.5)/1.5*470
    rows+=f'''<div style="display:flex;align-items:center;gap:22px;margin:13px 0">
<div style="width:250px;flex-shrink:0;font-size:28px;font-weight:{800 if low else 700};color:{'#B5553C' if low else 'var(--navy)'}">{name}</div>
<div style="height:44px;width:{w:.0f}px;background:{'var(--coral)' if low else 'var(--sky)'};border-radius:9px"></div>
<div style="font-size:30px;font-weight:800;color:{col}">{str(v).replace('.',',')}</div></div>'''
page(1,"light","VOCÊ SABIA?",f"""
<h1>Nota 4,8 no geral.<br><em>4,3 em limpeza.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="{CARD};padding:34px 40px 26px">
<div style="font-size:24px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:12px">NOTAS POR CATEGORIA · DE 0 A 5</div>
{rows}
<div style="border-top:2px solid #E3EAF1;margin-top:18px;padding-top:18px;font-size:30px;font-weight:800;color:var(--navy)">A média alta esconde onde está o problema.</div>
<div class="note" style="margin-top:10px">Exemplo ilustrativo</div>
</div>
</div>""")

# 2 Institucional: do PMS ao painel em 3 passos
def item(n,q,a):
    return f'''<div style="display:flex;gap:26px;align-items:flex-start;background:rgba(255,255,255,.07);border-radius:28px;padding:28px 32px;margin-bottom:20px">
<div style="flex-shrink:0;width:62px;height:62px;border-radius:50%;background:var(--sky);color:var(--navy);font-size:32px;font-weight:800;display:flex;align-items:center;justify-content:center">{n}</div>
<div><div style="font-size:38px;font-weight:800;color:#fff;line-height:1.15">{q}</div>
<div style="display:inline-block;margin-top:14px;background:rgba(156,197,228,.16);color:var(--sky);border-radius:999px;padding:9px 20px;font-size:25px;font-weight:700">{a}</div></div></div>'''
page(2,"dark","INSTITUCIONAL",f"""
<h1>Do PMS ao painel.<br><em>Sem planilha no meio.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="font-size:24px;font-weight:700;color:var(--sky);letter-spacing:.1em;margin-bottom:18px">COMO FUNCIONA</div>
{item(1,'Você conecta o seu PMS','Stays (App Center) ou Hostaway')}
{item(2,'As reservas viram métricas','RevPAR, ocupação e diária média por imóvel')}
{item(3,'A equipe acompanha junto','Comercial, financeiro e operacional')}
</div>""")

# 3 Você sabia: Black Friday, ocupação sobe e RevPAR cai
def card(lbl,occ,adr,rev,warn):
    border="3px solid var(--coral)" if warn else "3px solid transparent"
    badge='<div style="position:absolute;top:-22px;right:28px;background:var(--coral);color:#fff;font-weight:800;font-size:22px;padding:8px 18px;border-radius:999px">RENDE MENOS</div>' if warn else ""
    return f"""<div style="flex:1;{CARD};padding:34px 36px 30px;border:{border};position:relative">{badge}
<div style="font-size:30px;font-weight:800;color:var(--navy)">{lbl}</div>
<div style="font-size:24px;color:#6B7F93;margin-top:26px">Ocupação</div><div style="font-size:56px;font-weight:800;color:var(--navy)">{occ}</div>
<div style="font-size:24px;color:#6B7F93;margin-top:14px">Diária média</div><div style="font-size:56px;font-weight:800;color:var(--navy)">{adr}</div>
<div style="height:2px;background:#E3EAF1;margin:18px 0"></div>
<div style="font-size:24px;color:#6B7F93">RevPAR</div><div style="font-size:64px;font-weight:800;color:{'#B5553C' if warn else 'var(--blue)'}">{rev}</div></div>"""
page(3,"light","VOCÊ SABIA?",f"""
<h1 style="font-size:68px">O desconto lotou a agenda.<br><em>E a receita?</em></h1>
<div class="stage" style="padding-top:30px">
<div style="display:flex;gap:32px">{card('Sem desconto','60%','R$ 400','R$ 240',False)}{card('Com 25% off','73%','R$ 300','R$ 220',True)}</div>
<p class="sub" style="margin-top:34px;font-size:32px"><b style="color:var(--navy);font-weight:800">RevPAR = diária média × ocupação.</b><br>Mais noites vendidas não garantem mais receita.</p>
<div class="note">Exemplo ilustrativo · mês de 30 noites</div>
</div>""")
print("ok")
