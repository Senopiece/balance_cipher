from f3t44pb_rns import f3t44pb_rns as RNS

# sender secret
balance1 = 454532
secret1 = 45677

# sender open data (all the calculations are performed privately)
M1 = RNS(secret1)
cb1 = M1*RNS(balance1)
cbn1 = M1*RNS(balance1 - 40)

# recipient secret
balance2 = 345654
secret2 = 34325

# recipient open data (all the calculations are performed privately)
M2 = RNS(secret2)
cb2 = M2*RNS(balance2)
cbn2 = M2*RNS(balance2 + 40)

# account registration procedure (usually comes with the first transaction)
# 1) account owner sends its value M
# 2) before binding this M with the account public address we need to check that:
# 2.1) M != RNS(0)
# 2.2) there is no other M binded with this account
# 3) that M binds with this account public address on the blockchain

# transaction verification procedure
# TODO: prevent underflow

# 1) M1 and M2 exists
# 2) there is no underflow
# 3) (M2*cb1 + M1*cb2) == (M2*cbn1 + M1*cbn2)

print((M2*cb1 + M1*cb2) == (M2*cbn1 + M1*cbn2))
print(M2*cb1 + M1*cb2)
print(M2*cbn1 + M1*cbn2)
