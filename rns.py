class ComposedNumber:
    _data = None
    _basis = None
    _basis_mul = None


    def __init__(self, basis):
        assert isinstance(basis, tuple)
        self._data = 0
        self._basis = basis # <- final

        # slow at the creation, takes more memory, but efficient in calculations
        self._basis_mul = [1]
        for e in basis:
            self._basis_mul.append(self._basis_mul[-1] * e)
        # self._basis_mul <- final


    def __getitem__(self, i):
        return (self._data // self._basis_mul[i]) % self._basis[i]
    

    def __setitem__(self, i, v):
        assert 0 <= v < self._basis[i]
        delta = v - self[i]
        self._data += delta * self._basis_mul[i]
    

    def __eq__(self, other):
        assert isinstance(other, ComposedNumber)
        return self._data == other._data
    

    def __str__(self):
        decomposition = ""
        for i in range(len(self)):
            decomposition += str(self[i]) + (" " if i != len(self) - 1 else "")
        return "(" + decomposition + ")"
    

    def __len__(self):
        return len(self._basis)


class RNS:
    _data : ComposedNumber = None

    def __init__(self, num, basis=None):
        assert (isinstance(num, int) and isinstance(basis, tuple)) or (isinstance(num, ComposedNumber) and basis == None), \
            "constructor parameter must be a integer to convert or a raw data (ComposedNumber)"
        if isinstance(num, int):
            decomposition = ComposedNumber(basis)
            for i, e in enumerate(basis):
                decomposition[i] = num % e
            num = decomposition
        self._data = num
    

    def __add__(self, other):
        assert isinstance(other, RNS)
        assert self._data._basis == other._data._basis

        local_data = ComposedNumber(self._data._basis)

        for i in range(len(self._data)):
            local_data[i] = (self._data[i] + other._data[i]) % self._data._basis[i]

        return RNS(local_data)
    

    def __sub__(self, other):
        assert isinstance(other, RNS)
        assert self._data._basis == other._data._basis

        local_data = ComposedNumber(self._data._basis)

        for i in range(len(self._data)):
            local_data[i] = (self._data[i] - other._data[i]) % self._data._basis[i]

        return RNS(local_data)
    

    def __mul__(self, other):
        assert isinstance(other, RNS)
        assert self._data._basis == other._data._basis

        local_data = ComposedNumber(self._data._basis)

        for i in range(len(self._data)):
            local_data[i] = (self._data[i] * other._data[i]) % self._data._basis[i]

        return RNS(local_data)

    
    def __eq__(self, other):
        assert isinstance(other, RNS)
        assert self._data._basis == other._data._basis
        return other._data == self._data # delegates to ComposedNumber == ComposedNumber
    

    def __str__(self):
        return str(self._data) # delegates to str(ComposedNumber)