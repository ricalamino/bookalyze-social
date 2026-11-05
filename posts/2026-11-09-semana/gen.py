import pathlib, re
src=pathlib.Path('/home/claude/bookalyze-social/template/exemplo_lote1.py').read_text()
BASE=re.search(r'BASE = """(.*?)"""',src,re.S).group(1)
D=pathlib.Path('/home/claude/build')
def page(n,theme,tag,body):
    logo="logo_white.png" if theme=="dark" else "logo_color.png"
    (D/f"post{n}.html").write_text(BASE%dict(theme=theme,tag=tag,body=body,logo=logo),encoding="utf-8")
CARD="background:#fff;border-radius:28px;box-shadow:0 8px 30px rgba(42,73,106,.08)"

# 1 Você sabia: noites bloqueadas e ocupação (18 vendidas, 6 bloqueadas, 6 livres em 30)
OC="background:var(--blue)"
BL="background:repeating-linear-gradient(135deg,var(--coral) 0 7px,#F2C2B4 7px 14px)"
FR="background:#E3EAF1"
states=[OC]*5+[BL]*3+[OC]*6+[FR]*2+[OC]*3+[BL]*3+[OC]*4+[FR]*4
cells="".join(f'<div style="height:64px;border-radius:10px;{s}"></div>' for s in states)
def leg(s,t): return f'<div style="display:flex;align-items:center;gap:12px;font-size:25px;font-weight:700;color:var(--navy)"><div style="width:30px;height:30px;border-radius:7px;{s}"></div>{t}</div>'
def num(v,l,c): return f'''<div style="flex:1;{CARD};padding:28px 32px">
<div style="font-size:88px;font-weight:800;line-height:1;color:{c}">{v}</div>
<div style="font-size:27px;font-weight:700;color:var(--navy);margin-top:12px;line-height:1.2">{l}</div></div>'''
page(1,"light","VOCÊ SABIA?",f"""
<h1>Noite bloqueada<br><em>muda sua ocupação.</em></h1>
<div class="stage" style="padding-top:26px">
<div style="{CARD};padding:30px 34px 26px">
<div style="font-size:24px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:16px">UM IMÓVEL, 30 NOITES NO MÊS</div>
<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:8px">{cells}</div>
<div style="display:flex;justify-content:space-between;margin-top:20px">{leg(OC,'18 vendidas')}{leg(BL,'6 bloqueadas')}{leg(FR,'6 livres')}</div>
</div>
<div style="display:flex;gap:22px;margin-top:22px">
{num('60%','sobre as 30 noites do mês','var(--navy)')}
{num('75%','sobre as 24 noites disponíveis','var(--blue)')}
</div>
<div class="note" style="margin-top:14px">Exemplo ilustrativo · Mesmo imóvel, mesmas 18 noites vendidas</div>
</div>""")

# 2 Institucional: para equipes comercial, financeira e operacional
def team(t,q,items):
    li="".join(f'<span style="background:rgba(156,197,228,.16);color:var(--sky);border-radius:999px;padding:9px 20px;font-size:25px;font-weight:700;white-space:nowrap">{i}</span>' for i in items)
    return f'''<div style="background:rgba(255,255,255,.07);border-radius:28px;padding:28px 34px;margin-bottom:20px">
<div style="font-size:24px;font-weight:800;letter-spacing:.1em;color:var(--sky)">{t}</div>
<div style="font-size:40px;font-weight:800;color:#fff;line-height:1.15;margin-top:8px">{q}</div>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:16px">{li}</div></div>'''
page(2,"dark","PARA TODA A EQUIPE",f"""
<h1>Três equipes,<br><em>o mesmo painel.</em></h1>
<div class="stage" style="padding-top:30px">
{team('COMERCIAL','A diária está certa?',['RevPAR','Diária média','YoY e MoM'])}
{team('FINANCEIRO','O mês fecha com o proprietário?',['Prestação de contas','Ajustes manuais'])}
{team('OPERACIONAL','O que pede atenção hoje?',['Alertas operacionais','Ocupação'])}
</div>""")

# 3 Você sabia: a diária média esconde a semana (média simples = R$ 250)
days=[("Seg",180),("Ter",170),("Qua",170),("Qui",190),("Sex",400),("Sáb",430),("Dom",210)]
assert sum(v for _,v in days)/7==250
H=430; MAX=430; scale=H/MAX
bars=""
for d,v in days:
    c,t=("var(--blue)","#fff") if v>250 else ("#B4CBDD","var(--navy)")
    bars+=f'''<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;height:100%">
<div style="width:100%;height:{v*scale:.0f}px;background:{c};border-radius:8px 8px 0 0;text-align:center;padding-top:12px;font-size:28px;font-weight:800;color:{t}">{v}</div></div>'''
lab="".join(f'<div style="flex:1;text-align:center;font-size:26px;font-weight:700;color:var(--navy)">{d}</div>' for d,_ in days)
page(3,"light","VOCÊ SABIA?",f"""
<h1 style="font-size:70px">Diária média de R$ 250.<br><em>Nenhuma noite saiu por isso.</em></h1>
<div class="stage" style="padding-top:26px">
<div style="{CARD};padding:30px 36px 26px">
<div style="font-size:24px;font-weight:700;color:var(--blue);letter-spacing:.08em;margin-bottom:10px">DIÁRIA POR DIA DA SEMANA (R$)</div>
<div style="position:relative;height:440px;display:flex;gap:14px;border-bottom:2px solid #C9D6E2">{bars}
<div style="position:absolute;left:0;right:0;bottom:{250*scale:.0f}px;border-top:3px dashed var(--coral);z-index:1"></div>
<div style="position:absolute;left:0;bottom:{250*scale+8:.0f}px;font-size:26px;font-weight:800;color:#B5553C;background:#fff;padding:0 8px 0 0;z-index:2">Média: R$ 250</div>
</div>
<div style="display:flex;gap:14px;margin-top:10px">{lab}</div>
<div class="note" style="margin-top:12px">Exemplo ilustrativo · Uma semana com todas as noites vendidas</div>
</div>
</div>""")
print("ok")
