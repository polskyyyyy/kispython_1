import math


def main(y):
    if y < 5:
        f = (abs(y)) ** 6 - 63 * math.cos(y + 96 + y ** 2) ** 5
    elif 5 <= y < 15:
        f = (math.atan(y) ** 2) / 84
    elif 15 <= y < 43:
        f = 3 * (78 * y ** 2 - 42) ** 4 - (62 * y ** 3 - 65 * y) - math.log(95 * y ** 2 - 1) ** 3
    elif 43 <= y < 132:
        f = y - 0.04 - math.floor(y / 76 + y ** 2) ** 7 - 1
    elif 132 <= y:
        f = y ** 5
    return (f)


print(main(59))
