from copy import deepcopy


# TODO: metaclass
class EllipticPoint:
    def __init__(self, xo, yo):
        # curve: y^2 = x^3+486662x^2+x

        assert isinstance(xo, int)
        assert isinstance(yo, int)

        self.x = xo
        self.y = yo
    

    def __eq__(self, other):
        assert isinstance(other, EllipticPoint)
        return other.x == self.x and other.y == self.y
    

    def __add__(self, other):
        self == other # assert
        res = deepcopy(self)
        res.x = (self.data * other.data) % self.module
        return res
    

    def __sub__(self, other):
        self == other # assert
        res = deepcopy(self)
        res.data = (self.data * pow(other.data, -1, self.module)) % self.module
        return res
    

    def __mul__(self, n):
        assert isinstance(n, int) # scalar mul
        res = deepcopy(self)
        res.data = pow(self.data, n, self.module)
        return res
    

    def __str__(self):
        return str(self.data)