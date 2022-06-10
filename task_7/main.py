def main(x):
    a = x & 0b1111_1111_1111_11
    b = (x >> 14) & 0b1111_1111
    c = (x >> 22) & 0b1111_1111_1
    d = (x >> 31) & 0b1
    result = d | (a << 1) | (c << 15) | (b << 24)
    return result


print(hex(main(0xc09c5d0e)))
print(hex(main(0x475a53b0)))
