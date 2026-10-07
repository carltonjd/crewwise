# Three candidate palettes, each derived from the roofing world. Run to check contrast and write previews.
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

P = {
 'a-jobsite': dict(  # Jobsite: blueprint navy and hi-vis safety yellow, like a site sign and a hard hat
  ground='#F2F4F7', surface='#FFFFFF', ink='#0E1A2B', ink2='#44516A', ink3='#56637B', rule='#D8DEE7', rule2='#B4BFCE',
  dark='#0D1F3C', dark2='#152A4B', dark3='#24395D', darkink='#F2F4F7', darkink2='#AAB6CB',
  accent='#FFC21A', accenthi='#FFCD45', onaccent='#0E1A2B', accentdark='#FFC21A', line='#1E4FD8', wordmark='#0E1A2B',
  ok='#1D7044', okdot='#2E8B57', okdark='#6BD39A'),
 'b-evergreen': dict(  # Evergreen and copper: a contractor's truck door, copper flashing, cream primer
  ground='#F4F1E8', surface='#FFFDF8', ink='#16241E', ink2='#48544E', ink3='#5D6862', rule='#DCD5C5', rule2='#C2B9A5',
  dark='#1B3329', dark2='#233F33', dark3='#2F4F41', darkink='#F4F1E8', darkink2='#B4C2B9',
  accent='#A9501E', accenthi='#954418', onaccent='#FFFFFF', accentdark='#EE9A62', line='#A9501E', wordmark='#F4F1E8',
  ok='#23794A', okdot='#2E8B57', okdark='#7FD6A0'),
 'c-slate-cobalt': dict(  # Slate roof and cobalt: cool slate tiles at dusk, one strong blue for action
  ground='#F3F4F6', surface='#FFFFFF', ink='#111522', ink2='#474D60', ink3='#5C6275', rule='#DCDFE6', rule2='#BFC4CF',
  dark='#121624', dark2='#1B2032', dark3='#282E44', darkink='#F3F4F6', darkink2='#A9AEC0',
  accent='#2E49DC', accenthi='#2540C6', onaccent='#FFFFFF', accentdark='#94A5FF', line='#2E49DC', wordmark='#F3F4F6',
  ok='#1F7547', okdot='#2E8B57', okdark='#6BD39A'),
}

def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def cr(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + .05) / (lb + .05)

CHECKS = [('ink', 'ground', 4.5), ('ink2', 'ground', 4.5), ('ink3', 'ground', 4.5), ('ink3', 'surface', 4.5),
          ('darkink', 'dark', 4.5), ('darkink2', 'dark', 4.5), ('darkink2', 'dark2', 4.5),
          ('onaccent', 'accent', 4.5), ('onaccent', 'accenthi', 4.5), ('accentdark', 'dark', 4.5), ('accentdark', 'dark2', 4.5),
          ('ok', 'ground', 4.5), ('ok', 'surface', 4.5), ('okdark', 'dark', 4.5), ('okdark', 'dark2', 4.5),
          ('line', 'ground', 3), ('line', 'surface', 3), ('rule2', 'ground', 1.4)]

def css(v):
    return (f":root{{--ground:{v['ground']};--surface:{v['surface']};--ink:{v['ink']};--ink-2:{v['ink2']};--ink-3:{v['ink3']};"
            f"--rule:{v['rule']};--rule-2:{v['rule2']};--dark:{v['dark']};--dark-2:{v['dark2']};--dark-3:{v['dark3']};"
            f"--dark-ink:{v['darkink']};--dark-ink-2:{v['darkink2']};--accent:{v['accent']};--accent-hi:{v['accenthi']};"
            f"--on-accent:{v['onaccent']};--accent-on-dark:{v['accentdark']};--line:{v['line']};--wordmark:{v['wordmark']};"
            f"--ok:{v['ok']};--ok-dot:{v['okdot']};--ok-on-dark:{v['okdark']};}}")

if __name__ == '__main__':
    src = open(os.path.join(ROOT, 'public', 'index.html'), encoding='utf-8').read()
    for name, v in P.items():
        bad = [f"{a}/{b} {cr(v[a], v[b]):.2f}" for a, b, need in CHECKS if cr(v[a], v[b]) < need]
        print(name, 'OK' if not bad else 'FAIL ' + ', '.join(bad))
        page = src.replace('</head>', f'<style>{css(v)}</style>\n</head>', 1)
        open(os.path.join(ROOT, 'public', f'palette-{name}.html'), 'w', encoding='utf-8').write(page)
