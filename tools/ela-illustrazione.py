import math, random
random.seed(7)
W,H=1200,750; CX,CY=600,2700; RE=2150; RL=2330
def pt(th,r): return CX+r*math.sin(th), CY-r*math.cos(th)
def arc(r,a0,a1,n=80): return " ".join(f"{'M' if i==0 else 'L'}{pt(a0+(a1-a0)*i/n,r)[0]:.1f},{pt(a0+(a1-a0)*i/n,r)[1]:.1f}" for i in range(n+1))
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
'''<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#060C22"/><stop offset=".55" stop-color="#13224F"/><stop offset=".8" stop-color="#2A2F6B"/><stop offset="1" stop-color="#E0873A"/></linearGradient>
<radialGradient id="earth" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#0E1838"/><stop offset=".06" stop-color="#070D24"/><stop offset="1" stop-color="#050915"/></radialGradient>
<linearGradient id="aur" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#5FD08A" stop-opacity=".9"/><stop offset=".55" stop-color="#3FBF9A" stop-opacity=".45"/><stop offset="1" stop-color="#C04A8A" stop-opacity="0"/></linearGradient>
<radialGradient id="es" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFD08A" stop-opacity=".95"/><stop offset=".45" stop-color="#F0A23B" stop-opacity=".6"/><stop offset="1" stop-color="#C04A6B" stop-opacity="0"/></radialGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft"><feGaussianBlur stdDeviation="14"/></filter>
<filter id="blur6"><feGaussianBlur stdDeviation="6"/></filter>
</defs>''',
f'<rect width="{W}" height="{H}" fill="url(#sky)"/>']
# stars
for _ in range(260):
    x,y=random.uniform(0,W),random.uniform(0,470); r=random.choice([.6,.6,.8,1,1.3])
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" opacity="{random.uniform(.3,.9):.2f}"/>')
# aurora curtains (top left, high latitude)
for i in range(9):
    x=40+i*34+random.uniform(-8,8); h=random.uniform(150,230); w=random.uniform(26,46)
    s.append(f'<path d="M{x:.0f},{400} C{x+10:.0f},{400-h*.5:.0f} {x-12:.0f},{400-h*.8:.0f} {x+6:.0f},{400-h:.0f} L{x+w+6:.0f},{400-h+20:.0f} C{x+w-10:.0f},{400-h*.7:.0f} {x+w+12:.0f},{400-h*.4:.0f} {x+w:.0f},{400} Z" fill="url(#aur)" filter="url(#blur6)" opacity=".75"/>')
# meteor streaks (upper right)
for (x,y,l) in [(950,110,170),(1060,170,120),(880,220,90),(1130,80,140)]:
    a=math.radians(28)
    s.append(f'<line x1="{x}" y1="{y}" x2="{x-l*math.cos(a):.0f}" y2="{y+l*math.sin(a):.0f}" stroke="#DFF1FF" stroke-width="2.2" stroke-linecap="round" filter="url(#glow)" opacity=".9"/>')
# E layer band
for k,(dr,op) in enumerate([(-22,.10),(-10,.18),(0,.30),(10,.18),(22,.10)]):
    s.append(f'<path d="{arc(RL+dr,-0.38,0.38)}" fill="none" stroke="#7FB8FF" stroke-width="12" opacity="{op}"/>')
s.append(f'<path d="{arc(RL,-0.38,0.38)}" fill="none" stroke="#BFE3FF" stroke-width="1.2" opacity=".7" filter="url(#glow)"/>')
# FAI irregularities: small field-aligned striations right side
for i in range(14):
    th=0.16+i*0.006; x,y=pt(th,RL-14); x2,y2=pt(th+0.004,RL+16)
    s.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#9FD6FF" stroke-width="2" opacity=".7"/>')
# Es clouds
for th,sc in [(-0.11,1.0),(0.11,.85)]:
    x,y=pt(th,RL)
    s.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{95*sc:.0f}" ry="{26*sc:.0f}" fill="url(#es)" transform="rotate({math.degrees(th):.1f} {x:.0f} {y:.0f})" filter="url(#blur6)"/>')
# earth
s.append(f'<circle cx="{CX}" cy="{CY}" r="{RE}" fill="url(#earth)"/>')
s.append(f'<path d="{arc(RE+3,-0.45,0.45)}" fill="none" stroke="#6FB6FF" stroke-width="3" opacity=".8" filter="url(#glow)"/>')
s.append(f'<path d="{arc(RE+14,-0.45,0.45)}" fill="none" stroke="#F0A23B" stroke-width="22" opacity=".35" filter="url(#soft)"/>')
# city lights
for _ in range(420):
    th=random.uniform(-0.42,0.42); d=abs(random.gauss(0,40))+6
    x,y=pt(th,RE-d)
    if y<H: s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.choice([.7,.9,1.2])}" fill="#FFC870" opacity="{random.uniform(.35,.95):.2f}"/>')
# ray paths: two-hop Es
A,M1,B,M2,C=pt(-0.22,RE),pt(-0.11,RL-8),pt(0,RE),pt(0.11,RL-8),pt(0.22,RE)
ray=f"M{A[0]:.0f},{A[1]:.0f} L{M1[0]:.0f},{M1[1]:.0f} L{B[0]:.0f},{B[1]:.0f} L{M2[0]:.0f},{M2[1]:.0f} L{C[0]:.0f},{C[1]:.0f}"
s.append(f'<path d="{ray}" fill="none" stroke="#5FD08A" stroke-width="9" opacity=".25" filter="url(#soft)"/>')
s.append(f'<path d="{ray}" fill="none" stroke="#8CF0B0" stroke-width="2.4" stroke-linejoin="round" filter="url(#glow)"/>')
# fan of weaker rays from A
for d in (-0.02,0.02,0.04):
    m=pt(-0.11+d,RL-8)
    s.append(f'<path d="M{A[0]:.0f},{A[1]:.0f} L{m[0]:.0f},{m[1]:.0f}" stroke="#5FD08A" stroke-width="1" opacity=".45"/>')
# meteor scatter path B -> trail -> right
T=(880,268)
s.append(f'<path d="M{B[0]:.0f},{B[1]:.0f} L{T[0]},{T[1]} L{C[0]+60:.0f},{C[1]+8:.0f}" fill="none" stroke="#BFE3FF" stroke-width="1.3" stroke-dasharray="6 6" opacity=".7"/>')
# towers
def tower(x,y,th):
    rot=math.degrees(th)
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f})" stroke="#AFC6EE" fill="none" stroke-width="2">'
            '<path d="M-9,0 L0,-46 L9,0 M-6,-14 L6,-14 M-4,-28 L4,-28 M0,-46 L0,-58 M-14,-52 L14,-52 M-10,-56 L10,-56"/></g>'
            f'<g transform="translate({x:.1f},{y:.1f}) rotate({rot:.1f})"><circle cx="0" cy="-58" r="3" fill="#F0A23B" filter="url(#glow)"/></g>')
for th in (-0.22,0,0.22):
    x,y=pt(th,RE); s.append(tower(x,y,th))
s.append('</svg>')
open("ela.svg","w").write("\n".join(s))
