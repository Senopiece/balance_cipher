from ars.de1m256 import encode 

# sender secret
balance1 = 60

# sender open data (all the calculations are performed privately)
# TODO: m*b % 2**254 is having unique solution for b only if m is odd, is it good or bad?
m1 = 61831996350531240199057085283232358026495125261252625916218455899905125740353
m2 = 77347096829997860251145238741378512327304242939718028116032409255917948845697
A1 = encode(m1*balance1)
A2 = encode(m2*(balance1 - 40))

# recipient secret
balance2 = 3456

# recipient open data (all the calculations are performed privately)
g1 = 42334496918515581520281029467747373373690656937939313516048188657552755383937
g2 = 97680493710316016549179486752524137080160327319815402918319565371107429039937
B1 = encode(g1*balance2)
B2 = encode(g2*(balance2 + 40))

# verification
# TODO: underflow detection
l = (B2*m2 + A2*g2)*m1*g1
r = (B1*m1 + A1*g1)*m2*g2

print(f"l = {l}")
print(f"r = {r}")
print("l == r ✓" if l == r else "l != r")