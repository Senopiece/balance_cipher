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
        start = max(-c//3, -b//2),
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


def make_proof2(a, b, c):
    # make a proof that Ga > Gb > Gc, considering a case when proof verificator know a
    assert a > b > c >= 0

    random.seed(a*2**508 + b*2**254 + c)
    d = bettavariate_randint(
        start = max(-c//3, -b//2),
        stop = min(a-b, b-c)
    )

    return b + d, c + 2*d


def verify_proof2(a, Gb, Gc, proof):
    # verify a proof that Ga > Gb > Gc
    # NOTE: this proof is persistent until we dont know b, c and d
    k1, k2 = proof
    Ga = encode(a)
    Gd = encode(k1) - Gb
    return \
        Ga*k1 == (Gb + Gd)*a and \
        (Gb + Gd)*k2 == (Gc + Gd*2)*k1 and \
        a > k1 > k2


a = 999999999999999234
b = 3454999999999998
c = 56234234
print(make_proof2(a, b, c))
print(verify_proof2(a, encode(b), encode(c), make_proof2(a, b, c)))
