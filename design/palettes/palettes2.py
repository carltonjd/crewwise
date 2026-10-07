# Round 2 palettes: navy + blue + safety-orange actions. Checks contrast and writes preview pages.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from palettes import cr, css, CHECKS, ROOT

BASE = dict(ground='#F8F9FD', surface='#FFFFFF', ink='#0F1B33', ink2='#44506A', ink3='#56627A', rule='#E2E6EF', rule2='#C5CCDA',
            dark='#0E1A33', dark2='#162544', dark3='#243559', darkink='#F5F7FC', darkink2='#AEB9CF',
            ok='#1F7547', okdot='#2E8B57', okdark='#6BD39A')
P = {
 '1-trust-blue': dict(BASE, accent='#F26A1B', accenthi='#F47E36', onaccent='#0F1B33', line='#1E5BD8', accentdark='#8FB3FF', wordmark='#0F1B33'),
 '2-sky-blue': dict(BASE, accent='#F26A1B', accenthi='#F47E36', onaccent='#0F1B33', line='#2878E8', accentdark='#94C0FF', wordmark='#0F1B33'),
 '3-current': dict(ground='#F8F9FD', surface='#FFFFFF', ink='#111522', ink2='#474D60', ink3='#5C6275', rule='#E2E5EE', rule2='#C6CBD9',
                   dark='#121624', dark2='#1B2032', dark3='#282E44', darkink='#F3F4F6', darkink2='#A9AEC0',
                   accent='#2E49DC', accenthi='#2540C6', onaccent='#FFFFFF', accentdark='#94A5FF', line='#2E49DC', wordmark='#F3F4F6',
                   ok='#1F7547', okdot='#2E8B57', okdark='#6BD39A'),
}
EXTRA = [('line', 'ground', 3), ('onaccent', 'accent', 4.5)]

if __name__ == '__main__':
    src = open(os.path.join(ROOT, 'public', 'index.html'), encoding='utf-8').read()
    for name, v in P.items():
        bad = [f"{a}/{b} {cr(v[a], v[b]):.2f}" for a, b, need in CHECKS + EXTRA if cr(v[a], v[b]) < need]
        print(name, 'OK' if not bad else 'FAIL ' + ', '.join(bad))
        extra = f".logo{{color:{v['line']}}}"
        if name != '3-current':
            extra += (f":root{{--closing-bg:{v['dark']};--closing-ink:{v['darkink']};--wordmark:{v['darkink']}}}"
                      f".closing .btn.light{{background:{v['accent']};border-color:{v['accent']};color:{v['onaccent']}}}"
                      f".closing .btn.light:hover{{background:{v['accenthi']}}}")
        page = src.replace('</head>', f'<style>{css(v)}{extra}</style>\n</head>', 1)
        open(os.path.join(ROOT, 'public', f'palette-{name}.html'), 'w', encoding='utf-8').write(page)
