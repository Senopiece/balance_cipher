from ars.de1m2_256 import encode as encode
from comparison_proofs import make_proof, verify_proof, fake_proof

# sender secret
balance1 = 41
#origin1 = 567
#priv_key1 = origin1*2 # TODO: use origin to make balance reverse bruteforce impossible

# sender open data (all the calculations are performed privately)
m1 = 2344
m2 = 3232
A1 = encode(m1*(balance1))
A2 = m2*(balance1 - 40)
A2proof = make_proof(2**128, A2)
A2 = encode(A2)

# recipient secret
balance2 = 34
#origin2 = 4353
#priv_key2 = origin2*2

# recipient open data (all the calculations are performed privately)
g1 = 4233
g2 = 9768
B1 = encode(g1*(balance2))
B2 = g2*(balance2 + 40)
B2proof = make_proof(2**128, B2)
B2 = encode(B2)

# verification
M = encode(2**128)
M0 = encode(0)
print("B2 < 2^128 ✓" if verify_proof(M, B2, B2proof) else "FATAL: B2 < 2^128 has an incorrect proof")
print("A2 < 2^128 ✓" if verify_proof(M, A2, A2proof) else "FATAL: A2 < 2^128 has an incorrect proof")

l = (B2*m2 + A2*g2)*m1*g1
r = (B1*m1 + A1*g1)*m2*g2
print("l == r ✓" if l == r else "FATAL: l != r")