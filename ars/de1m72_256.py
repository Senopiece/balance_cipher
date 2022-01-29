from arc.DiscreteExponent import DiscreteExponent

def encode(n):
    return DiscreteExponent(1, 61, 7*2**256, n)

# properties:
# - period: 3*2**254