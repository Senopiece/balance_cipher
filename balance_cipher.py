from ars.de1m2_256 import encode as encode
from comparison_proofs import make_proof, verify_proof

# ====================================================== #
#               S E N D E R  S E C T I O N               #
# ====================================================== #
# sender secret
balance1 = 41

# already known sender open data
m1 = 2344 # open constant
A1 = encode(m1*balance1)

# sender open data (all the calculations are performed privately)
m2 = 3232 # open constant
A2 = balance1 - 40
A2proof = make_proof(2**253, m2*A2, 0)
A2 = encode(m2*A2)

# ====================================================== #
#            R E C I P I E N T  S E C T I O N            #
# ====================================================== #
# recipient secret
balance2 = 34

# already known recipient open data
g1 = 4233 # open constant
B1 = encode(g1*balance2)

# recipient open data (all the calculations performed privately)
g2 = 9768 # open constant
B2 = balance2 + 40
B2proof = make_proof(2**253, g2*B2, 0)
B2 = encode(g2*B2)

# ====================================================== #
#                 V E R I F I C A T I O N                #
# ====================================================== #
M = encode(2**253)
M0 = encode(0)

print("A2 is proven positive ✓" if \
    verify_proof(M, A2, M0, A2proof) \
    else "FATAL: A2 positiveness proof failed")

print("B2 is proven positive ✓" if \
    verify_proof(M, B2, M0, B2proof) \
    else "FATAL: B2 positiveness proof failed")

if (B2*m2 + A2*g2)*m1*g1 == (B1*m1 + A1*g1)*m2*g2:
    print("given == received ✓")
else:
    print("FATAL: given != received")