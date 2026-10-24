from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json
root=Path(__file__).parent
languages=set(json.loads((root/'content.json').read_text()))
assert languages=={'en','tr','de','es','fr','it','ja','ko','pt-BR'}
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.lang=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='a':self.links.append(a.get('href',''))
for lang in languages:
 for kind in ['privacy','support']:
  p=root/kind/lang/'index.html';s=p.read_text();parser=Links();parser.feed(s)
  assert parser.lang==lang
  assert 'mailto:miniverse.games1@gmail.com' in parser.links
  assert '<script' not in s and '<form' not in s and 'TODO' not in s
  for href in parser.links:
   if href.startswith('https://miniversegames1-hue.github.io/retro-jam/'):
    local=href.split('/retro-jam/',1)[1]
    assert (root/local/'index.html').is_file(),href
print('18pages: nine languages, internal links, email and tracking-free markup verified')
