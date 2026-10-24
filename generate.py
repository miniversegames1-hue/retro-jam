"""Build the public Retro Jam support site. No game assets or source are included."""
from pathlib import Path
from html import escape
import json
root=Path(__file__).parent
languages={'en':'English','tr':'Türkçe','de':'Deutsch','es':'Español','fr':'Français','it':'Italiano','ja':'日本語','ko':'한국어','pt-BR':'Português (Brasil)'}
# Each localized page describes the same current product behavior.
data=json.loads((root/'content.json').read_text())
base='https://miniversegames1-hue.github.io/retro-jam'
def write_page(kind,lang):
 row=data[lang]; title=row[0 if kind=='privacy' else 1]; paras=row[2:8] if kind=='privacy' else row[8:]
 nav=''.join(f'<a lang="{code}" hreflang="{code}" href="{base}/{kind}/{code}/"'+(' aria-current="page"' if code==lang else '')+'>'+name+'</a>' for code,name in languages.items())
 body=''.join('<p>'+escape(p).replace('miniverse.games1@gmail.com','<a href="mailto:miniverse.games1@gmail.com">miniverse.games1@gmail.com</a>')+'</p>' for p in paras)
 page=f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Retro Jam · {title}</title><link rel="stylesheet" href="../../style.css"><link rel="canonical" href="{base}/{kind}/{lang}/"></head><body><main><a class="brand" href="{base}/">RETRO <b>JAM</b></a><nav aria-label="Languages">{nav}</nav><nav><a href="{base}/privacy/{lang}/">{row[0]}</a><a href="{base}/support/{lang}/">{row[1]}</a></nav><h1>{title}</h1>{body}<footer><a href="https://www.apple.com/legal/privacy/">Apple Privacy Policy</a> · <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a><p>© 2026 Semih Gülücü · Miniverse Games</p></footer></main></body></html>'
 dest=root/kind/lang;dest.mkdir(parents=True,exist_ok=True);(dest/'index.html').write_text(page)
for lang in languages:
 assert len(data[lang])==11
 for kind in ['privacy','support']:write_page(kind,lang)
links=''.join(f'<li><strong>{name}</strong> — <a href="privacy/{lang}/">{data[lang][0]}</a> · <a href="support/{lang}/">{data[lang][1]}</a></li>' for lang,name in languages.items())
(root/'index.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Retro Jam · Privacy & Support</title><link rel="stylesheet" href="style.css"></head><body><main><h1 class="brand">RETRO <b>JAM</b></h1><p>Miniverse Games · Privacy & Support</p><ul>{links}</ul></main></body></html>')
(root/'style.css').write_text('body{margin:0;background:#070b20;color:#e3eafa;font:17px/1.7 system-ui,sans-serif}main{max-width:850px;margin:auto;padding:40px 24px}a{color:#20e5eb;overflow-wrap:anywhere}nav{display:flex;flex-wrap:wrap;gap:12px;margin:24px 0}nav a{padding:5px 10px;border:1px solid #254574;border-radius:6px;text-decoration:none}a[aria-current]{background:#20e5eb;color:#070b20}.brand{font-size:34px;font-weight:900;color:#20e5eb;text-decoration:none}.brand b{color:#ff2998}h1{line-height:1.2}li{margin:14px 0}footer{margin-top:40px;padding-top:20px;border-top:1px solid #254574;font-size:14px}p{overflow-wrap:anywhere}@media(max-width:400px){main{padding:25px 16px}nav{gap:6px}.brand{font-size:28px}}')
(root/'.nojekyll').touch()
print('Generated18localizedpages +index')
