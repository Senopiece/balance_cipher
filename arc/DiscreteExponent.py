from copy import deepcopy


class DiscreteExponent:
    def __init__(self, o, b, m, n=None):
        assert isinstance(m, int)
        assert isinstance(b, int)
        assert isinstance(o, int)

        self.module = m
        self.base = b
        self.origin = o

        if n is not None:
            assert isinstance(n, int)
            self.data = o
            self.data = (self + n).data
    

    def __add__(self, other):
        assert isinstance(other, DiscreteExponent) or isinstance(other, int)
        res = deepcopy(self)

        if isinstance(other, int):
            # works like this + DiscreteExponent(other)
            res.data = (pow(self.base, other, self.module))*self.data % self.module
        elif isinstance(other, DiscreteExponent):
            self == other # assert
            res.data = (self.data * other.data) % self.module
        
        return res
    

    def __sub__(self, other):
        assert isinstance(other, DiscreteExponent) or isinstance(other, int)
        res = deepcopy(self)

        if isinstance(other, int):
            res.data = (pow(self.base, -other, self.module))*self.data % self.module
        elif isinstance(other, DiscreteExponent):
            self == other # assert
            res.data = (self.data * pow(other.data, -1, self.module)) % self.module
        
        return res
    

    def __mul__(self, n):
        assert isinstance(n, int) # scalar mul
        res = deepcopy(self)
        res.data = pow(self.data, n, self.module)
        return res
    

    def __eq__(self, other):
        assert isinstance(other, DiscreteExponent)
        assert self.module == other.module
        assert self.origin == other.origin
        assert self.base == other.base
        return other.data == self.data
    

    def __str__(self):
        return str(self.data)