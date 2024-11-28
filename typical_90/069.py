import math

n, k = map(int, input().split())

if n >= 5 and k < 5:
    print(0)
    exit()
if n < 5 and k < n:
    print(0)
    exit()
if n < 5:
    ans = 1
    for i in range(n):
        ans *= k - i
        ans %= 10**9 + 7
    print(ans)
    exit()

ans = k * (k - 1)
t = pow(k - 2, n - 2, 10**9 + 7)
ans *= t
ans %= 10**9 + 7
print(ans)
