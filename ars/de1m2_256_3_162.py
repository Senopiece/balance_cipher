from arc.DiscreteExponent import DiscreteExponent

def encode(n):
    return DiscreteExponent(1, 61, 2**256 * 3**162, n)