from copy import deepcopy


class ResidueSequence:
    def __init__(self, o, b, n=None):
        assert isinstance(o, int)
        assert isinstance(b, tuple)
        assert all(isinstance(e, int) for e in b)

        self.basis = b
        self.origin = o

        if n is not None:
            assert isinstance(n, int)
            # TODO
    

    def __add__(self, other):
        return 0 # TODO
    

    def __sub__(self, other):
        return 0 # TODO
    

    def __mul__(self, n):
        return 0 # TODO
    

    def __eq__(self, other):
        return 0 # TODO
    

    def __str__(self):
        return str(self.data)