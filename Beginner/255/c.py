x, a, d, n = map(int, input().split())

if d < 0:  # 公差が正の等差数列に変更
    a += d * (n - 1)
    d *= -1


def arithmetic_i(a, d, i):
    return a + (i - 1) * d


if d == 0:
    print(abs(x - a))
    exit()

k = ((x - a) / d) + 1
if k < 1:
    print(a - x)
    exit()
elif k > n:
    print(abs(arithmetic_i(a, d, n) - x))
    exit()


k_arith = arithmetic_i(a, d, int(k))
k1_arith = arithmetic_i(a, d, int(k + 1))

print(min(abs(k_arith - x), abs(k1_arith - x)))
