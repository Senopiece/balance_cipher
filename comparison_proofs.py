from ars.de1m2_256 import encode as encode
from math import lcm
import random


def make_proof(a, b):
    # make a proof that Ga > Gb, knowing a and b
    random.seed(a*b)
    c = random.randint(0, abs(a-b)-1)
    l = lcm(a+c, b+2*c)
    k1 = l // (a+c)
    k2 = l // (b+2*c)
    #assert k2 < 2**160, "Numbers are too long"
    #assert 0 < k1 < k2, "May occur if you use negative numbers"
    if k2-k1 == a-b:
        print(f"WARNING: too week proof for {a} > {b}")
    return k1, k2, encode(c)



def fake_proof(a, b):
    # works sometimes, but with k2 < 2**160 chances of creating a fake proof became insufficient
    return make_proof(2**254-a, b)


def verify_proof(Ga, Gb, proof):
    # verify a proof that Ga > Gb
    # TODO: make sure that we cannot extract b (even knowing a) from this proof
    k1, k2, Gc = proof
    return (Ga + Gc)*k1 == (Gb + Gc*2)*k2 and 0 < k1 < k2 < 2**160


# a = 2**128
# b = 5345
# c = 0
# print(make_proof(a, b))
# print(make_proof(b, c))
# print(verify_proof(encode(b), encode(c), make_proof(b, c)))
# print(verify_proof(encode(a), encode(b), make_proof(a, b)))
