a, b = map(int, input().split())


def lcm(x, y):
    import math

    return x * y // math.gcd(x, y)


if lcm(a, b) > 10**18:
    print("Large")
else:
    print(lcm(a, b))
