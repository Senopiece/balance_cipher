from ars.de1m2_256 import encode as encode
from math import gcd
import random


def bettavariate_randint(start, stop):
    assert stop > start
    return int(random.betavariate(2, 2)*(stop - start) + start)


def make_proof(a, b, c):
    # make a proof that Ga > Gb > Gc
    assert a > b > c >= 0

    random.seed(a*2**508 + b*2**254 + c)
    d = bettavariate_randint(
        start = max(-c//2, -b//2),
        stop = min(a-b, b-c)
    )

    # proof for a > b
    g = gcd(a+d, b+2*d)
    k1 = (b+2*d) // g
    k2 = (a+d) // g

    # proof for b > 0
    g = gcd(b+d, c+2*d)
    k3 = (c+2*d) // g
    k4 = (b+d) // g

    return k1, k2, k3, k4, encode(d)


def verify_proof(Ga, Gb, Gc, proof):
    # verify a proof that Ga > Gb > Gc
    # TODO: make sure that we cannot extract b (even knowing a and c) from this proof
    k1, k2, k3, k4, Gd = proof
    return \
        (Ga + Gd)*k1 == (Gb + Gd*2)*k2 and \
        (Gb + Gd)*k3 == (Gc + Gd*2)*k4 and \
        k1 < k2 and k3 < k4


a = 345435454356
b = 34543545435
c = 56
print(make_proof(a, b, c))
print(verify_proof(encode(a), encode(b), encode(c), make_proof(a, b, c)))
