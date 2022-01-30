from ars.de1m2_256 import encode as encode
from math import lcm
import random


def make_proof(a, b):
    # make a proof that Ga > Gb > 0, knowing a and b
    random.seed(a*b)
    c = random.randint(1, min(a-b-1, b-1)) # TODO: gaussian random

    # proof for a > b
    l = lcm(a+c, b+2*c)
    k1 = l // (a+c)
    k2 = l // (b+2*c)
    #assert k2 < 2**160, "Numbers are too long"
    #assert 0 < k1 < k2, "May occur if you use negative numbers"
    if k2-k1 == a-b:
        print(f"WARNING: too week proof for {a} > {b}")

    # proof for b > 0
    l = lcm(b+c, 2*c)
    k3 = l // (b+c)
    k4 = l // (2*c)

    return k1, k2, k3, k4, encode(c)



def fake_proof(a, b):
    assert a > b # the actual make_proof is working with assert a > b > 0, this fake tries to down zero
    while True:
        a += 2**254
        b += 2**254
        r = make_proof(a, b)
        if verify_proof(encode(a), encode(b), r):
            return r


def verify_proof(Ga, Gb, proof):
    # verify a proof that Ga > Gb > 0
    # TODO: make sure that we cannot extract b (even knowing a) from this proof
    k1, k2, k3, k4, Gc = proof
    return \
        (Ga + Gc)*k1 == (Gb + Gc*2)*k2 and \
        (Gb + Gc)*k3 == Gc*2*k4 and \
        0 < k1 < k2 < 2**160 and \
        0 < k3 < k4 < 2**160


# a = 2**128
# b = 5345
# c = 0
# print(make_proof(a, b))
# print(make_proof(b, c))
# print(verify_proof(encode(b), encode(c), make_proof(b, c)))
# print(verify_proof(encode(a), encode(b), make_proof(a, b)))
