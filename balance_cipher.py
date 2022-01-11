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
    # NOTE: quantum computer can easily perform such algorithm, so there is another idea in new_algebraic_ring.py
    # TODO: check discrete log for this
    res = 0
    while x != 1:
        x = atomic_add(x, -1)
        res += 1
    return res


class Crypted:
    _data = None

    def __init__(self, n=0):
        self._data = encode(n)
    
    def __add__(self, other):
        assert isinstance(other, Crypted)
        res = Crypted()
        res._data = (self._data * other._data) % module
        return res
    
    def __sub__(self, other):
        assert isinstance(other, Crypted)
        res = Crypted()
        res._data = (self._data * pow(other._data, -1, module)) % module
        return res
    
    def __mul__(self, n):
        assert isinstance(n, int) # scalar mul
        res = Crypted()
        res._data = pow(self._data, n, module)
        return res
    
    def __eq__(self, other):
        assert isinstance(other, Crypted)
        return other._data == self._data
    
    def __str__(self):
        return str(self._data)


# sender secret
balance1 = 60

# sender open data (all the calculations are performed privately)
m1 = 61831996350531240199057085283232358026495125261252625916218455899905125740353
m2 = 77347096829997860251145238741378512327304242939718028116032409255917948845697
A1 = Crypted(m1*balance1)
A2 = Crypted(m2*(balance1 - 40))

# recipient secret
balance2 = 3456

# recipient open data (all the calculations are performed privately)
g1 = 42334496918515581520281029467747373373690656937939313516048188657552755383937
g2 = 97680493710316016549179486752524137080160327319815402918319565371107429039937
B1 = Crypted(g1*balance2)
B2 = Crypted(g2*(balance2 + 40))

# verification
l = (B2*m2 + A2*g2)*m1*g1
r = (B1*m1 + A1*g1)*m2*g2

print(f"l = {l}")
print(f"r = {r}")
print("l == r ✓" if l == r else "l != r")