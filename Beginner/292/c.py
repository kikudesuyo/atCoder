import math

n = int(input())


def add_cnt(n):
    return n - 1


def mul_cnt(n):
    cnt = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
    if n == math.isqrt(n) ** 2:
        return cnt * 2 - 1
    else:
        return cnt * 2


ans = 0
flag = False
for i in range(1, n):
    ab, cd = i, n - i
    tmp = mul_cnt(ab) * mul_cnt(cd)
    ans += tmp
print(ans)
