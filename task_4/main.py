def main(n):
    f0 = -0.07
    if n == 0:
        return f0
    elif n >= 1:
        fn = main(n - 1)
        return (fn ** 3) / 8 - fn - 1


print(main(6))
print(main(3))
