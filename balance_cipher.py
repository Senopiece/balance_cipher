from f100pb_rns import f100pb_rns as RNS
import time

# common open data
mask = tuple(1 < n < 44 for n in range(100)) # mask from f100pb to f3t44pb

# sender secret
balance1 = 454532
M1 = RNS(456773424327589256738493263542374632787842342)

# sender open data (all the calculations are performed privately)
M1s = (M1*M1).mask(mask)
cb1 = (M1*RNS(balance1)).mask(mask)
cbn1 = (M1*RNS(balance1 - 40)).mask(mask)

from math import sqrt
print(cb1.decode() / sqrt(M1s.decode())) # <- the only way to hack (works only if M1 is less than multiple of f3t44pb)

# recipient secret
balance2 = 345654
M2 = RNS(343257245492657294437562934328998262378492489)

# recipient open data (all the calculations are performed privately)
M2s = (M2*M2).mask(mask)
cb2 = (M2*RNS(balance2)).mask(mask)
cbn2 = (M2*RNS(balance2 + 40)).mask(mask)

# account registration procedure (usually comes with the first transaction)
# 1) account owner sends its value Ms
# 2) before binding this Ms with the account public address we need to check that:
# 2.1) Ms != RNS(0)
# 2.2) there is no other Ms binded with this account
# 3) finally bind the Ms with this account on the blockchain

# transaction verification procedure
# TODO: prevent underflow

# 1) M1s and M2s exists
# 2) M2s*(cb1 - cbn1)^2 == M1s*(cb2 - cbn2)^2

a = time.time()

d1 = cb1 - cbn1
d2 = cb2 - cbn2

l = M2s*d1*d1
r = M1s*d2*d2

print(f"l = {l}")
print(f"r = {r}")
print("l == r ✓" if l == r else "l != r")

b = time.time()
print("Verification time: ", b - a)

