class ComposedNumber:
    _data = None
    _basis = None
    _basis_mul = None


    def __init__(self, basis, data=None):
        assert isinstance(basis, tuple)
        self._data = 0
        self._basis = basis # <- final

        # slow at the creation, takes more memory, but efficient in calculations
        self._basis_mul = [1]
        for e in basis:
            self._basis_mul.append(self._basis_mul[-1] * e)
        # self._basis_mul <- final

        if data is not None:
            assert isinstance(data, int)
            self._data = data


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
        return str(tuple(self))
    

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
    

    def raw(self, mask=None):
        if mask is not None:
            assert all(isinstance(x, bool) for x in mask)
            assert isinstance(mask, tuple)
            assert len(mask) == len(self._data)

            masked_basis = []
            for i, e in enumerate(self._data._basis):
                if mask[i]:
                    masked_basis.append(e)
            
            masked_raw = ComposedNumber(tuple(masked_basis))

            j = 0
            for i in range(len(self._data)):
                if mask[i]:
                    masked_raw[j] = self._data[i]
                    j += 1

            return masked_raw
            
        else:
            return self._data._data
    

    def mask(self, mask):
        return RNS(self.raw(mask))
    

    def set_raw(self, new_raw):
        self._data._data = new_raw


    def decode(self):
        from sympy.ntheory.modular import crt
        return crt(self._data._basis, list(self._data))[0]
    

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