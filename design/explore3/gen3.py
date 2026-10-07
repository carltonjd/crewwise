import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'hero.html'), encoding='utf-8').read()

OLD_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500..700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
OLD_MARK = '<rect width="44" height="44" rx="10" fill="#13233A"/><polyline points="10,21 22,11 34,21" fill="none" stroke="#F06A35" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><polyline points="15,26 20,31 30,21" fill="none" stroke="#FFFFFF"'
assert OLD_FONTS in src and OLD_MARK in src

V = {
 'v1-galvanized': dict(
   fonts='family=Schibsted+Grotesk:wght@400..800',
   scheme='light', display='"Schibsted Grotesk"', body='"Schibsted Grotesk"', dw=700, track='-.045em',
   mark=('#14181C', '#C0632F', '#FFFFFF'),
   tokens='--ground:#F2F3F4;--ink:#14181C;--ink-2:#47505A;--ink-3:#5F6973;--rule:#DCE0E4;--rule-2:#BFC6CD;--accent:#B0522A;--accent-ink:#9C4722;--ok:#23794A;--cta:#14181C;--cta-hover:#2A3036;--cta-ink:#FFFFFF;'),
 'v2-slate': dict(
   fonts='family=Bricolage+Grotesque:opsz,wght@12..96,400..800',
   scheme='dark', display='"Bricolage Grotesque"', body='"Bricolage Grotesque"', dw=650, track='-.04em',
   mark=('#EEF0EE', '#FF5A36', '#121619'),
   tokens='color-scheme:dark;--ground:#121619;--ink:#EEF0EE;--ink-2:#A9B1B6;--ink-3:#8D969C;--rule:#262D32;--rule-2:#3B444B;--accent:#FF5A36;--accent-ink:#FF7A5C;--ok:#5ACF8E;--cta:#FF5A36;--cta-hover:#FF6E4E;--cta-ink:#121619;'),
 'v3-editorial': dict(
   fonts='family=Gloock&family=Hanken+Grotesk:wght@400..700',
   scheme='light', display='"Gloock"', body='"Hanken Grotesk"', dw=400, track='-.02em',
   mark=('#101010', '#C1272D', '#FFFFFF'),
   tokens='--ground:#FFFFFF;--ink:#101010;--ink-2:#4A4A4A;--ink-3:#666666;--rule:#E7E7E7;--rule-2:#CCCCCC;--accent:#B3261E;--accent-ink:#A3221B;--ok:#1E7546;--cta:#101010;--cta-hover:#2B2B2B;--cta-ink:#FFFFFF;'),
}

for name, v in V.items():
    s = src.replace(OLD_FONTS, f'<link href="https://fonts.googleapis.com/css2?{v["fonts"]}&display=swap" rel="stylesheet">')
    r, a, c = v['mark']
    s = s.replace(OLD_MARK, f'<rect width="44" height="44" rx="10" fill="{r}"/><polyline points="10,21 22,11 34,21" fill="none" stroke="{a}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><polyline points="15,26 20,31 30,21" fill="none" stroke="{c}"')
    override = (f'<style>:root{{color-scheme:{v["scheme"]};--display:{v["display"]}, "Helvetica Neue", Arial, sans-serif;--body:{v["body"]}, system-ui, "Segoe UI", Roboto, Arial, sans-serif;{v["tokens"]}}}'
                f' h1{{font-weight:{v["dw"]};letter-spacing:{v["track"]};}} .next h2{{font-weight:{v["dw"]};}} .logo{{font-weight:{max(500, min(700, v["dw"]))};}}'
                + (' h1{font-size:clamp(2.9rem,6.4vw,6rem);line-height:1.02;}' if 'Gloock' in v['display'] else '')
                + (' h1{font-variation-settings:"opsz" 96;}' if 'Bricolage' in v['display'] else '')
                + '</style>\n</head>')
    s = s.replace('</head>', override, 1)
    open(os.path.join(HERE, name + '.html'), 'w', encoding='utf-8').write(s)
    print('wrote', name)
