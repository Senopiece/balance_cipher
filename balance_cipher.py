module = 2**256


def atomic_add(x, n):
    # where x is in the domain and n is just a scalar to add
    return (pow(529, n, module))*x % module


def encode(x):
    # where x is just a scalar to be represented in the domain
    return atomic_add(1, x)


def decode(x):
    # where x is in the domain
    # NOTE: it is good here to be such slow
    # TODO: check discrete log for this
    res = 0
    while x != 1:
        x = atomic_add(x, -1)
        res += 1
    return res


def add(a, b):
    # where a and b are both in the domain
    return (a * b) % module
    # works as
    # while b != origin: # usually origin = 1
    #     b = atomic_add(b, -1)
    #     a = atomic_add(a, 1)
    # return a


def mul(a, n):
    # where a is in domain and n is just a number (scalar multiplication)
    return pow(a, n, module)


# sender secret
balance1 = 60

# sender open data (all the calculations are performed privately)
M1 = 40858891157460307674354882010572547498271232277915032737235431902522015964929
cb1 = encode(M1*balance1)
cb1n = encode(M1*(balance1 - 40))

# recipient secret
balance2 = 3456

# recipient open data (all the calculations are performed privately)
M2 = 105378189937130164065839937598184558310536310992898322397669330185205034255393
cb2 = encode(M2*balance2)
cb2n = encode(M2*(balance2 + 40))

# verification
def is_positive(x, m):
    neg = encode(-m)
    for _ in range(1000):
        if neg == x:
            return False
        neg = atomic_add(neg, -m)
    return True
    

l = add(mul(cb2n, M1), mul(cb1n, M2))
r = add(mul(cb2, M1), mul(cb1, M2))


print(f"sign: cb1n[{'+' if is_positive(cb1n, M1) else '-'}] cb2n[{'+' if is_positive(cb2n, M2) else '-'}] ")
print(f"l = {l}")
print(f"r = {r}")
print("l == r ✓" if l == r else "l != r")