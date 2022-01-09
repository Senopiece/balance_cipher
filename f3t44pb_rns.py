# from 3 to 44 primes basis (the beauty of this basis is that it is 255 bits in encoding)
from rns import RNS

# from sympy import prime
# f3t44p = tuple(prime(n) for n in range(3, 45))

f3t44p = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193)

def f3t44pb_rns(num):
    assert isinstance(num, int)
    return RNS(num, f3t44p)