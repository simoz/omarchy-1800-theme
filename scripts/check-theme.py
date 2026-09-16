"""Validate shipped theme colors and opaque text contrast (Python 3.11+)."""
from pathlib import Path
import tomllib,json
root=Path(__file__).resolve().parents[1]
c=tomllib.loads((root/'colors.toml').read_text());shell=tomllib.loads((root/'shell.toml').read_text())
def rgb(h):return [int(h[i:i+2],16)/255 for i in (1,3,5)]
def lum(h):
 a=[v/12.92 if v<=0.04045 else ((v+0.055)/1.055)**2.4 for v in rgb(h)]
 return sum(v*w for v,w in zip(a,[.2126,.7152,.0722]))
def contrast(a,b):
 x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)
checks={}
for fg in ['foreground','muted','dark_foreground','light_foreground','bright_foreground','accent','red','yellow','orange','green','cyan','blue','magenta','brown','bright_red','bright_yellow','bright_green','bright_cyan','bright_blue','bright_magenta']:
 for bg in ['background','lighter_background']:
  checks[f'{fg} on {bg}']=contrast(c[fg],c[bg])
checks['foreground on selection']=contrast(c['foreground'],c['selection'])
for name,v in shell.items():
 if 'background' in v:
  assert v['background-alpha']==1.0,(name,'not opaque')
  for fg in ['text','placeholder','text-error']:
   if fg in v:checks[f'{name}.{fg}']=contrast(v[fg],v['background'])
 if 'selected-background' in v:checks[f'{name}.selected-text']=contrast(v['selected-text'],v['selected-background'])
# Strongest interactive white overlay is 10%; test the resulting surface.
a=rgb(c['foreground']);b=rgb(c['lighter_background']);blend='#'+''.join(f'{round(255*(.1*x+.9*y)):02x}' for x,y in zip(a,b))
checks['foreground on pressed control']=contrast(c['foreground'],blend)
failed={k:v for k,v in checks.items() if v<4.5}
report={'threshold':4.5,'minimum':round(min(checks.values()),2),'checks':{k:round(v,2) for k,v in checks.items()},'failures':failed,'scope':'Shipped opaque text/surface pairs; excludes application overrides, transparency and untested live rendering.'}
(root/'docs/contrast.json').write_text(json.dumps(report,indent=2)+'\n')
assert not failed,failed
print(f'{len(checks)} contrast checks pass; minimum {min(checks.values()):.2f}:1.')
print(f'Primary: {contrast(c["foreground"],c["background"]):.2f}:1; selected: {contrast(c["foreground"],c["selection"]):.2f}:1; muted on surface: {contrast(c["muted"],c["lighter_background"]):.2f}:1')
