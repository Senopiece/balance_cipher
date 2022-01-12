# future ResidueSequence

basis = (2, 3, 5)

accmul = 1
for e in basis:
    accmul *= e


def add_one(a):
    res = 0
    m = 1
    for e in basis:
        res += (a % e) * m
        m *= e
    return res


def add(a, b):
    return a*b


def atomic_add(x):
    return (x % 2) + (x % 3)*2 + (x % 5)*2*3


def double_atomic_add(x):
    return (x % 2) + ((x % (2*3)) // 2)*2 + ( ( (x % 2) + (x % 3)*2 + (x % 5)*2*3 ) % 5)*2*3


def triple_atomic_add(x):
    a = atomic_add(x)
    return (x % 2) + (( ((x % 2) + (x % 3)*2) % (2*3)) // 2)*2 + ( ( (a % 2) + (a % 3)*2 + (a % 5)*2*3 ) % 5)*2*3


def sub_one(a):
    from sympy.ntheory.modular import crt
    v = []
    for e in basis:
        v.append(a % e)
        a //= e
    return crt(basis, v)[0]



# s = set()
# a = 1 # i dont know how to prove it properly, but emperically a = 1 is guaranteed to create maximal len(s)
# # TODO: how to get len(s) known a and basis
# for _ in range(accmul):
#     a = atomic_add(a)
#     s.add(a)

# print(accmul/len(s))

# for x in range(30):
#     print( (x % 2) + (x % 3)*2 + (x % 5)*2*3 )
    #print( ( (x % 2) + (x % 3)*2 + (x % 5)*2*3 ) % 5 )
    #print(atomic_add2(atomic_add2(x)) == double_atomic_add2(x))
