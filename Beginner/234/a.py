t = int(input())


def f(n):
    return n**2 + 2 * n + 3


print(f(f(f(t) + t) + f(f(t))))
