import pathlib
D = pathlib.Path(__file__).parent

BASE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:RH;font-weight:500;src:url(red-hat-display-latin-500-normal.woff2)}
@font-face{font-family:RH;font-weight:700;src:url(red-hat-display-latin-700-normal.woff2)}
@font-face{font-family:RH;font-weight:800;src:url(red-hat-display-latin-800-normal.woff2)}
:root{--navy:#2A496A;--blue:#5287AE;--sky:#9CC5E4;--bg:#F3F6F9;--coral:#E07A5F;--ink:#1C2F44}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;font-family:RH,sans-serif;font-weight:500}
.p{width:1080px;height:1350px;padding:96px 88px 0;position:relative;overflow:hidden;display:flex;flex-direction:column}
.dark{background:var(--navy);color:#fff}
.light{background:var(--bg);color:var(--ink)}
.tag{align-self:flex-start;font-weight:800;font-size:26px;letter-spacing:.14em;padding:14px 26px;border-radius:999px}
.dark .tag{background:rgba(156,197,228,.16);color:var(--sky)}
.light .tag{background:rgba(82,135,174,.14);color:var(--blue)}
h1{font-weight:800;font-size:80px;line-height:1.04;letter-spacing:-.02em;margin-top:44px}
.dark h1 em{font-style:normal;color:var(--sky)}
.light h1{color:var(--navy)} .light h1 em{font-style:normal;color:var(--blue)}
.sub{font-size:36px;line-height:1.35;margin-top:28px}
.dark .sub{color:#D5E3EF} .light .sub{color:#4A6178}
.foot{position:absolute;left:0;right:0;bottom:0;height:150px;display:flex;align-items:center;justify-content:space-between;padding:0 88px}
.dark .foot{border-top:2px solid rgba(255,255,255,.12)}
.light .foot{border-top:2px solid rgba(42,73,106,.12)}
.foot img{height:70px}
.foot span{font-size:26px;font-weight:700;opacity:.8}
.note{font-size:22px;opacity:.6;margin-top:18px}
.stage{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:200px}
</style></head><body><div class="p %(theme)s">
<div class="tag">%(tag)s</div>
%(body)s
<div class="foot"><img src="%(logo)s"><span>bookalyze.it</span></div>
</div></body></html>"""


def page(n, theme, tag, body):
    logo = "logo_white.png" if theme == "dark" else "logo_color.png"
    (D / f"post{n}.html").write_text(BASE % dict(theme=theme, tag=tag, body=body, logo=logo), encoding="utf-8")


# 1 ─ Institucional: ranking de lucro
rows = [("Imóvel A", 8.2), ("Imóvel B", 6.1), ("Imóvel C", 4.4), ("Imóvel D", 1.3), ("Imóvel E", -2.1)]
mx = 8.2
bars = ""
for name, v in rows:
    w = abs(v) / mx * 470
    col = "var(--coral)" if v < 0 else "var(--sky)"
    val = ("−" if v < 0 else "") + f"R$ {abs(v):.1f} mil".replace(".", ",")
    bars += f"""<div style="display:flex;align-items:center;gap:24px;margin:14px 0">
<div style="width:170px;flex-shrink:0;font-size:28px;font-weight:700;color:#D5E3EF">{name}</div>
<div style="height:54px;width:{w:.0f}px;background:{col};border-radius:10px"></div>
<div style="font-size:28px;font-weight:800;white-space:nowrap;color:{col}">{val}</div></div>"""
page(1, "dark", "LUCRO POR IMÓVEL", f"""
<h1>Qual imóvel puxa sua margem.<br><em>E qual está sangrando.</em></h1>
<div class="stage">
<div style="background:rgba(255,255,255,.06);border-radius:28px;padding:40px 44px">
<div style="font-size:26px;font-weight:700;color:var(--sky);letter-spacing:.08em;margin-bottom:12px">LUCRO LÍQUIDO · AGOSTO</div>
{bars}
<div class="note">Exemplo ilustrativo</div></div>
<p class="sub">Faturamento bonito pode esconder prejuízo.<br>No Bookalyze, você vê o lucro de cada imóvel.</p>
</div>""")

# 2 ─ Você sabia: ocupação x RevPAR
def card(lbl, occ, adr, rev, win):
    border = "3px solid var(--blue)" if win else "3px solid transparent"
    badge = '<div style="position:absolute;top:-22px;right:28px;background:var(--blue);color:#fff;font-weight:800;font-size:22px;padding:8px 18px;border-radius:999px">RENDE MAIS</div>' if win else ""
    return f"""<div style="flex:1;background:#fff;border-radius:28px;padding:40px 36px;border:{border};position:relative;box-shadow:0 8px 30px rgba(42,73,106,.08)">{badge}
<div style="font-size:30px;font-weight:800;color:var(--navy)">{lbl}</div>
<div style="font-size:24px;color:#6B7F93;margin-top:26px">Ocupação</div><div style="font-size:56px;font-weight:800;color:var(--navy)">{occ}</div>
<div style="font-size:24px;color:#6B7F93;margin-top:14px">Diária média</div><div style="font-size:56px;font-weight:800;color:var(--navy)">{adr}</div>
<div style="height:2px;background:#E3EAF1;margin:24px 0"></div>
<div style="font-size:24px;color:#6B7F93">RevPAR</div><div style="font-size:64px;font-weight:800;color:{'var(--blue)' if win else 'var(--navy)'}">{rev}</div></div>"""
page(2, "light", "VOCÊ SABIA?", f"""
<h1>Ocupação alta <em>não é</em> receita alta.</h1>
<div class="stage" style="padding-top:30px">
<div style="display:flex;gap:32px">{card('Imóvel A','90%','R$ 200','R$ 180',False)}{card('Imóvel B','70%','R$ 300','R$ 210',True)}</div>
<p class="sub" style="margin-top:44px"><b style="color:var(--navy);font-weight:800">RevPAR = diária média × ocupação.</b><br>É a receita por noite disponível. Olhar só a ocupação pode esconder diária barata.</p>
<div class="note">Exemplo ilustrativo</div>
</div>""")

# 3 ─ Novidade: Bookalyze no Claude
page(3, "dark", "NOVIDADE", f"""
<h1>Agora você pode <em>perguntar</em> aos seus dados.</h1>
<div class="stage">
<div style="display:flex;flex-direction:column;gap:26px">
<div style="align-self:flex-end;max-width:760px;background:var(--blue);color:#fff;font-size:32px;line-height:1.35;padding:28px 34px;border-radius:30px 30px 8px 30px">Como foi a ocupação de agosto comparada com agosto do ano passado?</div>
<div style="align-self:flex-start;max-width:800px;background:#fff;color:var(--ink);font-size:32px;line-height:1.35;padding:28px 34px;border-radius:30px 30px 30px 8px">Agosto fechou com <b style="font-weight:800;color:var(--navy)">78% de ocupação</b>, 6 pontos acima de agosto do ano passado. O maior salto foi no Studio Centro.</div>
<div class="note" style="align-self:flex-start">Exemplo ilustrativo</div>
</div>
<p class="sub" style="margin-top:36px">O Bookalyze agora conversa com o Claude. Conecte sua conta e pergunte em português, sem abrir dashboard.</p>
</div>""")

# 4 ─ Você sabia: antecedência média
page(4, "light", "VOCÊ SABIA?", f"""
<h1>Calendário lotado cedo demais <em>pode ser diária barata.</em></h1>
<div class="stage" style="padding-top:30px">
<div style="background:#fff;border-radius:28px;padding:48px 44px;box-shadow:0 8px 30px rgba(42,73,106,.08)">
<div style="font-size:26px;font-weight:700;color:var(--blue);letter-spacing:.08em">ANTECEDÊNCIA MÉDIA DA RESERVA</div>
<div style="margin-top:34px">
<div style="font-size:28px;font-weight:700;color:#6B7F93">Média do seu portfólio</div>
<div style="display:flex;align-items:center;gap:22px;margin:12px 0 34px"><div style="height:56px;width:110px;background:#C9D8E6;border-radius:10px"></div><div style="font-size:40px;font-weight:800;color:#6B7F93">25 dias</div></div>
<div style="font-size:28px;font-weight:700;color:var(--navy)">Imóvel C</div>
<div style="display:flex;align-items:center;gap:22px;margin-top:12px"><div style="height:56px;width:560px;background:var(--blue);border-radius:10px"></div><div style="font-size:40px;font-weight:800;color:var(--navy)">90 dias</div></div>
<div class="note">Exemplo ilustrativo</div>
</div></div>
<p class="sub" style="margin-top:44px">Quando um imóvel é reservado muito antes que o resto do portfólio, o hóspede está vendo o preço como oportunidade. Talvez dê para subir a diária.</p>
<p class="sub" style="margin-top:20px;color:var(--navy);font-weight:700">No Bookalyze, a antecedência média fica à vista.</p>
</div>""")

# 5 ─ Novidade: prestação de contas
lines = [("Receita das reservas", "R$ 12.400", False), ("Comissão da gestão (20%)", "− R$ 2.480", False),
         ("Limpezas", "− R$ 1.350", False), ("Manutenção", "− R$ 420", False), ("Ajuste manual · reembolso", "+ R$ 150", True)]
lh = "".join(f"""<div style="display:flex;justify-content:space-between;font-size:30px;padding:18px 0;border-bottom:2px solid #E3EAF1{';color:var(--blue);font-weight:700' if hl else ''}"><span>{a}</span><span style="font-weight:700">{b}</span></div>""" for a, b, hl in lines)
page(5, "light", "PRESTAÇÃO DE CONTAS", f"""
<h1>Prestação de contas <em>sem planilha.</em></h1>
<div class="stage">
<div style="background:#fff;border-radius:28px;padding:40px 48px;box-shadow:0 8px 30px rgba(42,73,106,.08)">
<div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:30px;font-weight:800;color:var(--navy)">Imóvel B · Agosto</div><div style="font-size:22px;color:#6B7F93">Exemplo ilustrativo</div></div>
<div style="margin-top:16px;color:var(--ink)">{lh}</div>
<div style="display:flex;justify-content:space-between;font-size:38px;font-weight:800;color:var(--navy);padding-top:26px"><span>Repasse ao proprietário</span><span>R$ 8.300</span></div>
</div>
<p class="sub" style="margin-top:40px">Receita e despesa por mês e por imóvel, direto do seu PMS. E, quando precisar, um ajuste manual com descrição.</p>
</div>""")

# 6 ─ Institucional: integrações
chip = lambda t: f'<div style="background:#fff;color:var(--navy);font-size:40px;font-weight:800;padding:30px 0;border-radius:24px;text-align:center;width:340px">{t}</div>'
page(6, "dark", "INTEGRAÇÃO NATIVA", f"""
<h1>Conectou, <em>analisou.</em></h1>
<p class="sub">Integração nativa com os PMS que você já usa.</p>
<div class="stage">
<div style="display:flex;align-items:center;justify-content:space-between">
<div style="display:flex;flex-direction:column;gap:28px">{chip('Stays')}{chip('Hostaway')}</div>
<svg width="170" height="120" viewBox="0 0 170 120"><path d="M10 60 H140 M110 25 L150 60 L110 95" stroke="#9CC5E4" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div style="background:rgba(255,255,255,.08);border:3px solid var(--sky);border-radius:28px;padding:34px 36px;width:330px">
<div style="display:flex;align-items:flex-end;gap:16px;height:160px">
<div style="flex:1;height:45%;background:var(--blue);border-radius:8px"></div><div style="flex:1;height:65%;background:var(--blue);border-radius:8px"></div><div style="flex:1;height:52%;background:var(--blue);border-radius:8px"></div><div style="flex:1;height:90%;background:var(--sky);border-radius:8px"></div></div>
<div style="font-size:26px;font-weight:700;color:var(--sky);margin-top:20px;text-align:center">Seu painel</div></div>
</div>
<p class="sub" style="margin-top:60px">Reservas, ocupação e receita puxadas direto do seu PMS. Sem planilha, sem esperar o fechamento do mês.</p>
</div>""")
print("ok")
