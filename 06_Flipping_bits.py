def flippingBits(n):
    # Use bitwise XOR with 2**32 - 1 to flip the bits
    return n ^ 0xFFFFFFFF