"""WCAG contrast audit for the Da Green palette."""
def lin(c):
    c/=255
    return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
def L(hexs):
    r=int(hexs[1:3],16);g=int(hexs[3:5],16);b=int(hexs[5:7],16)
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def ratio(fg,bg):
    a,b=L(fg)+0.05,L(bg)+0.05
    return round(max(a,b)/min(a,b),2)

C=dict(bg="#F2F0E6",surface="#E5E8DA",primary="#1F3D2B",canopy="#16301F",
       accent="#CB5E3C",accent_ink="#A1431F",text="#22261E",muted="#4E5340",
       cream="#F2F0E6",cream_dim="#D9D9C7")

pairs=[
 ("body text / bg","text","bg",4.5),
 ("body text / surface","text","surface",4.5),
 ("muted / bg","muted","bg",4.5),
 ("muted / surface","muted","surface",4.5),
 ("heading primary / bg","primary","bg",4.5),
 ("heading primary / surface","primary","surface",4.5),
 ("label accent_ink / bg","accent_ink","bg",4.5),
 ("label accent_ink / surface","accent_ink","surface",4.5),
 ("cream / canopy","cream","canopy",4.5),
 ("cream_dim / canopy","cream_dim","canopy",4.5),
 ("cream / primary (btn)","cream","primary",4.5),
 ("hero em accent / canopy (LARGE)","accent","canopy",3.0),
 ("--- problem checks ---","text","bg",0),
 ("accent SMALL / canopy","accent","canopy",4.5),
 ("accent SMALL / primary","accent","primary",4.5),
 ("cream / accent (chip)","cream","accent",4.5),
 ("cream / accent_ink (chip fix)","cream","accent_ink",4.5),
]
for name,fg,bg,need in pairs:
    if need==0: print(f"\n{name}");continue
    r=ratio(C[fg],C[bg]); ok="PASS" if r>=need else "**FAIL**"
    print(f"  {r:>5}:1  need {need}  {ok}  {name}")

# search a light-coral "bloom" that passes >=4.5 small text on canopy AND primary
print("\nbloom candidates (need >=4.5 on canopy & primary):")
for hexs in ["#E59A78","#E8A081","#EBA98C","#EDB196","#E0926E","#E39C7C","#EAA98D"]:
    rc=ratio(hexs,C["canopy"]); rp=ratio(hexs,C["primary"])
    print(f"  {hexs}  canopy {rc}  primary {rp}  {'OK both' if rc>=4.5 and rp>=4.5 else ('OK canopy' if rc>=4.5 else 'no')}")
