from ars.de1m2_256 import encode as encode
from math import gcd
import random


def make_proof(a, b):
    # make a proof that Ga > Gb > 0, knowing a and b
    random.seed(a*b)
    c = random.randint(0, min(a-b-1, b-1)) # TODO: gaussian random

    # proof for a > b
    g = gcd(a+c, b+2*c)
    k1 = (b+2*c) // g
    k2 = (a+c) // g

    # proof for b > 0
    g = gcd(b+c, 2*c)
    k3 = (2*c) // g
    k4 = (b+c) // g

    return k1, k2, k3, k4, encode(c)



def fake_proof(a, b):
    proof = list(make_proof(a + 2**254, b))
    for i in range(4):
        proof[i] %= 2**254
    return proof


def verify_proof(Ga, Gb, proof):
    # verify a proof that Ga > Gb > 0
    # TODO: make sure that we cannot extract b (even knowing a) from this proof
    k1, k2, k3, k4, Gc = proof
    return \
        (Ga + Gc)*k1 == (Gb + Gc*2)*k2 and \
        (Gb + Gc)*k3 == Gc*2*k4 and \
        0 < k1 < k2 < 2**250 and \
        0 < k3 < k4 < 2**250


a = 2**128
b = 4568
print(make_proof(a, b))
print(verify_proof(encode(a), encode(b), make_proof(a, b)))
