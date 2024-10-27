from decimal import Decimal

x, k = map(int, input().split())


def f(x, k):
    return Decimal(x).quantize(Decimal(f"1E{k}"), rounding="ROUND_HALF_UP")


for i in range(k):
    x = f(x, i + 1)
print(int(x))
