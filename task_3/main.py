import math


def main(m, b, a, p):
    f1 = 0
    f2 = 0
    for c in range(1, b + 1):
        for j in range(1, m + 1):
            f1 += (abs(c)) ** 6 - 63 * math.cos(c + 96 + j ** 2) ** 5
    for j in range(1, a + 1):
        f2 += abs(45 * p ** 2 + 76 + 87 * j) ** 3 + \
              1 + math.floor(p / 76 + j ** 2) ** 7
    f = f1 + f2
    return f


print(main(2, 3, 3, -0.79))
print(main(7, 5, 3, 0.52))
