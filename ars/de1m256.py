from arc.DiscreteExponent import DiscreteExponent

def encode(n):
    return DiscreteExponent(1, 2**256, n)

# properties:
# - period: 2**254