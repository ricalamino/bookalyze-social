# Template das artes

- 1080x1350 PNG, fonte Red Hat Display (woff2 aqui), logos `logo_color.png` (fundo claro) e `logo_white.png` (fundo escuro).
- `exemplo_lote1.py` gera os HTMLs do lote 1: copie a função `page()` e o CSS `BASE` para novos posts.
- `render.js` (Playwright): renderiza `posts/postN.html` → `posts/postN.png`. Rode com `NODE_PATH=$(npm root -g) node render.js` a partir da pasta que contém `posts/`.
