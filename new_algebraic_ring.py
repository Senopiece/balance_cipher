# future ResidueSequence

from sympy import prime
basis = [prime(n) for n in range(1, 20)]

accmul = 1
for e in basis:
    accmul *= e


def decompose(a):
    v = []
    for e in basis:
        v.append(a % e)
        a //= e
    return v


def compose(v):
    res = 0
    m = 1
    for e in basis:
        res += (next(v) % e) * m
        m *= e
    return res


def add_one(a):
    # where a is a ring element
    # equivalent to add(a, add_one(1)) = add_one(a)
    # add(a, add_one(add_one(1))) = add_one(add_one(a))
    # add(a, atomic_add(1, 2)) = add_one(add_one(a)) = atomic_add(a, 2)
    # add(atomic_add(1, a), atomic_add(1, 2)) = atomic_add(1, a+2)
    res = 0
    m = 1
    for e in basis:
        res += (a % e) * m
        m *= e
    return res


def add(a, b):
    # where a and b both are ring elements
    a = decompose(a)
    b = decompose(b)

    res = 0
    m = 1
    for i, e in enumerate(basis):
        res += ((a[i] + b[i]) % e) * m
        m *= e
    
    return res


def sub_one(a):
    from sympy.ntheory.modular import crt
    return crt(basis, decompose(a))[0]


#s = set()
r = [[[], 0] for _ in basis]
a = 1
for x in range(50000):
    a = add_one(a)
    for i, e in enumerate(decompose(a)):
        if len(r[i][0]) == 0:
            r[i][0].append(i)
        else:
            if r[i][0] == e:

    #s.add(a)
#print(len(s))


#print(decompose(add_one(1)), decompose(add(1, 9)))


# s = set()
# a = 1 # i dont know how to prove it properly, but emperically a = 1 is guaranteed to create maximal len(s)
# # TODO: how to get len(s) known a and basis
# for _ in range(accmul):
#     a = add_one(a)
#     s.add(a)
