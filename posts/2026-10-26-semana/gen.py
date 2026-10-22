import pathlib, re
src=pathlib.Path('/home/claude/bookalyze-social/template/exemplo_lote1.py').read_text()
BASE=re.search(r'BASE = """(.*?)"""',src,re.S).group(1)
D=pathlib.Path('/home/claude/build')
def page(n,theme,tag,body):
    logo="logo_white.png" if theme=="dark" else "logo_color.png"
    (D/f"post{n}.html").write_text(BASE%dict(theme=theme,tag=tag,body=body,logo=logo),encoding="utf-8")
CARD="background:#fff;border-radius:28px;box-shadow:0 8px 30px rgba(42,73,106,.08)"

# 1 Você sabia: taxa de cancelamento por canal
def bar(ch,pct,w,c):
    return f'''<div style="display:flex;align-items:center;gap:22px;margin:18px 0">
<div style="width:190px;flex-shrink:0;font-size:30px;font-weight:700;color:var(--navy)">{ch}</div>
<div style="flex:1;height:56px;background:#EEF2F6;border-radius:12px;position:relative">
<div style="height:56px;width:{w}%;background:{c};border-radius:12px"></div></div>
<div style="width:90px;text-align:right;font-size:34px;font-weight:800;color:{c}">{pct}</div></div>'''
page(1,"light","VOCÊ SABIA?",f"""
<h1>Cada canal cancela <em>de um jeito.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="{CARD};padding:40px 44px 30px">
<div style="font-size:26px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:10px">TAXA DE CANCELAMENTO · ÚLTIMOS 90 DIAS</div>
{bar('Canal A','6%',27,'var(--blue)')}{bar('Canal B','22%',100,'var(--coral)')}{bar('Direto','3%',14,'var(--blue)')}
<div class="note">Exemplo ilustrativo · Portfólio todo: 11%</div></div>
<p class="sub" style="margin-top:40px">A média do portfólio esconde o canal que devolve as datas em cima da hora. Olhe a taxa por canal antes de mexer na política de cancelamento.</p>
</div>""")

# 2 Institucional: sem planilha, sem esperar o fechamento
def step(t,strike=True):
    return f'''<div style="display:flex;gap:16px;align-items:flex-start;margin:14px 0">
<div style="width:30px;height:30px;border-radius:8px;border:3px solid #B9C7D4;flex-shrink:0;margin-top:4px"></div>
<div style="font-size:29px;font-weight:700;color:#7C8FA2;line-height:1.25">{t}</div></div>'''
page(2,"dark","SEM PLANILHA",f"""
<h1>Não espere o mês fechar <em>para saber como foi.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="display:flex;gap:26px">
<div style="flex:1;background:#fff;border-radius:28px;padding:34px 30px">
<div style="font-size:24px;font-weight:800;letter-spacing:.1em;color:#7C8FA2">DO JEITO ANTIGO</div>
{step('Exportar reservas do PMS')}{step('Colar na planilha')}{step('Conferir fórmula quebrada')}{step('Esperar o fechamento')}</div>
<div style="flex:1;background:rgba(156,197,228,.14);border:3px solid var(--sky);border-radius:28px;padding:34px 30px;display:flex;flex-direction:column">
<div style="font-size:24px;font-weight:800;letter-spacing:.1em;color:var(--sky)">NO BOOKALYZE</div>
<div style="font-size:40px;font-weight:800;color:#fff;line-height:1.15;margin-top:22px">Abre o painel.</div>
<div style="font-size:28px;font-weight:500;color:#D5E3EF;line-height:1.3;margin-top:16px">RevPAR, ocupação e diária média do mês em andamento, por imóvel.</div></div>
</div>
<p class="sub" style="margin-top:38px">Integração com Stays e Hostaway: os dados chegam sozinhos. Você decide com o mês ainda em curso.</p>
</div>""")

# 3 Institucional: demo de 20 minutos
items=["RevPAR, ocupação e diária média por imóvel","Comparativos YoY e MoM","Prestação de contas por acomodação","Alertas operacionais","Integração com Stays e Hostaway"]
lis="".join(f'''<div style="display:flex;gap:18px;align-items:center;margin:13px 0">
<svg width="34" height="34" viewBox="0 0 34 34" style="flex-shrink:0"><circle cx="17" cy="17" r="17" fill="#5287AE"/><path d="M10 17.5 L15 22.5 L24 12.5" stroke="#fff" stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
<span style="font-size:30px;font-weight:700;color:#fff">{t}</span></div>''' for t in items)
ring='''<svg width="230" height="230" viewBox="0 0 230 230"><circle cx="115" cy="115" r="98" stroke="rgba(255,255,255,.12)" stroke-width="22" fill="none"/>
<circle cx="115" cy="115" r="98" stroke="#9CC5E4" stroke-width="22" fill="none" stroke-linecap="round" stroke-dasharray="205.25 615.75" transform="rotate(-90 115 115)"/>
<text x="115" y="122" text-anchor="middle" font-family="RH" font-weight="800" font-size="74" fill="#fff">20</text>
<text x="115" y="160" text-anchor="middle" font-family="RH" font-weight="700" font-size="26" fill="#9CC5E4">MINUTOS</text></svg>'''
page(3,"dark","DEMO",f"""
<h1>20 minutos <em>para ver o painel.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="display:flex;gap:40px;align-items:center;background:rgba(255,255,255,.06);border-radius:28px;padding:38px 40px">
<div style="flex-shrink:0">{ring}</div><div>{lis}</div></div>
<p class="sub" style="margin-top:38px">Uma conversa rápida: você vê o Bookalyze funcionando e tira as dúvidas sobre o seu portfólio.</p>
</div>""")
print("ok")
