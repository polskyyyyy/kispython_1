import math


def main(z, x):
    f = math.sqrt(x/10+z**5)
    t = math.sqrt((43*z**3+45+31*z**2)**6/71-43*(10*x**3+1+66*z)**4)
    return f - t

print(main(0.65, -0.57))