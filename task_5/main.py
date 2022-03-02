import math


def main(z, x):
    f = 0
    for i in range(1, len(z) + 1):
        f += 3 * ((z[math.ceil(i / 4 - 1)]) ** 3 -
                  42 * x[math.ceil(i / 3 - 1)]) ** 2
    return f * 63


print(main([-0.49, -0.29, -0.56, -0.72, -0.01, -0.74, -0.75], [-0.19, -0.15, -0.06, -0.5, -0.63, 0.51, -0.51]))
