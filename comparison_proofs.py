from ars.de1m2_256 import encode as encode
import random


def bettavariate_randint(start, stop):
    assert stop > start
    return int(random.betavariate(2, 2)*(stop - start) + start)


def make_proof(a, b, c):
    # make a proof that Ga > Gb > Gc
    assert a > b > c >= 0

    random.seed(a*2**508 + b*2**254 + c)
    d = bettavariate_randint(
        start = max((-c//3)+1, (-b//2)+1),
        stop = min(a-b, b-c)
    )

    return a+1*d, b+2*d, c+3*d


def verify_proof(Ga, Gb, Gc, proof):
    # verify a proof that Ga > Gb > Gc
    # NOTE: this proof is persistent until we dont know all the values a, b, c and d
    k1, k2, k3 = proof
    Gd = encode(k1) - Ga
    return \
        (Ga + Gd)*k2 == (Gb + Gd*2)*k1 and \
        (Gb + Gd*2)*k3 == (Gc + Gd*3)*k2 and \
        k1 > k2 > k3


a = 345435454356234234
b = 345435454
c = 561324
print(make_proof(a, b, c))
print(verify_proof(encode(a), encode(b), encode(c), make_proof(a, b, c)))
