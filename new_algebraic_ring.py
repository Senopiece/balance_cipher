basis = (2, 5, 11)

accmul = 1
for e in basis:
    accmul *= e


def atomic_add(x):
    res = 0
    m = 1
    for e in basis:
        res += (x % e) * m
        m *= e
    return res


def atomic_sub(x):
    from sympy.ntheory.modular import crt
    v = []
    for e in basis:
        v.append(x % e)
        x //= e
    return crt(basis, v)[0]



s = set()
a = 1 # i dont know how to prove it properly, but emperically a = 1 is guaranteed to create maximal len(s)
# TODO: how to get len(s) known a and basis
for _ in range(accmul):
    a = atomic_add(a)
    s.add(a)

print(accmul/len(s))
