import pathlib, re, sys
sys.path.insert(0,'/home/claude/bookalyze-social/template')
src=pathlib.Path('/home/claude/bookalyze-social/template/exemplo_lote1.py').read_text()
BASE=re.search(r'BASE = """(.*?)"""',src,re.S).group(1)
D=pathlib.Path('/home/claude/build')
def page(n,theme,tag,body):
    logo="logo_white.png" if theme=="dark" else "logo_color.png"
    (D/f"post{n}.html").write_text(BASE%dict(theme=theme,tag=tag,body=body,logo=logo),encoding="utf-8")

# 1 Você sabia: sazonalidade YoY
def col(lbl,val,h,c,txt="var(--navy)"):
    return f'''<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;width:150px">
<div style="font-size:34px;font-weight:800;color:{txt};margin-bottom:12px">{val}</div>
<div style="width:110px;height:{h}px;background:{c};border-radius:12px 12px 4px 4px"></div>
<div style="font-size:24px;font-weight:700;color:#6B7F93;margin-top:14px;text-align:center;line-height:1.2">{lbl}</div></div>'''
page(1,"light","VOCÊ SABIA?",f"""
<h1>Compare agosto com <em>agosto do ano passado.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="background:#fff;border-radius:28px;padding:40px 44px 30px;box-shadow:0 8px 30px rgba(42,73,106,.08)">
<div style="font-size:26px;font-weight:700;color:var(--blue);letter-spacing:.08em">OCUPAÇÃO DO PORTFÓLIO</div>
<div style="display:flex;justify-content:space-around;align-items:flex-end;height:280px;margin-top:50px">
{col('Jul/26','82%',215,'#C9D8E6','#6B7F93')}{col('Ago/26','64%',168,'var(--blue)')}{col('Ago/25','58%',152,'#C9D8E6','#6B7F93')}</div>
<div style="display:flex;justify-content:space-between;margin-top:26px;font-size:28px;font-weight:800">
<span style="color:#C0573F">vs mês anterior: −18 pts</span><span style="color:var(--blue)">vs ano anterior: +6 pts</span></div>
<div class="note">Exemplo ilustrativo</div></div>
<p class="sub" style="margin-top:40px">Julho tem férias escolares. Agosto cair é sazonalidade, não problema. O comparativo justo é com o mesmo mês do ano anterior (YoY).</p>
</div>""")

# 2 Novidade: ranking de imóveis
rows=[("Imóvel A","R$ 312",1.0,False),("Imóvel B","R$ 268",.86,False),("Imóvel C","R$ 241",.77,False),("Imóvel D","R$ 174",.56,False),("Imóvel E","R$ 129",.41,True)]
bars=""
for i,(n,v,f,low) in enumerate(rows,1):
    c="var(--coral)" if low else ("var(--sky)" if i==1 else "var(--blue)")
    bars+=f'''<div style="display:flex;align-items:center;gap:22px;margin:16px 0">
<div style="width:44px;font-size:30px;font-weight:800;color:var(--sky)">{i}º</div>
<div style="width:170px;flex-shrink:0;font-size:28px;font-weight:700;color:#D5E3EF">{n}</div>
<div style="height:52px;width:{f*420:.0f}px;background:{c};border-radius:10px"></div>
<div style="font-size:28px;font-weight:800;white-space:nowrap;color:{"var(--coral)" if low else "#fff"}">{v}</div></div>'''
page(2,"dark","NOVIDADE",f"""
<h1>Seus imóveis, <em>do melhor ao que pede atenção.</em></h1>
<div class="stage">
<div style="background:rgba(255,255,255,.06);border-radius:28px;padding:40px 44px">
<div style="font-size:26px;font-weight:700;color:var(--sky);letter-spacing:.08em;margin-bottom:10px">RANKING POR REVPAR · SETEMBRO</div>
{bars}
<div class="note">Exemplo ilustrativo</div></div>
<p class="sub">Ranking de imóveis por performance no Bookalyze. Você vê na hora quem puxa o portfólio e quem ficou para trás.</p>
</div>""")

# 3 Institucional: cobrança por portfólio
def team(t,d):
    return f'''<div style="flex:1;background:#fff;border-radius:24px;padding:30px 26px;box-shadow:0 8px 30px rgba(42,73,106,.08)">
<div style="width:56px;height:56px;border-radius:50%;background:rgba(82,135,174,.18);display:flex;align-items:center;justify-content:center"><div style="width:22px;height:22px;border-radius:50%;background:var(--blue)"></div></div>
<div style="font-size:32px;font-weight:800;color:var(--navy);margin-top:20px">{t}</div>
<div style="font-size:24px;color:#6B7F93;margin-top:8px;line-height:1.3">{d}</div></div>'''
page(3,"light","PARA A EQUIPE TODA",f"""
<h1>Você paga pelo portfólio. <em>Não por usuário.</em></h1>
<div class="stage" style="padding-top:20px">
<div style="display:flex;gap:24px">{team('Comercial','Diária média e RevPAR')}{team('Financeiro','Receita e prestação de contas')}{team('Operação','Ocupação e reservas')}</div>
<div style="margin-top:34px;background:var(--navy);color:#fff;border-radius:24px;padding:30px 36px;font-size:32px;font-weight:700;line-height:1.35">Coloque quem precisa no painel. <span style="color:var(--sky)">A conta não sobe a cada login novo.</span></div>
<p class="sub" style="margin-top:36px">Cada time olha os mesmos números, no mesmo painel. Sem planilha paralela, sem versão diferente da verdade.</p>
</div>""")
print("ok")
