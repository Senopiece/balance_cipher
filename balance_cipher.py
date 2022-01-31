from ars.de1m2_256 import encode as encode
from comparison_proofs import make_proof, verify_proof

# I realized that origins does not prevent from bruteforce
# balance restore, so plz TODO

# ----------------------------------------------------------------- #
#                     S E N D E R  S E C R E T                      #
# ----------------------------------------------------------------- #
balance1 = 41
# (when the account was initiated, this value was given
# in encrypted form: encode(m0*origin)
# and proven that it's < 2**100)
origin1 = 1267650600228227059142349752145 # 100 bits


# ----------------------------------------------------------------- #
#                   S E N D E R  O P E N  D A T A                   #
# ----------------------------------------------------------------- #
#                           already known                           #
# ----------------------------------------------------------------- #
m0 = 7225 # open constant
m1 = 2344 # open constant
AO = encode(m0*origin1)
A1 = encode(m1*(balance1 + origin1))


# ----------------------------------------------------------------- #
#                   S E N D E R  O P E N  D A T A                   #
# ----------------------------------------------------------------- #
#          all the calculations are performed privately             #
# ----------------------------------------------------------------- #
m2 = 3232 # open constant
A2 = balance1 + origin1 - 40
A2proof = make_proof(2**253, m0*m2*A2, m2*m0*origin1)
A2 = encode(m2*A2)


# ----------------------------------------------------------------- #
#                R E C I P I E N T  S E C R E T                     #
# ----------------------------------------------------------------- #
balance2 = 34
# (when the account was initiated, this value was given
# in encrypted form: encode(m0*origin)
# and proven that it's < 2**100)
origin2 = 1165650600228105977238812769943 # 100 bits


# ----------------------------------------------------------------- #
#               R E C I P I E N T  O P E N  D A T A                 #
# ----------------------------------------------------------------- #
#                          already known                            #
# ----------------------------------------------------------------- #
g0 = 6542 # open constant
g1 = 4233 # open constant
BO = encode(g0*origin2)
B1 = encode(g1*(balance2 + origin2))


# ----------------------------------------------------------------- #
#               R E C I P I E N T  O P E N  D A T A                 #
# ----------------------------------------------------------------- #
#          all the calculations are performed privately             #
# ----------------------------------------------------------------- #
g2 = 9768 # open constant
B2 = balance2 + origin2 + 40
B2proof = make_proof(2**253, g0*g2*B2, g2*g0*origin2)
B2 = encode(g2*B2)


# ----------------------------------------------------------------- #
#                      V E R I F I C A T I O N                      #
# ----------------------------------------------------------------- #
M = encode(2**253)

print("A2 is proven positive ✓" if \
    verify_proof(M, A2*m0, AO*m2, A2proof) \
    else "FATAL: A2 positiveness proof failed")

print("B2 is proven positive ✓" if \
    verify_proof(M, B2*g0, BO*g2, B2proof) \
    else "FATAL: B2 positiveness proof failed")

if (B2*m2 + A2*g2)*m1*g1 == (B1*m1 + A1*g1)*m2*g2:
    print("given == received ✓")
else:
    print("FATAL: given != received")