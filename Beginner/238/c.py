str_n = input()
d = len(str_n) - 1
n = int(str_n)


def tousa(n):
    return n * (n + 1) // 2


cnt = 0
for i in range(d):
    cnt += tousa(9 * 10**i)
    cnt %= 998244353

diff = n - 10**d
cnt += tousa(diff + 1)
cnt %= 998244353
print(cnt)
