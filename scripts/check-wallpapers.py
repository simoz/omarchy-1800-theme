"""Verify accepted wallpaper dimensions, checksums and manifest (requires Pillow)."""
import hashlib,json
from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
items=json.loads((root/'docs/backgrounds.json').read_text())
assert len(items)==12
for item in items:
 p=root/item['file']
 assert p.exists(),f'Missing wallpaper: {p.name}'
 with Image.open(p) as im:
  assert im.size==(3840,2160),(p.name,im.size)
  assert im.format=='PNG',(p.name,im.format)
 assert item['sha256']==hashlib.sha256(p.read_bytes()).hexdigest(),p.name
 assert (root/item['prompt']).exists(),item['prompt']
 assert (root/item['reference']).exists(),item['reference']
assert {item['file'] for item in items}=={str(p.relative_to(root)) for p in (root/'backgrounds').glob('*.png')}
print('12 native 4K PNGs, checksums, approved references and prompt files verified.')
