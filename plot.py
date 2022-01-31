import matplotlib.pyplot as plt
from math import lcm, gcd


def f(a, b, c):
    return lcm(a+c, b+2*c)


def find_c_for_minimal_lcm(a, b):
    assert a - b > 0
    mlcm = lcm(a, b)
    best_c = 0
    for c in range(0, a-b):
        if lcm(a+c, b+2*c) < mlcm:
            best_c = c
    return best_c


a = 455
b = a-234
c = find_c_for_minimal_lcm(a, b)
print(lcm(a, b))
print(lcm((a+c), (b+2*c)))
print(c)
plt.plot([f(a, b, c) for c in range(a-b)])
plt.plot([(a+c)*(b+2*c) for c in range(a-b)])
plt.show()